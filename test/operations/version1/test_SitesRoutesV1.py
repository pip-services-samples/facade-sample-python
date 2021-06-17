# -*- coding: utf-8 -*-
import datetime

from pip_services3_commons.convert import JsonConverter, TypeCode
from pip_services3_commons.refer import Descriptor

from pip_facades_sample_python.clients.version1.SiteV1 import SiteV1
from pip_facades_sample_python.operations.version1.SitesOperationsV1 import SitesOperationsV1
from test.fixtures.ReferencesTest import ReferencesTest
from test.fixtures.RestClientTest import RestClientTest
from test.fixtures.TestUsers import TestUsers

SITE1: SiteV1 = SiteV1(
    id='2',
    code='111',
    name='Site #1',
    description='Test site #1',
    create_time=datetime.datetime.now(),
    creator_id='123',
    active=True
)

SITE2: SiteV1 = SiteV1(
    id='3',
    code='222',
    name='Site #2',
    description='Test site #2',
    create_time=datetime.datetime.now(),
    creator_id='123',
    active=True
)


class TestSitesOperationsV1:
    references: ReferencesTest = None
    rest: RestClientTest = None

    def setup_method(self):
        self.rest = RestClientTest()
        self.references = ReferencesTest()
        self.references.put(Descriptor('iqs-services-facade', 'operations', 'sites', 'default', '1.0'),
                            SitesOperationsV1())
        self.references.open(None)

    def teardown_method(self):
        self.references.close(None)

    def test_should_perform_site_operations(self):
        site1: SiteV1 = SiteV1()
        site2: SiteV1 = SiteV1()

        # Create one site
        response = self.rest.post_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites',
            JsonConverter.to_json(SITE1)
        )
        site = JsonConverter.from_json(TypeCode.Map, response.content)

        assert site['name'] == SITE1.name
        assert site['description'] == SITE1.description

        site1 = SiteV1(**site)

        # Create another site
        response = self.rest.post_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites',
            JsonConverter.to_json(SITE2)
        )

        site = JsonConverter.from_json(TypeCode.Map, response.content)

        assert site['name'] == SITE2.name
        assert site['description'] == SITE2.description

        site2 = SiteV1(**site)

        # Get all sites
        response = self.rest.get_as_user(TestUsers.AdminUserSessionId,
                                         '/api/v1/sites')
        page = JsonConverter.from_json(TypeCode.Map, response.content)

        # Account for 1 test site
        assert len(page['data'])

        # Find site by code
        response = self.rest.get('/api/v1/sites/find_by_code?code=' + site1.code)
        site = JsonConverter.from_json(TypeCode.Map, response.content)

        assert site['id'] == site1.id

        # Validate site code
        response = self.rest.post_as_user(TestUsers.AdminUserSessionId,
                                          '/api/v1/sites/validate_code?code=' + site1.code,
                                          {}, )

        assert response.content.decode('utf-8').replace('"', '') == site1.id

        # Generate code
        response = self.rest.post_as_user(TestUsers.AdminUserSessionId,
                                          '/api/v1/sites/' + site1.id + '/generate_code',
                                          {}, )

        assert JsonConverter.from_json(TypeCode.Map, response.content) is not None

        # Update the site
        site1.description = 'Updated Content 1'
        site1.center = {'type': 'Point', 'coordinates': [32, -110]}
        site1.radius = 5

        response = self.rest.put_as_user(TestUsers.AdminUserSessionId,
                                         '/api/v1/sites/' + site1.id,
                                         JsonConverter.to_json(site1))
        site = JsonConverter.from_json(TypeCode.Map, response.content)

        assert site['description'] == 'Updated Content 1'
        assert site['name'] == site1.name
        assert site['radius'] == 5
        assert site['center'] == {'type': 'Point', 'coordinates': [32, -110]}

        # Delete site
        response = self.rest.delete_as_user(TestUsers.AdminUserSessionId,
                                            '/api/v1/sites/' + site1.id, )
        site = JsonConverter.from_json(TypeCode.Map, response.content)
        assert site['deleted'] is True

        # Try to get delete site
        response = self.rest.get_as_user(TestUsers.AdminUserSessionId,
                                         '/api/v1/sites/' + site1.id)

        site = JsonConverter.from_json(TypeCode.Map, response.content)

        assert site['deleted'] is True
