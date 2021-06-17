# -*- coding: utf-8 -*-
import datetime

from pip_services3_commons.convert import JsonConverter, TypeCode
from pip_services3_commons.refer import Descriptor

from pip_facades_sample_python.clients.version1.InvitationV1 import InvitationV1
from pip_facades_sample_python.operations.version1.InvitationsOperationsV1 import InvitationsOperationsV1
from test.fixtures.ReferencesTest import ReferencesTest
from test.fixtures.RestClientTest import RestClientTest
from test.fixtures.TestUsers import TestUsers

INVITATION1: InvitationV1 = InvitationV1(
    id='1',
    action='activate',
    site_id='1',
    role='manager',
    create_time=datetime.datetime.now(),
    creator_id='1',
    invitee_email='test@somewhere.com'
)

INVITATION2: InvitationV1 = InvitationV1(
    id='2',
    action='activate',
    site_id='1',
    create_time=datetime.datetime.now(),
    creator_id='1',
    invitee_email='test2@somewhere.com'
)

INVITATION3: InvitationV1 = InvitationV1(
    id='3',
    action='notify',
    site_id='1',
    create_time=datetime.datetime.now(),
    creator_id='1',
    invitee_email='test2@somewhere.com'
)


class TestInvitationsOperationsV1:
    references: ReferencesTest = None
    rest: RestClientTest = None

    def setup_method(self):
        self.rest = RestClientTest()
        self.references = ReferencesTest()
        self.references.put(Descriptor('iqs-services-facade', 'operations', 'invitations', 'default', '1.0'),
                            InvitationsOperationsV1())
        self.references.open(None)

    def teardown_method(self):
        self.references.close(None)

    def test_should_resend_invitations(self):
        invitation1: InvitationV1 = None

        # Send invitation
        response = self.rest.post_as_user(TestUsers.AdminUserSessionId,
                                          '/api/v1/sites/' + INVITATION1.site_id + '/invitations',
                                          JsonConverter.to_json(INVITATION1))

        invitation = JsonConverter.from_json(TypeCode.Map, response.content)
        assert invitation['site_id'] == INVITATION1.site_id
        assert invitation['invitee_email'] == INVITATION1.invitee_email

        invitation1 = InvitationV1(**invitation)

        # Send another invitation
        response = self.rest.post_as_user(TestUsers.AdminUserSessionId,
                                          '/api/v1/sites/' + invitation1.site_id + '/invitations/' + invitation1.id + '/resend',
                                          {})

        assert response.status_code < 300
        # assert invitation['id'] == invitation1.id

    def test_should_perform_invitation_operations(self):
        invitation1: InvitationV1 = None
        invitation2: InvitationV1 = None

        # Send one invitation
        response = self.rest.post_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites/' + INVITATION1.site_id + '/invitations',
            JsonConverter.to_json(INVITATION1)
        )
        invitation = JsonConverter.from_json(TypeCode.Map, response.content)

        assert invitation['site_id'] == INVITATION1.site_id
        assert invitation['creator_id'] == INVITATION1.creator_id
        assert invitation['invitee_email'] == INVITATION1.invitee_email

        invitation1 = InvitationV1(**invitation)

        # Send another invitation
        response = self.rest.post_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites/' + INVITATION2.site_id + '/invitations',
            JsonConverter.to_json(INVITATION2),
        )

        invitation = JsonConverter.from_json(TypeCode.Map, response.content)

        assert invitation['site_id'] == INVITATION2.site_id
        assert invitation['creator_id'] == INVITATION2.creator_id
        assert invitation['invitee_email'] == INVITATION2.invitee_email

        invitation2 = InvitationV1(**invitation)

        # Get all invitations
        response = self.rest.get_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites/' + INVITATION1.site_id + '/invitations'
        )

        page = JsonConverter.from_json(TypeCode.Map, response.content)

        assert response.status_code == 200
        assert page is not None and page != {}
        # assert len(page['data']) == 2

        # Delete invitation
        response = self.rest.delete_as_user(TestUsers.AdminUserSessionId,
                    '/api/v1/sites/' + invitation1.site_id + '/invitations/' + invitation1.id)

        assert response.status_code < 300

        # Try to get delete invitation
        response = self.rest.get_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites/' + invitation1.site_id + '/invitations/' + invitation1.id,
        )

        assert response.status_code < 300
        assert response.content == b''

    def test_should_notify_invitations(self):
        response = self.rest.post_as_user(
            TestUsers.AdminUserSessionId,
            '/api/v1/sites/' + INVITATION1.site_id + '/invitations/notify',
            JsonConverter.to_json(INVITATION3),
        )

        assert response.status_code < 300
        assert response.content == b''

