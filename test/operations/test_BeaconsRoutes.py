# -*- coding: utf-8 -*-
from pip_services3_commons.run import Parameters

from pip_beacons_sample_python.data.version1 import BeaconV1, BeaconTypeV1

from pip_services3_facade

from test.fixtures.ReferencesTest import ReferencesTest
from test.fixtures.RestClientTest import RestClientTest

import json

BEACON1 = BeaconV1("1", "1", BeaconTypeV1.AltBeacon, "00001", "TestBeacon1",
                   {"type": 'Point', "coordinates": [0, 0]}, 50)

BEACON2 = BeaconV1("2", "1", BeaconTypeV1.iBeacon, "00002", "TestBeacon2",
                   {"type": 'Point', "coordinates": [2, 2]}, 70)

BEACON3 = BeaconV1("3", "2", BeaconTypeV1.AltBeacon, "00003", "TestBeacon3",
                   {"type": 'Point', "coordinates": [10, 10]}, 50)


class TestBeaconsOperationsV1:
    references = None
    rest = None

    @staticmethod
    def _clear_file_persistence():
        with open('./data/beacons.test.json', 'w') as f:
            f.write('[]')

    @classmethod
    def setup_class(cls):
        cls._clear_file_persistence()
        cls.rest = RestClientTest()
        cls.references = ReferencesTest()
        cls.references.open(None)

    @classmethod
    def teardown_class(cls):
        cls._clear_file_persistence()
        cls.references.close(None)

    def test_beacons_operations(self):
        # Create one beacon
        response = self.rest.post('/api/1.0/beacons', Parameters.from_value(BEACON1))
        assert response.reason == 'Created'

        created_beacon = json.loads(response.content)
        assert BEACON1['udi'] == created_beacon['udi']
        assert BEACON1['id'] == created_beacon['id']
        assert BEACON1['site_id'] == created_beacon['site_id']
        assert BEACON1['type'] == created_beacon['type']
        assert created_beacon['center'] is not None

        # Create the second beacon
        response = self.rest.post('/api/1.0/beacons', Parameters.from_value(BEACON2))
        assert response.reason == 'Created'

        created_beacon = json.loads(response.content)
        assert BEACON2['udi'] == created_beacon['udi']
        assert BEACON2['id'] == created_beacon['id']
        assert BEACON2['site_id'] == created_beacon['site_id']
        assert BEACON2['type'] == created_beacon['type']
        assert created_beacon['center'] is not None

        # Get all beacons
        response = self.rest.get('/api/1.0/beacons')
        beacons = json.loads(response.content)
        assert len(beacons['data']) == 2

        # Update the beacon
        BEACON1['label'] = 'ABC'
        response = self.rest.put('/api/1.0/beacons', Parameters.from_value(BEACON1))
        assert response.reason == 'OK'
        updated_beacon = json.loads(response.content)
        assert BEACON1['id'] == updated_beacon['id']
        assert updated_beacon['label'] == 'ABC'

        # Get beacon by udi
        response = self.rest.get(f"/api/1.0/beacons/{BEACON1['udi']}")
        assert response.reason == 'OK'
        beacon_udi = json.loads(response.content)['udi']
        assert BEACON1['udi'] == beacon_udi

        # Calculate position for one beacon
        response = self.rest.post('/api/1.0/beacons/calculate_position',
                                  Parameters.from_tuples("site_id", '1', "udis", ['00001']))
        assert response.reason == 'OK'
        calc_position = json.loads(response.content)
        assert calc_position['type'] == 'Point'
        assert len(calc_position['coordinates']) == 2
        assert calc_position['coordinates'][0] == 0
        assert calc_position['coordinates'][1] == 0

        # Delete the beacon
        response = self.rest.delete(f"/api/1.0/beacons/{BEACON1['id']}")
        deleted_result = json.loads(response.content)
        assert deleted_result['id'] == BEACON1['id']

        # Try to get deleted beacon
        response = self.rest.get(f"/api/1.0/beacons/{BEACON1['id']}")
        assert response.reason == 'Not Found'

