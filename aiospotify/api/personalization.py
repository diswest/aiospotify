from aiospotify.api import Connector


class Personalization:
    def __init__(self, connector: Connector):
        self._connector = connector
