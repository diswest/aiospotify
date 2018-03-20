"""Endpoints for retrieving information about, and managing, tracks that the current user has saved
in their “Your Music” library."""

from typing import List

from aiospotify.api import Connector
from aiospotify.models import Album, Track


class Library:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_saved_tracks(self) -> List[Track]:
        pass

    async def save_track(self, track: Track):
        await self.save_tracks([track])

    async def save_tracks(self, tracks: List[Track]):
        pass

    async def delete_track(self, track: Track):
        await self.delete_tracks([track])

    async def delete_tracks(self, tracks: List[Track]):
        pass

    async def is_track_saved(self, track: Track) -> bool:
        return (await self.are_tracks_saved([track]))[0]

    async def are_tracks_saved(self, track: List[Track]) -> List[bool]:
        pass

    async def get_saved_albums(self) -> List[Album]:
        pass

    async def save_album(self, album: Album):
        await self.save_albums([album])

    async def save_albums(self, albums: List[Album]):
        pass

    async def delete_album(self, album: Album):
        await self.delete_albums([album])

    async def delete_albums(self, albums: List[Album]):
        pass

    async def is_album_saved(self, album: Album) -> bool:
        return (await self.are_albums_saved([album]))[0]

    async def are_albums_saved(self, album: List[Album]) -> List[bool]:
        pass
