from aiospotify.api import Connector


class Playlists:
    def __init__(self, connector: Connector):
        self._connector = connector
