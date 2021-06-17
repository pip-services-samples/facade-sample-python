# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, Any

from pip_services3_commons.data import DataPage, PagingParams, FilterParams

from pip_facades_sample_python.clients.version1.SessionV1 import SessionV1


class ISessionsClientV1(ABC):
    @abstractmethod
    def get_sessions(self, correlation_id: Optional[str], filter_params: FilterParams,
                     paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_session_by_id(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        pass

    @abstractmethod
    def open_session(self, correlation_id: Optional[str], user_id: str, user_name: str,
                     address: str, client: str, user: Any, data: Any, )->SessionV1:
        pass

    @abstractmethod
    def store_session_data(self, correlation_id: Optional[str], session_id: str, data: Any) -> SessionV1:
        pass

    @abstractmethod
    def update_session_user(self, correlation_id: Optional[str], session_id: str, user: Any) -> SessionV1:
        pass

    @abstractmethod
    def close_session(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        pass

    @abstractmethod
    def delete_session_by_id(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        pass
