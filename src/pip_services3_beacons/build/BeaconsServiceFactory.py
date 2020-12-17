# -*- coding: utf-8 -*-
"""
    step8.build.BeaconsServiceFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsServiceFactory class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.refer import Descriptor
from pip_services3_components.build import Factory

from ..logic.BeaconsController import BeaconsController
from ..persistence.BeaconsFilePersistence import BeaconsFilePersistence
from ..persistence.BeaconsMemoryPersistence import BeaconsMemoryPersistence
# from ..persistence.BeaconsMongoDbPersistence import BeaconsMongoDbPersistence
from ..services.version1.BeaconsHttpServiceV1 import BeaconsHttpServiceV1

MemoryPersistenceDescriptor = Descriptor('beacons', 'persistence', 'memory', '*', '1.0')
FilePersistenceDescriptor = Descriptor('beacons', 'persistence', 'file', '*', '1.0')
# MongoDbPersistenceDescriptor = Descriptor('beacons', 'persistence', 'mongodb', '*', '1.0')
ControllerDescriptor = Descriptor('beacons', 'controller', 'default', '*', '1.0')
HttpServiceV1Descriptor = Descriptor('beacons', 'service', 'http', '*', '1.0')

class BeaconsServiceFactory(Factory):
    def __init__(self):
        super(BeaconsServiceFactory, self).__init__()

        self.register_as_type(MemoryPersistenceDescriptor, BeaconsMemoryPersistence)
        self.register_as_type(FilePersistenceDescriptor, BeaconsFilePersistence)
        # self.register_as_type(MongoDbPersistenceDescriptor, BeaconsMongoDbPersistence)
        self.register_as_type(ControllerDescriptor, BeaconsController)
        self.register_as_type(HttpServiceV1Descriptor, BeaconsHttpServiceV1)