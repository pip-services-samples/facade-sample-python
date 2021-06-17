# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC
from typing import Optional, List

from pip_facades_sample_python.clients.version1.EmailSettingsV1 import EmailSettingsV1


class IEmailSettingsClientV1(ABC):

    @abstractmethod
    def get_settings_by_ids(self, correlation_id: Optional[str], recipient_ids: List[str]) -> List[EmailSettingsV1]:
        pass

    @abstractmethod
    def get_settings_by_id(self, correlation_id: Optional[str], recipient_id: str) -> EmailSettingsV1:
        pass

    @abstractmethod
    def get_settings_by_email_settings(self, correlation_id: Optional[str], email: str) -> EmailSettingsV1:
        pass

    @abstractmethod
    def set_settings(self, correlation_id: Optional[str], settings: EmailSettingsV1) -> EmailSettingsV1:
        pass

    @abstractmethod
    def set_verified_settings(self, correlation_id: Optional[str], settings: EmailSettingsV1) -> EmailSettingsV1:
        pass

    @abstractmethod
    def set_recipient(self, correlation_id: Optional[str], recipient_id: str, name: str, email: str,
                      language: str) -> EmailSettingsV1:
        pass

    @abstractmethod
    def set_subscriptions(self, correlation_id: Optional[str], recipient_id: str,
                          subscriptions: any) -> EmailSettingsV1:
        pass

    @abstractmethod
    def delete_settings_by_id(self, correlation_id: Optional[str], recipient_id: str):
        pass

    @abstractmethod
    def resend_verification(self, correlation_id: Optional[str], recipient_id: str):
        pass

    @abstractmethod
    def verify_email(self, correlation_id: Optional[str], recipient_id: str, code: str):
        pass
