# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from pip_services3_commons.data import IStringIdentifiable


class InvitationV1(IStringIdentifiable):
    def __init__(self, id: str = None, action: str = None, site_id: str = None, site_name: Optional[str] = None,
                 role: Optional[str] = None, create_time: Optional[datetime.datetime] = None,
                 creator_name: Optional[str] = None, creator_id: str = None,
                 invitee_name: Optional[str] = None, invitee_email: Optional[str] = None,
                 invitee_id: Optional[str] = None,
                 sent_time: Optional[datetime.datetime] = None,
                 expire_time: Optional[datetime.datetime] = None):

        self.id = id
        self.action = action
        self.site_id = site_id
        self.site_name = site_name
        self.role = role
        self.create_time = create_time
        self.creator_name = creator_name
        self.creator_id = creator_id
        self.invitee_name = invitee_name
        self.invitee_email = invitee_email
        self.invitee_id = invitee_id
        self.sent_time = sent_time
        self.expire_time = expire_time
