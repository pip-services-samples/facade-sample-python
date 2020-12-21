# -*- coding: utf-8 -*-

from pip_services3_components.build.CompositeFactory import CompositeFactory

from pip_beacons_sample_python.build.BeaconsClientFactory import BeaconsClientFactory


class ClientFacadeFactory(CompositeFactory):

    def __init__(self):
        super(ClientFacadeFactory, self).__init__()

        self.add(BeaconsClientFactory())
