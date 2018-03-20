from aiospotify.api import Connector


class Search:
    def __init__(self, connector: Connector):
        self._connector = connector
