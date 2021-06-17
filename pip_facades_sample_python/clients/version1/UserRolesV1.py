# -*- coding: utf-8 -*-

import datetime
from typing import List

from pip_services3_commons.data import IStringIdentifiable


class UserRolesV1(IStringIdentifiable):

    def __init__(self, id: str, roles: List[str]):
        self.id: str = id
        self.roles: List[str] = roles or []
        self.updated_time: datetime.datetime = datetime.datetime.now()
