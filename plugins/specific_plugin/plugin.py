#!/usr/bin/python3.7

from core.base_plugin import BasePlugin


class ASpecificPlugin(BasePlugin):
    def __init__(self):
        super(ASpecificPlugin, self).__init__()
        self._name = "SpecificPlugin"
