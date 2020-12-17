# -*- coding: utf-8 -*-

from pip_services3_components.build.Factory import Factory
from pip_services3_commons.refer.Descriptor import Descriptor

from src.services.version1.FacadeServiceV1 import FacadeServiceV1


class FacadeFactory(Factory):
    facade_service_v1_descriptor = Descriptor("pip-services-facade", "service", "http", "*", "1.0")

    def __init__(self):
        super(FacadeFactory, self).__init__()
        self.register_as_type(FacadeFactory.facade_service_v1_descriptor, FacadeServiceV1)
