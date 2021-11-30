# -*- coding: utf-8 -*-

import datetime

import bottle
from pip_services3_commons.convert import JsonConverter, TypeCode
from pip_services3_commons.refer import Descriptor, IReferences
from pip_services3_rpc.services import RestOperations

from pip_facades_sample_python.clients.version1.IInvitationsClientV1 import IInvitationsClientV1
from pip_facades_sample_python.clients.version1.InvitationV1 import InvitationV1


class InvitationsOperationsV1(RestOperations):

    def __init__(self):
        super().__init__()
        self.__invitations_client: IInvitationsClientV1 = None

        self._dependency_resolver.put('invitations', Descriptor('pip-services-invitations', 'client', '*', '*', '1.0'))

    def set_references(self, references: IReferences):
        super().set_references(references)

        self.__invitations_client = self._dependency_resolver.get_one_required('invitations')

    def get_invitations(self, site_id):
        filter_params = self._get_filter_params()
        paging = self._get_paging_params()

        filter_params.set_as_object('site_id', site_id)

        result = self.__invitations_client.get_invitations(None, filter_params, paging)
        return self._send_result(result)

    def get_invitation(self, site_id, invitation_id):
        result = self.__invitations_client.get_invitations_by_id(None, invitation_id)
        return self._send_result(result)

    def send_invitation(self, site_id):
        json_data = bottle.request.json if isinstance(bottle.request.json, dict) else JsonConverter.from_json(
            TypeCode.Map, bottle.request.json)

        invitation = InvitationV1(**json_data)
        user = {} if not hasattr(bottle.request, 'user') else bottle.request.user

        invitation.create_time = datetime.datetime.now()
        invitation.creator_id = getattr(user, 'id', None)
        invitation.creator_name = getattr(user, 'name', None)

        result = self.__invitations_client.create_invitation(None, invitation)
        return self._send_result(result)

    def delete_invitation(self, site_id, invitation_id):
        result = self.__invitations_client.delete_invitation(None, invitation_id)
        return self._send_result(result)

    def approve_invitation(self, site_id, invitation_id):
        params = dict(bottle.request.query.decode())
        role = params.get('role')

        result = self.__invitations_client.approve_invitation(None, invitation_id, role)
        return self._send_result(result)

    def deny_invitation(self, site_id, invitation_id):
        result = self.__invitations_client.deny_invitation(None, invitation_id)
        return self._send_result(result)

    def resend_invitation(self, site_id, invitation_id):
        result = self.__invitations_client.resend_invitation(None, invitation_id)
        return self._send_result(result)

    def notify_invitation(self, site_id):
        json_data = bottle.request.json if isinstance(bottle.request.json, dict) else JsonConverter.from_json(
            TypeCode.Map, bottle.request.json)

        invitation = InvitationV1(**json_data)
        user = {} if not hasattr(bottle.request, 'user') else bottle.request.user

        invitation.create_time = datetime.datetime.now()
        invitation.creator_id = getattr(user, 'id', None)
        invitation.creator_name = getattr(user, 'name', None)

        result = self.__invitations_client.notify_invitation(None, invitation)
        return self._send_empty_result(result)
