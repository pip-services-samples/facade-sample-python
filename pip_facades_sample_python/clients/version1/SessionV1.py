# -*- coding: utf-8 -*-
import datetime
from typing import Any

from pip_services3_commons.data import IdGenerator


class SessionV1:
    def __init__(self, id: str, user_id: str, user_name: str = None,
                 address: str = None, client: str = None):

        # Identification
        self.id = id or IdGenerator.next_long()
        self.user_id = user_id
        self.user_name = user_name
        # Session info
        self.active = True
        self.open_time = datetime.datetime.now()
        self.close_time: datetime.datetime = None
        self.request_time = datetime.datetime.now()
        self.address = address
        self.client = client

        # Cached content
        self.user: Any = None
        self.data: Any = None
