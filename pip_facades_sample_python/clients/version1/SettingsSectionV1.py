# -*- coding: utf-8 -*-
import datetime

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.data import IStringIdentifiable


class SettingsSectionV1(IStringIdentifiable):

    def __init__(self, id: str, parameters: ConfigParams = None):
        self.id: str = id
        self.parameters: ConfigParams = parameters or ConfigParams()
        self.update_time: datetime.datetime = datetime.datetime.now()
