# -*- coding: utf-8 -*-
"""
    step8.persistence.BeaconsFilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsFilePersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services3_data.persistence import JsonFilePersister

from .BeaconsMemoryPersistence import BeaconsMemoryPersistence

class BeaconsFilePersistence(BeaconsMemoryPersistence):
    _persister = None

    def __init__(self, path = None):
        super(BeaconsFilePersistence, self).__init__()

        self._persister = JsonFilePersister(path)
        self._loader = self._persister
        self._saver = self._persister

    def configure(self, config):
        super(BeaconsFilePersistence, self).configure(config)
        self._persister.configure(config)
