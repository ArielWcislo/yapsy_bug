#!/usr/bin/python3.7

from yapsy.IPlugin import IPlugin


class BasePlugin(IPlugin):
    def __init__(self):
        super(BasePlugin, self).__init__()
        self._name = 'Base'

    @property
    def name(self):
        return self._name
