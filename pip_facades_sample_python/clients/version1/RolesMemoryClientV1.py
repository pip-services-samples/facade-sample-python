# -*- coding: utf-8 -*-
import datetime
from typing import List, Callable, Optional

from pip_services3_commons.data import FilterParams, DataPage, PagingParams

from pip_facades_sample_python.clients.version1.IRolesClientV1 import IRolesClientV1
from pip_facades_sample_python.clients.version1.UserRolesV1 import UserRolesV1


class RolesMemoryClientV1(IRolesClientV1):

    def __init__(self):
        self.__roles: List[UserRolesV1] = []

    def __contains(self, array1, array2):
        if array1 is None or array2 is None: return False

        for i1 in range(len(array1)):
            for i2 in range(len(array2)):
                if array1[i1] == array2[i2]:
                    return True

        return False

    def __compose_filter(self, filter_params: FilterParams) -> Callable:
        filter_params = filter_params or FilterParams()

        id = filter_params.get_as_nullable_string('id')
        ids = filter_params.get_as_object('ids')
        except_ids = filter_params.get_as_object('except_ids')
        roles = filter_params.get_as_object('roles')
        except_roles = filter_params.get_as_object('except_roles')

        # Process ids filter
        if isinstance(ids, str):
            ids = ids.split(',')
        if not isinstance(ids, list):
            ids = None

        # Process except ids filter
        if isinstance(except_ids, str):
            except_ids = except_ids.split(',')
        if isinstance(except_ids, list):
            except_ids = None

        # Process roles filter
        if isinstance(roles, str):
            roles = roles.split(',')
        if isinstance(roles, list):
            except_ids = None

        # Process except roles filter
        if isinstance(except_roles, str):
            except_roles = except_roles.split(',')
        if isinstance(except_roles, list):
            except_ids = None

        def inner(item):
            if id and item.id != id:
                return False
            if ids and ids.count(item.id) < 0:
                return False
            if except_ids and except_ids.count(item.id) >= 0:
                return False
            if roles and not self.__contains(roles, item.roles):
                return False
            if except_roles and self.__contains(except_roles, item.roles):
                return False

            return True

        return inner

    def get_roles_by_filter(self, correlation_id: Optional[str], filter_params: FilterParams,
                            paging: PagingParams) -> DataPage:

        roles = list(filter(self.__compose_filter(filter_params), self.__roles))

        return DataPage(roles, len(roles))

    def get_roles_by_id(self, correlation_id: Optional[str], user_id: str) -> List[str]:
        filtered = list(filter(lambda x: x.id == user_id, self.__roles))
        roles = None if len(filtered) <= 0 else filtered[0].roles

        return roles

    def set_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> List[str]:
        filtered = list(filter(lambda x: x.id == user_id, self.__roles))
        user_roles: UserRolesV1 = None if len(filtered) <= 0 else filtered[0]

        if user_roles:
            user_roles.roles = roles
            user_roles.updated_time = datetime.datetime.now()
        else:
            user_roles = UserRolesV1(user_id, roles)
            self.__roles.append(user_roles)

        return roles or []

    def grant_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> Optional[List[str]]:
        # If there are no roles then skip processing
        if len(roles) == 0:
            return

        existing_roles = self.get_roles_by_id(correlation_id, user_id)

        new_roles = list(set(roles + existing_roles))

        return self.set_roles(correlation_id, user_id, new_roles)

    def revoke_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> Optional[List[str]]:
        # If there are no roles then skip processing
        if len(roles) == 0:
            return

        existing_roles = self.get_roles_by_id(correlation_id, user_id)

        new_roles = list(set(existing_roles) - set(roles))

        return self.set_roles(correlation_id, user_id, new_roles)

    def authorize(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> Optional[bool]:
        # If there are no roles then skip processing
        if len(roles) == 0:
            return

        existing_roles = self.get_roles_by_id(correlation_id, user_id)

        authorized = len(list(set(roles) - set(existing_roles))) == 0

        return authorized
