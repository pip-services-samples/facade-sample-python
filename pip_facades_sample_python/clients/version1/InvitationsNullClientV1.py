# -*- coding: utf-8 -*-

from typing import Optional, List

from pip_services3_commons.data import FilterParams, PagingParams, DataPage

from pip_facades_sample_python.clients.version1.IInvitationsClientV1 import IInvitationsClientV1
from pip_facades_sample_python.clients.version1.InvitationV1 import InvitationV1


class InvitationsNullClientV1(IInvitationsClientV1):
    def get_invitations(self, correlation_id: Optional[str], filter_params: FilterParams,
                        paging: PagingParams) -> DataPage:
        return DataPage([], 0)

    def get_invitations_by_id(self, correlation_id: Optional[str], invitation_id: str) -> Optional[InvitationV1]:
        return None

    def create_invitation(self, correlation_id: Optional[str], invitation: InvitationV1) -> InvitationV1:
        return invitation

    def update_invitation(self, correlation_id: Optional[str], invitation: InvitationV1) -> InvitationV1:
        return invitation

    def delete_invitation(self, correlation_id: Optional[str], invitation_id: str) -> Optional[InvitationV1]:
        return None

    def activate_invitations(self, correlation_id: Optional[str], email: str, user_id: str) -> List[InvitationV1]:
        return []

    def approve_invitation(self, correlation_id: Optional[str], invitation_id: str, role: str) -> Optional[InvitationV1]:
        return None

    def deny_invitation(self, correlation_id: Optional[str], invitation_id: str) -> Optional[InvitationV1]:
        return None

    def resend_invitation(self, correlation_id: Optional[str], invitation_id: str) -> Optional[InvitationV1]:
        return None

    def notify_invitation(self, correlation_id: Optional[str], invitation: InvitationV1):
        return

    def delete_invitation_by_id(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass
