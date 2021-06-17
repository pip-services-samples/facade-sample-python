# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, List

from pip_services3_commons.data import FilterParams, PagingParams, DataPage

from pip_facades_sample_python.clients.version1.InvitationV1 import InvitationV1


class IInvitationsClientV1(ABC):
    @abstractmethod
    def get_invitations(self, correlation_id: Optional[str], filter_params: FilterParams,
                        paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_invitations_by_id(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass

    @abstractmethod
    def create_invitation(self, correlation_id: Optional[str], invitation: InvitationV1) -> InvitationV1:
        pass

    @abstractmethod
    def update_invitation(self, correlation_id: Optional[str], invitation: InvitationV1) -> InvitationV1:
        pass

    @abstractmethod
    def delete_invitation(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass

    @abstractmethod
    def delete_invitation_by_id(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass

    @abstractmethod
    def activate_invitations(self, correlation_id: Optional[str], email: str, user_id: str) -> List[InvitationV1]:
        pass

    @abstractmethod
    def approve_invitation(self, correlation_id: Optional[str], invitation_id: str, role: str) -> InvitationV1:
        pass

    @abstractmethod
    def deny_invitation(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass

    @abstractmethod
    def resend_invitation(self, correlation_id: Optional[str], invitation_id: str) -> InvitationV1:
        pass

    @abstractmethod
    def notify_invitation(self, correlation_id: Optional[str], invitation: InvitationV1):
        pass
