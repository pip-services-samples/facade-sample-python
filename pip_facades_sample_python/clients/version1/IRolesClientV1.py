# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, List

from pip_services3_commons.data import FilterParams, PagingParams, DataPage


class IRolesClientV1(ABC):

    @abstractmethod
    def get_roles_by_filter(self, correlation_id: Optional[str], filter_params: FilterParams,
                            paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_roles_by_id(self, correlation_id: Optional[str], user_id: str) -> List[str]:
        pass

    @abstractmethod
    def set_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> List[str]:
        pass

    @abstractmethod
    def grant_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> List[str]:
        pass

    @abstractmethod
    def revoke_roles(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> List[str]:
        pass

    @abstractmethod
    def authorize(self, correlation_id: Optional[str], user_id: str, roles: List[str]) -> bool:
        pass
