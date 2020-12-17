# -*- coding: utf-8 -*-
"""
    step8.persistence.BeaconsMongoDbPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsMongoDbPersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_commons.data import FilterParams
# from pip_services3_mongodb.persistence import IdentifiableMongoDbPersistence
from .IBeaconsPersistence import IBeaconsPersistence

# class BeaconsMongoDbPersistence(IdentifiableMongoDbPersistence, IBeaconsPersistence):

#     def __init__(self):
#         super(BeaconsMongoDbPersistence, self).__init__("beacons")
#         self._maxPageSize = 1000

#     def compose_filter(self, filter):
#         filter = filter if filter != None else FilterParams()
#         criteria = []

#         id = filter.get_as_nullable_string("id")
#         if id != None:
#             criteria.append({"id": id})
#         site_id = filter.get_as_nullable_string("site_id")
#         if site_id != None:
#             criteria.append({"site_id": site_id})
#         label = filter.get_as_nullable_string("label")
#         if label != None:
#             criteria.append({"label": label})
#         udi = filter.get_as_nullable_string("udi")
#         if udi != None:
#             criteria.append({"udi": udi})
#         udis = filter.get_as_object("udis")
#         if udis != None and len(udis) > 0:
#             udis = udis.split(",")
#             criteria.append({"udi": {"$in": udis}})
#         return {"$and": criteria} if len(criteria) > 0 else None

#     def get_page_by_filter(self, correlation_id, filter, paging):
#         filter = filter if filter != None else FilterParams()
#         return super(BeaconsMongoDbPersistence, self).get_page_by_filter(correlation_id, self.compose_filter(filter), paging, None, None)

#     def get_one_by_udi(self, correlation_id, udi):
#         if udi == None:
#             return None
#         item = self._collection.find_one({'udi': udi})
#         item = self._convert_to_public(item)

#         if item == None:
#             self._logger.trace(correlation_id, "Found beacon by %s", udi)
#         else:
#             self._logger.trace(correlation_id, "Cannot find beacon by %s", udi)

#         return item
