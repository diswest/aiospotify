from aiospotify.api import Connector


class Player:
    def __init__(self, connector: Connector):
        self._connector = connector
