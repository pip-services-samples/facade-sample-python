# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage

from pip_facades_sample_python.clients.version1.SiteV1 import SiteV1


class ISitesClientV1(ABC):
    @abstractmethod
    def get_sites(self, correlation_id: Optional[str], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_site_by_id(self, correlation_id: Optional[str], site_id: str) -> SiteV1:
        pass

    @abstractmethod
    def get_site_by_code(self, correlation_id: Optional[str], code: str) -> SiteV1:
        pass

    @abstractmethod
    def generate_code(self, correlation_id: Optional[str], site_id: str) -> str:
        pass

    @abstractmethod
    def create_site(self, correlation_id: Optional[str], site: SiteV1) -> SiteV1:
        pass

    @abstractmethod
    def update_site(self, correlation_id: Optional[str], site: SiteV1) -> SiteV1:
        pass

    @abstractmethod
    def delete_site_by_id(self, correlation_id: Optional[str], site_id: str) -> SiteV1:
        pass
