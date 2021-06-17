# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from pip_facades_sample_python.clients.version1.UserPasswordInfoV1 import UserPasswordInfoV1


class IPasswordsClientV1(ABC):
    @abstractmethod
    def get_password_info(self, correlation_id: Optional[str], user_id: str) -> UserPasswordInfoV1:
        pass

    @abstractmethod
    def set_temp_password(self, correlation_id: Optional[str], user_id: str) -> str:
        pass

    @abstractmethod
    def set_password(self, correlation_id: Optional[str], user_id: str, password: str):
        pass

    @abstractmethod
    def delete_password(self, correlation_id: Optional[str], user_id: str):
        pass

    @abstractmethod
    def authenticate(self, correlation_id: Optional[str], user_id: str, password: str) -> bool:
        pass

    @abstractmethod
    def change_password(self, correlation_id: Optional[str], user_id: str, old_password: str, new_password: str):
        pass

    @abstractmethod
    def validate_code(self, correlation_id: Optional[str], user_id: str, code: str) -> bool:
        pass

    @abstractmethod
    def reset_password(self, correlation_id: Optional[str], user_id: str, code: str, password: str):
        pass

    @abstractmethod
    def recover_password(self, correlation_id: Optional[str], user_id: str):
        pass
