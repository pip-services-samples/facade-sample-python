# -*- coding: utf-8 -*-
from typing import Any, Optional

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.data import FilterParams, DataPage, PagingParams

from pip_facades_sample_python.clients.version1.ISettingsClientV1 import ISettingsClientV1


class SettingsNullClientV1(ISettingsClientV1):
    def __init__(self, config: Any = None):
        pass

    def get_section_ids(self, correlation_id: Optional[str], filter_params: FilterParams,
                        paging: PagingParams) -> DataPage:
        return DataPage([])

    def get_sections(self, correlation_id: Optional[str], filter_params: FilterParams,
                     paging: PagingParams) -> DataPage:
        return DataPage([])

    def get_section_by_id(self, correlation_id: Optional[str], id: str) -> ConfigParams:
        return ConfigParams()

    def set_section(self, correlation_id: Optional[str], id: str, parameters: ConfigParams) -> ConfigParams:
        return parameters

    def modify_section(self, correlation_id: Optional[str], id: str, update_params: ConfigParams,
                       increment_params: ConfigParams) -> ConfigParams:
        update_params = update_params or ConfigParams()
        increment_params = increment_params or ConfigParams()
        update_params = update_params.override(increment_params)
        return update_params
