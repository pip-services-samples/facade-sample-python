# -*- coding: utf-8 -*-
"""
    step8.clients.BeaconsHttpClientV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsHttpClientV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services3_commons.data import DataPage
from pip_services3_rpc.clients import CommandableHttpClient

from .IBeaconsClientV1 import IBeaconsClientV1


class BeaconsHttpClientV1(CommandableHttpClient, IBeaconsClientV1):
    def __init__(self):
        super(BeaconsHttpClientV1, self).__init__("v1/beacons")

    def get_beacons_by_filter(self, correlation_id, filter, paging):
        result = self.call_command(
            'get_beacons',
            correlation_id,
            {
                'filter': filter,
                'paging': paging
            }
        )
        return DataPage(result['data'], result['total'])

    def get_beacon_by_id(self, correlation_id, id):
        return self.call_command(
            'get_beacon_by_id',
            correlation_id,
            {
                'id': id
            }
        )

    def get_beacon_by_udi(self, correlation_id, udi):
        return self.call_command(
            'get_beacon_by_udi',
            correlation_id,
            {
                'udi': udi
            }
        )

    def calculate_position(self, correlation_id, site_id, udis):
        return self.call_command(
            'calculate_position',
            correlation_id,
            {
                'site_id': site_id,
                'udis': udis
            }
        )

    def create_beacon(self, correlation_id, entity):
        return self.call_command(
            'create_beacon',
            correlation_id,
            {
                'beacon': entity
            }
        )

    def update_beacon(self, correlation_id, entity):
        return self.call_command(
            'update_beacon',
            correlation_id,
            {
                'beacon': entity
            }
        )

    def delete_beacon_by_id(self, correlation_id, id):
        return self.call_command(
            'delete_beacon_by_id',
            correlation_id,
            {
                'id': id
            }
        )

