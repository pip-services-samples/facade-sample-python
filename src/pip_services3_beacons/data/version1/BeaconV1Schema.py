# -*- coding: utf-8 -*-
"""
    step8.data.version1.BeaconV1Schema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconV1Schema class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services3_commons.validate.ObjectSchema import ObjectSchema
from pip_services3_commons.convert.TypeCode import TypeCode

class BeaconV1Schema(ObjectSchema):
    def __init__(self):
        super(ObjectSchema, self).__init__()
        self.with_optional_property("id", "String")
        self.with_required_property("site_id", "String")
        self.with_optional_property("type", "String")
        self.with_required_property("udi", "String")
        self.with_optional_property("label", "String")
        self.with_optional_property("center", "Object")
        self.with_optional_property("radius", "float")
 