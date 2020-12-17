# -*- coding: utf-8 -*-

from pip_services3_components.build.Factory import Factory
from pip_services3_commons.refer.Descriptor import Descriptor

from ..clients.version1.BeaconsDirectClientV1 import BeaconsDirectClientV1
from ..clients.version1.BeaconsHttpClientV1 import BeaconsHttpClientV1
from ..clients.version1.BeaconsNullClientV1 import BeaconsNullClientV1


class BeaconsClientFactory(Factory):
    null_client_descriptor = Descriptor('beacons', 'client', 'null', '*', '1.0')
    direct_client_descriptor = Descriptor('beacons', 'client', 'direct', '*', '1.0')
    http_client_descriptor = Descriptor('beacons', 'client', 'http', '*', '1.0')

    def __init__(self):
        super(BeaconsClientFactory, self).__init__()

        self.register_as_type(BeaconsClientFactory.null_client_descriptor, BeaconsNullClientV1)
        self.register_as_type(BeaconsClientFactory.http_client_descriptor, BeaconsHttpClientV1)
        self.register_as_type(BeaconsClientFactory.direct_client_descriptor, BeaconsDirectClientV1)
