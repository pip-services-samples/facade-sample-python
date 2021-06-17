# -*- coding: utf-8 -*-
import datetime
from typing import Optional, Any

from pip_services3_commons.data import IStringIdentifiable


class SiteV1(IStringIdentifiable):
    def __init__(self, id: str = None, code: Optional[str] = None, create_time: Optional[datetime.datetime] = None,
                 creator_id: Optional[str] = None, deleted: Optional[str] = None, active: bool = None,
                 name: str = None, description: Optional[str] = None, address: Optional[str] = None,
                 center: Optional[Any] = None, radius: Optional[float] = None, geometry: Optional[Any] = None,
                 boundaries: Optional[Any] = None, language: Optional[str] = None, timezone: [str] = None,
                 industry: Optional[str] = None, org_size: Optional[str] = None, total_sites: Optional[int] = None,
                 purpose: Optional[str] = None, params: Optional[Any] = None):

        self.id = id
        self.code = code
        self.create_time = create_time
        self.creator_id = creator_id
        self.deleted = deleted
        self.active = active
        self.name = name
        self.description = description
        self.address = address
        self.center = center
        self.radius = radius  # In km

        self.geometry = geometry  # GeoJSON
        self.boundaries = boundaries  # GeoJSON
        self.language = language
        self.timezone = timezone
        self.industry = industry
        self.org_size = org_size
        self.total_sites = total_sites
        self.purpose = purpose
        self.params = params
