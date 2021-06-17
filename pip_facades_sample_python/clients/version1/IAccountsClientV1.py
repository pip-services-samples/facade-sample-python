# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage
from pip_facades_sample_python.clients.version1.AccountV1 import AccountV1


class IAccountsClientV1(ABC):

    @abstractmethod
    def get_accounts(self, correlation_id: Optional[str], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_account_by_id(self, correlation_id: Optional[str], id: str, ) -> AccountV1:
        pass

    @abstractmethod
    def get_account_by_login(self, correlation_id: Optional[str], login: str) -> AccountV1:
        pass

    @abstractmethod
    def get_account_by_id_or_login(self, correlation_id: Optional[str], ir_or_login: str) -> AccountV1:
        pass

    @abstractmethod
    def create_account(self, correlation_id: Optional[str], account: AccountV1) -> AccountV1:
        pass

    @abstractmethod
    def update_account(self, correlation_id: Optional[str], account: AccountV1) -> AccountV1:
        pass

    @abstractmethod
    def delete_account_by_id(self, correlation_id: Optional[str], id: str) -> AccountV1:
        pass
