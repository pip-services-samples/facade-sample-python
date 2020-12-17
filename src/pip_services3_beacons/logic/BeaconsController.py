# -*- coding: utf-8 -*-
"""
    step8.logic.BeaconsController
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsController class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.commands import ICommandable
from pip_services3_commons.config import IConfigurable
from pip_services3_commons.data import FilterParams
from pip_services3_commons.refer import IReferenceable, Descriptor

from ..logic.IBeaconsController import IBeaconsController
from ..logic.BeaconsCommandSet import BeaconsCommandSet


class BeaconsController(IBeaconsController, IConfigurable, IReferenceable, ICommandable):
    _persistence = None
    _commandSet = None
    def __init__(self):
        pass


    def configure(self, config):
        pass

    def get_command_set(self):
        if self._commandSet == None:
            self._commandSet = BeaconsCommandSet(self)
        return self._commandSet

    def set_references(self, references):
        self._persistence = references.get_one_required(Descriptor("beacons", "persistence", "*", "*", "1.0"))

    def get_beacons_by_filter(self, correlation_id, filter, paging):
        return self._persistence.get_page_by_filter(correlation_id, filter, paging)

    def get_beacon_by_id(self, correlation_id, id):
        return self._persistence.get_one_by_id(correlation_id, id)

    def get_beacon_by_udi(self, correlation_id, udi):
        return self._persistence.get_one_by_udi(correlation_id, udi)

    def calculate_position(self, correlation_id, site_id, udis):
        if udis == None or len(udis) == 0:
            return None

        result = self._persistence.get_page_by_filter(correlation_id, FilterParams.from_tuples("site_id", site_id, "udis", udis), None)
        beacons = result.data

        lat = 0
        lng = 0
        count = 0
        for beacon in beacons:
            if beacon['center'] != None and beacon['center']['type'] == "Point" and len(beacon['center']['coordinates']) > 1:
                lng = lng + beacon['center']['coordinates'][0]
                lat = lat + beacon['center']['coordinates'][1]
                count = count + 1

        if count > 0:
            position = {"type": 'Point', "coordinates": [lng / count, lat / count]}
            return position
        return None


    def create_beacon(self, correlation_id, entity):
        return self._persistence.create(correlation_id, entity)

    def update_beacon(self, correlation_id, entity):
        return self._persistence.update(correlation_id, entity)

    def delete_beacon_by_id(self, correlation_id, id):
        return self._persistence.delete_by_id(correlation_id, id)
