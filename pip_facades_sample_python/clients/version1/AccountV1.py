# -*- coding: utf-8 -*-
import datetime
from typing import Optional, Any, List

from pip_services3_commons.data import IStringIdentifiable

from pip_facades_sample_python.clients.version1.SiteV1 import SiteV1


class AccountV1(IStringIdentifiable):

    def __init__(self, id: str = None, login: str = None, name: str = None, create_time: datetime.datetime = None,
                 deleted: Optional[bool] = None, active: bool = None, time_zone: str = None,
                 language: str = None, theme: str = None, custom_hdr: Any = None, custom_dat: Any = None, sites: List[SiteV1] = None):
        # Identification
        self.id: str = id
        self.login: str = login
        self.name: str = name

        # Activity tracking
        self.create_time: datetime.datetime = create_time
        self.deleted: Optional[bool] = deleted
        self.active: bool = active

        self.create_time = datetime.datetime.now()
        self.active = True
        self.sites = sites

        # User preferences
        self.time_zone: str = time_zone
        self.language: str = language
        self.theme: str = theme

        # Custom fields
        self.custom_hdr: Any = custom_hdr
        self.custom_dat: Any = custom_dat
