# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, List, Any

from pip_services3_commons.data import DataPage, PagingParams, FilterParams

from pip_facades_sample_python.clients.version1.BeaconV1 import BeaconV1


class IBeaconsClientV1(ABC):

    @abstractmethod
    def get_beacons(self, correlation_id: Optional[str], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_beacon_by_id(self, correlation_id: Optional[str], beacon_id: str) -> BeaconV1:
        pass

    @abstractmethod
    def get_beacon_by_udi(self, correlation_id: Optional[str], udi: str) -> BeaconV1:
        pass

    @abstractmethod
    def calculate_position(self, correlation_id: Optional[str], site_id: str, udis: List[str]) -> Any:
        pass

    @abstractmethod
    def create_beacon(self, correlation_id: Optional[str], beacon: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def update_beacon(self, correlation_id: Optional[str], beacon: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def delete_beacon_by_id(self, correlation_id: Optional[str], id: str) -> BeaconV1:
        pass
