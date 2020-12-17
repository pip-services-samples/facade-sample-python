# -*- coding: utf-8 -*-
"""
    step8.logic.BeaconsCommandSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsCommandSet class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services3_commons.commands import CommandSet, Command
from pip_services3_commons.convert import TypeCode
from pip_services3_commons.data import FilterParams, PagingParams
from pip_services3_commons.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema, ArraySchema

from ..data.version1 import BeaconV1Schema


class BeaconsCommandSet(CommandSet):
    _controller = None

    def __init__(self, controller):
        super(BeaconsCommandSet, self).__init__()
        self._controller = controller

        self.add_command(self.make_get_beacons_command())
        self.add_command(self.make_get_beacon_by_id_command())
        self.add_command(self.make_get_beacon_by_udi_command())
        self.add_command(self.make_calculate_position_command())
        self.add_command(self.make_create_beacon_command())
        self.add_command(self.make_update_beacon_command())
        self.add_command(self.make_delete_beacon_by_id_command())

    def make_get_beacons_command(self):
        def handler(correlation_id, args):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            return self._controller.get_beacons_by_filter(correlation_id, filter, paging)
        return Command("get_beacons", ObjectSchema().with_optional_property("filter", FilterParamsSchema())
                                                    .with_optional_property("paging", PagingParamsSchema()), handler)

    def make_get_beacon_by_id_command(self):
        def handler(correlation_id, args):
            id = args.get_as_string("id")
            return self._controller.get_beacon_by_id(correlation_id, id)
        return Command("get_beacon_by_id", ObjectSchema().with_required_property("id", "String"), handler)

    def make_get_beacon_by_udi_command(self):
        def handler(correlation_id, args):
            id = args.get_as_string("udi")
            return self._controller.get_beacon_by_udi(correlation_id, id)
        return Command("get_beacon_by_udi", ObjectSchema().with_required_property("udi", "String"), handler)

    def make_calculate_position_command(self):
        def handler(correlation_id, args):
            site_id = args.get_as_string("site_id")
            udis = args.get_as_nullable_string("udis")
            return self._controller.calculate_position(correlation_id, site_id, udis)
        return Command("calculate_position", ObjectSchema().with_required_property("site_id", "String")
                       .with_required_property("udis", ArraySchema("String")), handler)

    def make_create_beacon_command(self):
        def handler(correlation_id, args):
            entity = args.get("beacon")
            return self._controller.create_beacon(correlation_id, entity)
        return Command("create_beacon", ObjectSchema().with_optional_property("beacon", BeaconV1Schema()), handler)

    def make_update_beacon_command(self):
        def handler(correlation_id, args):
            entity = args.get("beacon")
            return self._controller.update_beacon(correlation_id, entity)
        return Command("update_beacon", ObjectSchema().with_optional_property("beacon", BeaconV1Schema()), handler)

    def make_delete_beacon_by_id_command(self):
        def handler(correlation_id, args):
            id = args.get_as_string("id")
            return self._controller.delete_beacon_by_id(correlation_id, id)
        return Command("delete_beacon_by_id", ObjectSchema().with_required_property("id", "String"), handler)

