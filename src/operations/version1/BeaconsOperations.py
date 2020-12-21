# -*- coding: utf-8 -*-
from pip_services3_commons.data import FilterParams
from pip_services3_commons.refer import Descriptor
from pip_services3_rpc.services import RestOperations

from pip_beacons_sample_python.clients import BeaconsHttpClientV1


class BeaconsOperations(RestOperations):
    _beacons_client: BeaconsHttpClientV1
    _number_of_calls = 0

    def __init__(self):
        super(BeaconsOperations, self).__init__()
        self._dependency_resolver.put('beacons',
                                      Descriptor('beacons', 'client', '*', '*', '1.0'))

    def get_number_of_calls(self):
        return self._number_of_calls

    def increment_number_of_calls(self, req=None, res=None):
        self._number_of_calls += 1

    def set_references(self, references):
        super().set_references(references)
        self._beacons_client = self._dependency_resolver.get_one_required('beacons')

    def get_page_by_filter(self):
        correlation_id = self._get_correlation_id()
        filters = self._get_filter_params()
        paging = self._get_paging_params()
        return self._send_result(self._beacons_client.get_beacons_by_filter(correlation_id, filters, paging))

    def get_one_by_id(self, id):
        correlation_id = self._get_correlation_id()
        return self._send_result(self._beacons_client.get_beacon_by_id(correlation_id, id))

    def get_one_by_udi(self, udi):
        correlation_id = self._get_correlation_id()
        return self._send_result(self._beacons_client.get_beacon_by_udi(correlation_id, udi))

    def create(self):
        correlation_id = self._get_correlation_id()
        entity = self._get_data()
        return self._send_created_result(self._beacons_client.create_beacon(correlation_id, entity))

    def update(self):
        correlation_id = self._get_correlation_id()
        entity = self._get_data()
        return self._send_result(self._beacons_client.update_beacon(correlation_id, entity))

    def delete_by_id(self, id):
        correlation_id = self._get_correlation_id()
        result = self._beacons_client.delete_beacon_by_id(correlation_id, id)
        return self._send_deleted_result(result)

    def calculate_position(self):
        data = self._get_data()
        udis, site_id = data['udis'], data['site_id']

        if udis is None or len(udis) == 0:
            return self._send_bad_request(None, 'udis is empty')

        return self._send_result(self._beacons_client.calculate_position(None, site_id, udis))

    def handled_error(self):
        raise Exception('NotSupported', 'Test handled error')

    def unhandled_error(self):
        raise TypeError('Test unhandled error')
