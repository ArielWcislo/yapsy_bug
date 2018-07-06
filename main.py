#!/usr/bin/python3.7

from yapsy import PluginManager


def main():
    manager = PluginManager.PluginManager()
    manager.setPluginPlaces(['plugins'])
    manager.collectPlugins()

    plugins = manager.getAllPlugins()
    for plugin in plugins:
        print(plugin, type(plugin))
        print(plugin.plugin_object, type(plugin.plugin_object))
        print(plugin.plugin_object.name)


if __name__ == "__main__":
    main()
