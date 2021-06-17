# -*- coding: utf-8 -*-
import datetime

from pip_services3_commons.data import IStringIdentifiable


class UserPasswordInfoV1(IStringIdentifiable):
    def __init__(self, id: str = None, change_time: datetime.datetime = None, locked: bool = None,
                 lock_time: datetime.datetime = None):
        self.id = id
        self.change_time = change_time
        self.locked = locked
        self.lock_time = lock_time
