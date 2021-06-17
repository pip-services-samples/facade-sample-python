# -*- coding: utf-8 -*-
from typing import List, Optional

from pip_facades_sample_python.clients.version1.EmailSettingsV1 import EmailSettingsV1
from pip_facades_sample_python.clients.version1.IEmailSettingsClientV1 import IEmailSettingsClientV1


class EmailSettingsMemoryClientV1(IEmailSettingsClientV1):

    def __init__(self):
        self.__settings: List[EmailSettingsV1] = []

    def get_settings_by_ids(self, correlation_id: Optional[str], recipient_ids: List[str]) -> List[EmailSettingsV1]:
        settings = list(filter(lambda x: recipient_ids.count(x.id) > 0, self.__settings))
        return settings

    def get_settings_by_id(self, correlation_id: Optional[str], recipient_id: str) -> EmailSettingsV1:
        settings = list(filter(lambda x: x.id == recipient_id, self.__settings))[0]
        return settings

    def get_settings_by_email_settings(self, correlation_id: Optional[str], email: str) -> EmailSettingsV1:
        settings = list(filter(lambda x: x.email == email, self.__settings))[0]
        return settings

    def set_settings(self, correlation_id: Optional[str], settings: EmailSettingsV1) -> EmailSettingsV1:
        settings.verified = False
        settings.subscriptions = settings.subscriptions or {}

        self.__settings = list(filter(lambda x: x.id != settings.id, self.__settings))
        self.__settings.append(settings)
        return settings

    def set_verified_settings(self, correlation_id: Optional[str], settings: EmailSettingsV1) -> EmailSettingsV1:
        settings.verified = True
        settings.subscriptions = settings.subscriptions or {}

        self.__settings = list(filter(lambda x: x.id != settings.id, self.__settings))
        self.__settings.append(settings)
        return settings

    def set_recipient(self, correlation_id: Optional[str], recipient_id: str, name: str, email: str,
                      language: str) -> EmailSettingsV1:

        settings = list(filter(lambda x: x.id == recipient_id, self.__settings))[0]

        if settings:
            settings.name = name
            settings.email = email
            settings.language = language
        else:
            settings = EmailSettingsV1(
                id=recipient_id,
                name=name,
                email=email,
                language=language,
                verified=False,
                subscriptions={}
            )
            self.__settings.append(settings)

        return settings

    def set_subscriptions(self, correlation_id: Optional[str], recipient_id: str,
                          subscriptions: any) -> EmailSettingsV1:

        settings = list(filter(lambda x: x.id == recipient_id, self.__settings))[0]
        if settings:
            settings.subscriptions = subscriptions
        else:
            settings = EmailSettingsV1(
                id=recipient_id,
                name=None,
                email=None,
                language=None,
                subscriptions=subscriptions
            )
            self.__settings.append(settings)

        return settings

    def delete_settings_by_id(self, correlation_id: Optional[str], recipient_id: str):
        self.__settings = list(filter(lambda x: x.id != recipient_id, self.__settings))

    def resend_verification(self, correlation_id: Optional[str], recipient_id: str):
        pass

    def verify_email(self, correlation_id: Optional[str], recipient_id: str, code: str):
        settings = list(filter(lambda x: x.id == recipient_id, self.__settings))

        if settings and settings.ver_code == code:
            settings.verified = True
            settings.ver_code = None
