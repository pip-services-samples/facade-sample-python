# -*- coding: utf-8 -*-
"""
    step8.persistence.BeaconsMemoryPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsMemoryPersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.data import FilterParams
from pip_services3_data.persistence import IdentifiableMemoryPersistence

from .IBeaconsPersistence import IBeaconsPersistence


class BeaconsMemoryPersistence(IdentifiableMemoryPersistence, IBeaconsPersistence):

    def __init__(self):
        super(BeaconsMemoryPersistence, self).__init__()
        self._maxPageSize = 1000

    def get_page_by_filter(self, correlation_id, filter, paging):
        filter = filter if filter != None else FilterParams()

        id = filter.get_as_nullable_string("id")
        site_id = filter.get_as_nullable_string("site_id")
        label = filter.get_as_nullable_string("label")
        udi = filter.get_as_nullable_string("udi")
        udis = filter.get_as_object("udis")
        if udis != None and len(udis) > 0:
            udis = udis.split(",")

        def filter_beacons(item):
            if id != None and item['id'] != id:
                return False
            if site_id != None and item['site_id'] != site_id:
                return False
            if label != None and item['label'] != label:
                return False
            if udi != None and item['udi'] != udi:
                return False
            if udis != None and item['udi'] not in udis:
                return False
            return True

        return super(BeaconsMemoryPersistence, self).get_page_by_filter(correlation_id, filter_beacons, paging=paging)

    def get_one_by_udi(self, correlation_id, udi):
        if udi == None:
            return None
        for item in self._items:
            if udi == item['udi']:
                return item

