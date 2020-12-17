# -*- coding: utf-8 -*-
"""
    step8.services.BeaconsHttpServiceV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsHttpServiceV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.refer import Descriptor
from pip_services3_rpc.services import CommandableHttpService

class BeaconsHttpServiceV1(CommandableHttpService):
    def __init__(self):
        super(BeaconsHttpServiceV1, self).__init__("v1/beacons")
        self._dependency_resolver.put("controller", Descriptor('beacons', 'controller', '*', '*', '1.0'))