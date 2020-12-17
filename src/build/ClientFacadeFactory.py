# -*- coding: utf-8 -*-

from pip_services3_components.build.CompositeFactory import CompositeFactory

from src.pip_services3_beacons.build.BeaconsClientFactory import BeaconsClientFactory


class ClientFacadeFactory(CompositeFactory):

    def __init__(self):
        super(ClientFacadeFactory, self).__init__()

        self.add(BeaconsClientFactory())
