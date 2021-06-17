# -*- coding: utf-8 -*-

from typing import List, Callable, Optional, Any

from pip_services3_commons.data import FilterParams, PagingParams, DataPage, IdGenerator

from pip_facades_sample_python.clients.version1.BeaconV1 import BeaconV1
from pip_facades_sample_python.clients.version1.IBeaconsClientV1 import IBeaconsClientV1


class BeaconsMemoryClientV1(IBeaconsClientV1):
    def __init__(self):
        self.__beacons: List[BeaconV1] = []

    def __compose_filter(self, filter_params: FilterParams) -> Callable:
        filter_params = filter_params or FilterParams()

        id = filter_params.get_as_nullable_string('id')
        site_id = filter_params.get_as_nullable_string('site_id')
        label = filter_params.get_as_nullable_string('label')
        udi = filter_params.get_as_nullable_string('udi')
        udis = filter_params.get_as_object('udis')
        if isinstance(udis, str):
            udis = udis.split(',')
        if not isinstance(udis, list):
            udis = None

        def inner(item):
            if id is not None and item.id != id:
                return False
            if site_id is not None and item.site_id != site_id:
                return False
            if label is not None and item.label != label:
                return False
            if udi is not None and item.udi != udi:
                return False
            if udis is not None and udis.count(item.udi) < 0:
                return False
            return True

        return inner

    def get_beacons(self, correlation_id: Optional[str], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        beacons = list(filter(self.__compose_filter(filter_params), self.__beacons))

        return DataPage(beacons, len(beacons))

    def get_beacon_by_id(self, correlation_id: Optional[str], beacon_id: str) -> BeaconV1:
        filtered = list(filter(lambda x: x.id == id, self.__beacons))
        beacon = None if len(filtered) <= 0 else filtered[0]

        return beacon

    def get_beacon_by_udi(self, correlation_id: Optional[str], udi: str) -> BeaconV1:
        filtered = list(filter(lambda x: x.udi == udi, self.__beacons))
        beacon = None if len(filtered) <= 0 else filtered[0]

        return beacon

    def calculate_position(self, correlation_id: Optional[str], site_id: str, udis: List[str]) -> Any:
        beacons: List[BeaconV1] = []
        position = None

        if udis is None or len(udis) == 0:
            return

        page = self.get_beacons(correlation_id,
                                  FilterParams.from_tuples(
                                      'site_id', site_id,
                                      'udis', udis
                                  ), PagingParams())

        beacons = page.data or []

        lat = 0
        lng = 0
        count = 0

        for beacon in beacons:
            if beacon.center is not None and beacon.center['type'] == 'Point' and isinstance(
                    beacon.center['coordinates'], list):
                lng += beacon.center['coordinates'][0]
                lat += beacon.center['coordinates'][1]
                count += 1

        if count > 0:
            position = {
                'type': 'Point',
                'coordinates': [lng / count, lat / count]
            }

        return position or None

    def create_beacon(self, correlation_id: Optional[str], beacon: BeaconV1) -> BeaconV1:
        beacon.id = beacon.id or IdGenerator.next_long()
        beacon.type = beacon.type or 'unknown'

        self.__beacons.append(beacon)

        return beacon

    def update_beacon(self, correlation_id: Optional[str], beacon: BeaconV1) -> BeaconV1:
        beacon.type = beacon.type or 'unknown'

        self.__beacons = list(filter(lambda x: x.id != beacon.id, self.__beacons))
        self.__beacons.append(beacon)

        return beacon

    def delete_beacon_by_id(self, correlation_id: Optional[str], id: str) -> BeaconV1:
        filtered = list(filter(lambda x: x.id == id, self.__beacons))
        beacon = None if len(filtered) <= 0 else filtered[0]
        if beacon:
            self.__beacons = list(filter(lambda x: x.id != beacon.id, self.__beacons))

        return beacon
