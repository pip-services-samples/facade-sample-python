# -*- coding: utf-8 -*-
import datetime
from typing import Any

from pip_services3_commons.data import IStringIdentifiable


class EmailSettingsV1(IStringIdentifiable):

    def __init__(self, id: str = None, name: str = None, email: str = None, language: str = None,
                 subscriptions: Any = None, verified: bool = None, ver_code: str = None,
                 ver_expire_time: datetime.datetime = None, custom_hdr: Any = None, custom_dat: Any = None):

        # Recipient information
        self.id = id
        self.name = name
        self.email = email
        self.language = language

        # Email management
        self.subscriptions = subscriptions
        self.verified = verified
        self.ver_code = ver_code
        self.ver_expire_time = ver_expire_time

        # Email management
        self.custom_hdr = custom_hdr
        self.custom_dat = custom_dat
