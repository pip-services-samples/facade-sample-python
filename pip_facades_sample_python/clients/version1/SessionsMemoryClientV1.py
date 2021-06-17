# -*- coding: utf-8 -*-
from typing import List, Optional, Any

from pip_services3_commons.data import PagingParams, DataPage, FilterParams

from pip_facades_sample_python.clients.version1.ISessionsClientV1 import ISessionsClientV1
from pip_facades_sample_python.clients.version1.SessionV1 import SessionV1


class SessionsMemoryClientV1(ISessionsClientV1):
    def __init__(self):
        self.__sessions: List[SessionV1] = []

    def get_sessions(self, correlation_id: Optional[str], filter_params: FilterParams,
                     paging: PagingParams) -> DataPage:
        return DataPage(self.__sessions, len(self.__sessions))

    def get_session_by_id(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        filtered = list(filter(lambda x: x.id == session_id, self.__sessions))
        sessions = None if len(filtered) <= 0 else filtered[0]
        return sessions

    def open_session(self, correlation_id: Optional[str], user_id: str, user_name: str,
                     address: str, client: str, user: Any, data: Any, ) -> SessionV1:
        session = SessionV1(None, user_id, user_name, address, client)
        session.user = user
        session.data = data

        self.__sessions.append(session)

        return session

    def store_session_data(self, correlation_id: Optional[str], session_id: str, data: Any) -> Optional[SessionV1]:
        return None

    def update_session_user(self, correlation_id: Optional[str], session_id: str, user: Any) -> SessionV1:
        filtered = list(filter(lambda x: x.id == session_id, self.__sessions))
        session = None if len(filtered) <= 0 else filtered[0]
        if session:
            session.user = user

        return session

    def close_session(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        filtered = list(filter(lambda x: x.id == session_id, self.__sessions))
        session = None if len(filtered) <= 0 else filtered[0]
        if session:
            session.active = False

        return session

    def delete_session_by_id(self, correlation_id: Optional[str], session_id: str) -> SessionV1:
        filtered = list(filter(lambda x: x.id == session_id, self.__sessions))
        session = None if len(filtered) <= 0 else filtered[0]
        if session:
            self.__sessions = list(filter(lambda x: x.id != session_id, self.__sessions))

        return session
