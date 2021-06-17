# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Optional

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.data import FilterParams, PagingParams, DataPage


class ISettingsClientV1(ABC):
    @abstractmethod
    def get_section_ids(self, correlation_id: Optional[str], filter_params: FilterParams,
                        paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_sections(self, correlation_id: Optional[str], filter_params: FilterParams,
                     paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_section_by_id(self, correlation_id: Optional[str], id: str) -> ConfigParams:
        pass

    @abstractmethod
    def set_section(self, correlation_id: Optional[str], id: str, parameters: ConfigParams) -> ConfigParams:
        pass

    @abstractmethod
    def modify_section(self, correlation_id: Optional[str], id: str, update_params: ConfigParams,
                       increment_params: ConfigParams) -> ConfigParams:
        pass
