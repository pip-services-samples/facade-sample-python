# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List, Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage, IdGenerator
from pip_services3_commons.errors import BadRequestException

from pip_facades_sample_python.clients.version1.AccountV1 import AccountV1
from pip_facades_sample_python.clients.version1.IAccountsClientV1 import IAccountsClientV1


class AccountsMemoryClientV1(IAccountsClientV1):

    def __init__(self, *accounts: AccountV1):
        self.__max_page_size = 100
        self.__accounts: List[AccountV1] = list(accounts)

    def __match_string(self, value: str, search: str) -> bool:
        if value is None and search is None:
            return True
        if value is None or search is None:
            return False
        return value.lower().find(search) >= 0

    def __match_search(self, item: AccountV1, search: str) -> bool:
        search = search.lower()
        if self.__match_string(item.name, search):
            return True

        return False

    def __compose_filter(self, filter_params: FilterParams):
        filter_params = filter_params or FilterParams()
        search = filter_params.get_as_nullable_string('search')
        id = filter_params.get_as_nullable_string('id')
        name = filter_params.get_as_nullable_string('name')
        login = filter_params.get_as_nullable_string('login')
        active = filter_params.get_as_nullable_boolean('active')
        from_create_time = filter_params.get_as_nullable_datetime('from_create_time')
        to_create_time = filter_params.get_as_nullable_datetime('to_create_time')
        deleted = filter_params.get_as_boolean_with_default('deleted', False)

        def inner(item: AccountV1):
            if search is not None and not self.__match_search(item, search):
                return False
            if id is not None and id != item.id:
                return False
            if name is not None and name != item.name:
                return False
            if login is not None and login != item.login:
                return False
            if active is not None and active != item.active:
                return False
            if from_create_time is not None and item.create_time >= from_create_time:
                return False
            if to_create_time is not None and item.create_time < to_create_time:
                return False
            if not deleted and item.deleted:
                return False
            return True

        return inner

    def get_accounts(self, correlation_id: Optional[str], filter_params: FilterParams,
                     paging: PagingParams) -> DataPage:
        filter_curl = self.__compose_filter(filter_params)
        accounts = list(filter(filter_curl, self.__accounts))

        # Extract a page
        paging = PagingParams() if paging is None else paging
        skip = paging.get_skip(-1)
        take = paging.get_take(self.__max_page_size)

        total = None
        if paging.total:
            total = len(accounts)

        if skip > 0:
            accounts = accounts[skip:]

        accounts = accounts[:take]

        page = DataPage(accounts, total)

        return page

    def get_account_by_id(self, correlation_id: Optional[str], id: str, ) -> AccountV1:
        accounts = list(filter(lambda x: x.id == id, self.__accounts))
        account = None if len(accounts) <= 0 else accounts[0]

        return account

    def get_account_by_login(self, correlation_id: Optional[str], login: str) -> AccountV1:
        accounts = list(filter(lambda x: x.login == login, self.__accounts))
        account = None if len(accounts) <= 0 else accounts[0]

        return account

    def get_account_by_id_or_login(self, correlation_id: Optional[str], id_or_login: str) -> AccountV1:
        accounts = list(filter(lambda x: x.id == id_or_login or x.login == id_or_login, self.__accounts))
        account = None if len(accounts) <= 0 else accounts[0]

        return account

    def create_account(self, correlation_id: Optional[str], account: AccountV1) -> Optional[AccountV1]:
        if account is None:
            return

        accounts = list(filter(lambda x: x.id == account.id or x.login == account.login, self.__accounts))
        if len(accounts) > 0:
            raise BadRequestException(correlation_id, 'DUPLICATE_LOGIN', 'Found account with duplicate login')

        account = deepcopy(account)
        account.id = account.id or IdGenerator.next_long()

        self.__accounts.append(account)

        return account

    def update_account(self, correlation_id: Optional[str], account: AccountV1) -> Optional[AccountV1]:
        filtered = list(map(lambda x: x.id, self.__accounts))

        if filtered.count(account.id) <= 0:
            return

        index = filtered.index(account.id)

        account = deepcopy(account)
        self.__accounts[index] = account

        return account

    def delete_account_by_id(self, correlation_id: Optional[str], id: str) -> Optional[AccountV1]:
        index = list(map(lambda x: x.id, self.__accounts)).index(id)
        item = self.__accounts[index]

        if index < 0:
            return

        item.deleted = True

        return item
