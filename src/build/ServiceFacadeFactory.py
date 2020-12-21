# -*- coding: utf-8 -*-

from pip_services3_components.build.CompositeFactory import CompositeFactory

from pip_beacons_sample_python.build.BeaconsServiceFactory import BeaconsServiceFactory


class ServiceFacadeFactory(CompositeFactory):

    def __init__(self):
        super(ServiceFacadeFactory, self).__init__()

        self.add(BeaconsServiceFactory())
