# -*- coding: utf-8 -*-
"""
    step8.clients.BeaconsDirectClientV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsDirectClientV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.refer import Descriptor
from pip_services3_rpc.clients import DirectClient

from .IBeaconsClientV1 import IBeaconsClientV1


class BeaconsDirectClientV1(DirectClient, IBeaconsClientV1):
    def __init__(self):
        super(BeaconsDirectClientV1, self).__init__()
        self._dependency_resolver.put('controller', Descriptor('beacons', 'controller', '*', '*', '1.0'))

    def get_beacons_by_filter(self, correlation_id, filter, paging):
        timing = self._instrument(correlation_id, 'beacons.get_beacons')
        result = self._controller.get_beacons_by_filter(correlation_id, filter, paging)
        timing.end_timing()
        return result

    def get_beacon_by_id(self, correlation_id, id):
        timing = self._instrument(correlation_id, 'beacons.get_beacon_by_id')
        result = self._controller.get_beacon_by_id(correlation_id, id)
        timing.end_timing()
        return result

    def get_beacon_by_udi(self, correlation_id, udi):
        timing = self._instrument(correlation_id, 'beacons.get_beacon_by_udi')
        result = self._controller.get_beacon_by_udi(correlation_id, udi)
        timing.end_timing()
        return result

    def calculate_position(self, correlation_id, site_id, udis):
        timing = self._instrument(correlation_id, 'beacons.calculate_position')
        result = self._controller.calculate_position(correlation_id, site_id, udis)
        timing.end_timing()
        return result

    def create_beacon(self, correlation_id, entity):
        timing = self._instrument(correlation_id, 'beacons.create_beacon')
        result = self._controller.create_beacon(correlation_id, entity)
        timing.end_timing()
        return result

    def update_beacon(self, correlation_id, entity):
        timing = self._instrument(correlation_id, 'beacons.update_beacon')
        result = self._controller.update_beacon(correlation_id, entity)
        timing.end_timing()
        return result

    def delete_beacon_by_id(self, correlation_id, id):
        timing = self._instrument(correlation_id, 'beacons.delete_beacon_by_id')
        result = self._controller.delete_beacon_by_id(correlation_id, id)
        timing.end_timing()
        return result

