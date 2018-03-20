import asyncio
from typing import Optional

from aiospotify import api


class Spotify:
    def __init__(self, connector: Optional[api.Connector] = None,
                 loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()):
        self._connector = connector if connector else api.Connector(loop)
        self._albums = api.Albums(self._connector)
        self._artists = api.Artists(self._connector)
        self._browse = api.Browse(self._connector)
        self._follow = api.Follow(self._connector)
        self._library = api.Library(self._connector)
        self._personalization = api.Personalization(self._connector)
        self._player = api.Player(self._connector)
        self._profile = api.Profile(self._connector)
        self._search = api.Search(self._connector)
        self._tracks = api.Tracks(self._connector)

    def __del__(self):
        if self._connector.is_open():
            self._connector.close()

    @property
    def albums(self) -> api.Albums:
        return self._albums

    @property
    def artists(self) -> api.Artists:
        return self._artists

    @property
    def browse(self) -> api.Browse:
        return self._browse

    @property
    def follow(self) -> api.Follow:
        return self._follow

    @property
    def library(self) -> api.Library:
        return self._library

    @property
    def personalization(self) -> api.Personalization:
        return self._personalization

    @property
    def player(self) -> api.Player:
        return self._player

    @property
    def profile(self) -> api.Profile:
        return self._profile

    @property
    def search(self) -> api.Search:
        return self._search

    @property
    def tracks(self) -> api.Tracks:
        return self._tracks
