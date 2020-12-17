# -*- coding: utf-8 -*-

from .IBeaconsClientV1 import IBeaconsClientV1


class BeaconsNullClientV1(IBeaconsClientV1):

    def get_beacons_by_filter(self, correlation_id, filter, paging):
        pass

    def get_beacon_by_id(self, correlation_id, id):
        pass

    def get_beacon_by_udi(self, correlation_id, udi):
        pass

    def calculate_position(self, correlation_id, site_id, udis):
        pass

    def create_beacon(self, correlation_id, entity):
        pass

    def update_beacon(self, correlation_id, entity):
        pass

    def delete_beacon_by_id(self, correlation_id, id):
        pass
