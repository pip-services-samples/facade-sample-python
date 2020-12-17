# -*- coding: utf-8 -*-

from pip_services3_components.build.CompositeFactory import CompositeFactory

from src.pip_services3_beacons.build.BeaconsServiceFactory import BeaconsServiceFactory


class ServiceFacadeFactory(CompositeFactory):

    def __init__(self):
        super(ServiceFacadeFactory, self).__init__()

        self.add(BeaconsServiceFactory())
