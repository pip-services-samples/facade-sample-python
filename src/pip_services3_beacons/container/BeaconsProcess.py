# -*- coding: utf-8 -*-
"""
    step8.container.BeaconsProcess
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsProcess class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
import sys

from pip_services3_container import ProcessContainer
from pip_services3_rpc.build import DefaultRpcFactory

from ..build.BeaconsServiceFactory import BeaconsServiceFactory


class BeaconsProcess(ProcessContainer):
    def __init__(self):
        super(BeaconsProcess, self).__init__('beacons', 'Beacons microservice')

        self._factories.add(BeaconsServiceFactory())
        self._factories.add(DefaultRpcFactory())

