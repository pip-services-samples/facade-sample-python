# -*- coding: utf-8 -*-
from typing import Optional

from pip_facades_sample_python.clients.version1.IPasswordsClientV1 import IPasswordsClientV1
from pip_facades_sample_python.clients.version1.UserPasswordInfoV1 import UserPasswordInfoV1


class PasswordsNullClientV1(IPasswordsClientV1):

    def get_password_info(self, correlation_id: Optional[str], user_id: str) -> UserPasswordInfoV1:
        return UserPasswordInfoV1(
            id=user_id,
            change_time=None,
            locked=False,
            lock_time=None
        )

    def set_temp_password(self, correlation_id: Optional[str], user_id: str) -> str:
        return '123'

    def set_password(self, correlation_id: Optional[str], user_id: str, password: str):
        return

    def delete_password(self, correlation_id: Optional[str], user_id: str):
        return

    def authenticate(self, correlation_id: Optional[str], user_id: str, password: str) -> bool:
        return True

    def change_password(self, correlation_id: Optional[str], user_id: str, old_password: str, new_password: str):
        return

    def validate_code(self, correlation_id: Optional[str], user_id: str, code: str) -> bool:
        return True

    def reset_password(self, correlation_id: Optional[str], user_id: str, code: str, password: str):
        return

    def recover_password(self, correlation_id: Optional[str], user_id: str):
        return
