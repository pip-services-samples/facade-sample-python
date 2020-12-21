# -*- coding: utf-8 -*-

from pip_services3_rpc.services.RestService import RestService
from pip_services3_rpc.services.AboutOperations import AboutOperations

from pip_facades_sample_python.operations.version1.BeaconsOperations import BeaconsOperations


class FacadeServiceV1(RestService):
    _about_operations = AboutOperations()
    _beacons_operations = BeaconsOperations()

    def __init__(self):
        super(FacadeServiceV1, self).__init__()
        self._base_route = 'api/1.0'

    def configure(self, config):
        super().configure(config)

        self._about_operations.configure(config)
        self._beacons_operations.configure(config)

    def set_references(self, references):
        super().set_references(references)

        self._about_operations.set_references(references)
        self._beacons_operations.set_references(references)

    def register(self):
        self.register_beacons_routes()

    def register_beacons_routes(self):
        self.register_interceptor('/beacons', self._beacons_operations.increment_number_of_calls)
        self.register_route('get', '/beacons/calls', None, self._beacons_operations.get_number_of_calls)
        self.register_route('get', '/beacons', None, self._beacons_operations.get_page_by_filter)
        self.register_route('get', '/beacons/<id>', None, self._beacons_operations.get_one_by_id)
        self.register_route('get', '/beacons/<udi>', None, self._beacons_operations.get_one_by_udi)
        self.register_route('get', '/beacons/handled_error', None, self._beacons_operations.handled_error)
        self.register_route('get', '/beacons/unhandled_error', None, self._beacons_operations.unhandled_error)
        self.register_route('delete', '/beacons/<id>', None, self._beacons_operations.delete_by_id)
        self.register_route('post', '/beacons/calculate_position', None, self._beacons_operations.calculate_position)
        self.register_route('post', '/beacons', None, self._beacons_operations.create)
        self.register_route('post', '/about', None, self._about_operations.get_about)
        self.register_route('put', '/beacons', None, self._beacons_operations.update)
        self.register_route('delete', '/beacons/<id>', None, self._beacons_operations.delete_by_id)
