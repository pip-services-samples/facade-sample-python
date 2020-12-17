# -*- coding: utf-8 -*-
"""
    step8.data.version1.BeaconV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconV1 class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""


class BeaconV1(dict):
    def __init__(self, id, site_id, type, udi, label, center, radius):
        super(BeaconV1, self).__init__()
        self['id'] = id
        self['site_id'] = site_id
        self['type'] = type
        self['udi'] = udi
        self['label'] = label
        self['center'] = center
        self['radius'] = radius

        # set class attributes in runtime
        for attr in self:
            setattr(self, attr, self[attr])
