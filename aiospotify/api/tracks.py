from aiospotify.api import Connector


class Tracks:
    def __init__(self, connector: Connector):
        self._connector = connector
