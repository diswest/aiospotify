from aiospotify.api import Connector


class Profile:
    def __init__(self, connector: Connector):
        self._connector = connector
