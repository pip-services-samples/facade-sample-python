# -*- coding: utf-8 -*-

from pip_services3_commons.config.ConfigParams import ConfigParams
from pip_services3_commons.refer.Descriptor import Descriptor
from pip_services3_components.build.CompositeFactory import CompositeFactory
from pip_services3_container.refer.ManagedReferences import ManagedReferences
# from pip_services3_mongodb.build.DefaultMongoDbFactory import DefaultMongoDbFactory
from pip_services3_rpc.build.DefaultRpcFactory import DefaultRpcFactory

from pip_facades_sample_python.build.ClientFacadeFactory import ClientFacadeFactory
from pip_facades_sample_python.build.FacadeFactory import FacadeFactory
from pip_facades_sample_python.build.ServiceFacadeFactory import ServiceFacadeFactory
from pip_beacons_sample_python.clients.version1.BeaconsDirectClientV1 import BeaconsDirectClientV1
from pip_beacons_sample_python.logic import BeaconsController
from pip_beacons_sample_python.persistence.BeaconsFilePersistence import BeaconsFilePersistence
from pip_facades_sample_python.services.version1.FacadeServiceV1 import FacadeServiceV1


class ReferencesTest(ManagedReferences):
    _factory = CompositeFactory()

    def __init__(self):
        super(ReferencesTest, self).__init__()

        self._setup_factoriest()
        self._append_dependencies()
        self._configure_service()
        self._create_user_and_sessions()

    def _setup_factoriest(self):
        self._factory.add(ClientFacadeFactory())
        self._factory.add(ServiceFacadeFactory())
        self._factory.add(DefaultRpcFactory())

    def append(self, descriptor):
        component = self._factory.create(descriptor)
        self.put(descriptor, component)

    def _append_dependencies(self):
        # Add factories
        self.put(None, self._factory)

        # Add service

        # TODO: check this
        facade_service = FacadeServiceV1()
        facade_service.configure(ConfigParams.from_tuples(
            'root_path', '',  # '/api/1.0',
            'connection.protocol', 'http',
            'connection.host', 'localhost',
            'connection.port', 3000
        ))
        self.put(None, facade_service)

        # Add services
        self.put(Descriptor('beacons', 'client', 'direct', '*', '1.0'), BeaconsDirectClientV1())
        self.put(Descriptor('beacons', 'persistence', 'file', 'default', '1.0'),
                 BeaconsFilePersistence('./data/beacons.test.json'))
        self.put(Descriptor('beacons', 'controller', 'default', 'default', '1.0'), BeaconsController())

    def _configure_service(self):
        # Configure Facade service
        service = self.get_one_required(Descriptor('pip-services', 'endpoint', 'http', 'default', '*'))

        service.configure(ConfigParams.from_tuples(
            'root_path', '',  # '/api/1.0',
            'connection.protocol', 'http',
            'connection.host', 'localhost',
            'connection.port', 3000
        ))

    def _create_user_and_sessions(self):
        # TODO need add
        pass
