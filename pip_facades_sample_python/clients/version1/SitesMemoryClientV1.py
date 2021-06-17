# -*- coding: utf-8 -*-
import datetime
from typing import List, Callable, Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage, IdGenerator

from pip_facades_sample_python.clients.version1.ISitesClientV1 import ISitesClientV1
from pip_facades_sample_python.clients.version1.SiteV1 import SiteV1


class SitesMemoryClientV1(ISitesClientV1):
    def __init__(self):
        self.__sites: List[SiteV1] = []

    def __match_string(self, value: str, search: str) -> bool:
        if value is None and search is None:
            return True
        if value is None or search is None:
            return False

        return value.lower().find(search) >= 0

    def __match_search(self, item: SiteV1, search: str) -> bool:
        search = search.lower()
        if self.__match_string(item.id, search):
            return True
        if self.__match_string(item.name, search):
            return True
        return False

    def __contains(self, array1, array2) -> bool:
        if array1 is None or array2 is None: return False

        for i1 in range(len(array1)):
            for i2 in range(len(array2)):
                if array1[i1] == array2[i2]:
                    return True

        return False

    def __compose_filter(self, filter_params: FilterParams) -> Callable:
        filter_params = filter_params or FilterParams()

        search = filter_params.get_as_nullable_string('search')
        id = filter_params.get_as_nullable_string('id')
        code = filter_params.get_as_nullable_string('code')
        active = filter_params.get_as_nullable_boolean('active')
        deleted = filter_params.get_as_boolean_with_default('deleted', False)

        def inner(item):
            if id and item.id != id:
                return False
            if code and item.code != code:
                return False
            if active and item.active != active:
                return False
            if not deleted and item.deleted:
                return False
            if search and not self.__match_search(item, search):
                return False

            return True

        return inner

    def get_sites(self, correlation_id: Optional[str], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        sites = list(filter(self.__compose_filter(filter_params), self.__sites))
        return DataPage(sites, len(sites))

    def get_site_by_id(self, correlation_id: Optional[str], site_id: str) -> SiteV1:
        site = list(filter(lambda x: x.id == site_id, self.__sites))[0]
        return site

    def get_site_by_code(self, correlation_id: Optional[str], code: str) -> SiteV1:
        filtered = list(filter(lambda x: x.code == code, self.__sites))
        site = None if len(filtered) <=0 else filtered[0]
        return site

    def generate_code(self, correlation_id: Optional[str], site_id: str) -> str:
        return site_id

    def create_site(self, correlation_id: Optional[str], site: SiteV1) -> SiteV1:
        site.id = site.id or IdGenerator.next_long()
        site.create_time = datetime.datetime.now()
        site.active = site.active is not None or True

        self.__sites.append(site)

        return site

    def update_site(self, correlation_id: Optional[str], site: SiteV1) -> SiteV1:
        self.__sites = list(filter(lambda x: x.id != site.id, self.__sites))
        self.__sites.append(site)

        return site

    def delete_site_by_id(self, correlation_id: Optional[str], site_id: str) -> SiteV1:
        filtered = list(filter(lambda x: x.id == site_id, self.__sites))
        site = None if len(filtered) <= 0 else filtered[0]
        if site:
            site.deleted = True

        return site
