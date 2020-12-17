# -*- coding: utf-8 -*-
"""
    step8.logic.IBeaconsController
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    IBeaconsController class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IBeaconsController():
    def get_beacons_by_filter(self, correlation_id, filter, paging):
        raise NotImplementedError('Method from interface definition')

    def get_beacon_by_id(self, correlation_id, id):
        raise NotImplementedError('Method from interface definition')

    def get_beacon_by_udi(self, correlation_id, udi):
        raise NotImplementedError('Method from interface definition')

    def calculate_position(self, correlation_id, site_id, udis):
        raise NotImplementedError('Method from interface definition')

    def create_beacon(self, correlation_id, entity):
        raise NotImplementedError('Method from interface definition')

    def update_beacon(self, correlation_id, entity):
        raise NotImplementedError('Method from interface definition')

    def delete_beacon_by_id(self, correlation_id, id):
        raise NotImplementedError('Method from interface definition')
