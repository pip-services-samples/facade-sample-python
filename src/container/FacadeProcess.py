# -*- coding: utf-8 -*-
from pip_services3_container import ProcessContainer
from pip_services3_rpc.build.DefaultRpcFactory import DefaultRpcFactory

from ..build.ClientFacadeFactory import ClientFacadeFactory
from ..build.FacadeFactory import FacadeFactory
from ..build.ServiceFacadeFactory import ServiceFacadeFactory

# from pip_services3_mongodb.build.DefaultMongoDbFactory import DefaultMongoDbFactory


class FacadeProcess(ProcessContainer):

    def __init__(self):
        super(FacadeProcess, self).__init__("pip-facades-example", "Example Pip.Services facade")

        self._factories.add(ClientFacadeFactory())
        self._factories.add(ServiceFacadeFactory())
        self._factories.add(FacadeFactory())
        self._factories.add(DefaultRpcFactory())
        # self._factories.add(DefaultMongoDbFactory())
