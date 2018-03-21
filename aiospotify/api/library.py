"""Endpoints for retrieving information about, and managing, tracks that the current user has saved
in their “Your Music” library."""

from typing import List, Optional

from aiospotify.api import Connector
from aiospotify.models import Album, Track


class Library:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_saved_tracks(self, market: Optional[str] = None, limit: int = 20,
                               offset: int = 0) -> List[Track]:
        """Get a list of the songs saved in the current Spotify user’s “Your Music” library.

        Args:
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter if
                you want to apply Track Relinking.
            limit (int): Optional. The maximum number of objects to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first object to return.
                Default: 0 (i.e., the first object). Use with limit to get the next set of objects.

        Returns:
            List[Track]: List of track objects.
        """

        pass

    async def save_track(self, track: Track):
        """Save the track to the current user’s “Your Music” library.

        Args:
            track (Track): Track to save.
        """
        await self.save_tracks([track])

    async def save_tracks(self, tracks: List[Track]):
        """Save one or more tracks to the current user’s “Your Music” library.

        Args:
            tracks (List[Track]): Tracks to save. Maximum: 50 tracks.
        """
        pass

    async def remove_track(self, track: Track):
        """Remove the track from the current user’s “Your Music” library.

        Args:
            track (Track): Track to remove.

        """
        await self.remove_tracks([track])

    async def remove_tracks(self, tracks: List[Track]):
        """Remove one or more tracks from the current user’s “Your Music” library.

        Args:
            tracks (List[Track]): Tracks to remove. Maximum: 50 tracks.
        """
        pass

    async def is_track_saved(self, track: Track) -> bool:
        """Check the track is already saved in the current Spotify user’s “Your Music” library.

        Args:
            track (Track): Track to check.

        Returns:
            bool
        """
        return (await self.are_tracks_saved([track]))[0]

    async def are_tracks_saved(self, tracks: List[Track]) -> List[bool]:
        """Check if one or more tracks is already saved in the current Spotify user’s
        “Your Music” library.

        Args:
            tracks (List[Track]): Tracks to check. Maximum: 50 tracks.

        Returns:
            List[bool]: List of True or False values, in the same order in which the tracks were
                specified.
        """
        pass

    async def get_saved_albums(self, market: Optional[str] = None, limit: int = 20,
                               offset: int = 0) -> List[Album]:
        """Get a list of the albums saved in the current Spotify user’s “Your Music” library.

        Args:
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter if
                you want to apply Track Relinking.
            limit (int): Optional. The maximum number of objects to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first object to return.
                Default: 0 (i.e., the first object). Use with limit to get the next set of objects.

        Returns:
            List[Album]: List of album objects.
        """
        pass

    async def save_album(self, album: Album):
        """Save the album to the current user’s “Your Music” library.

        Args:
            album (Album): Album to save.
        """
        await self.save_albums([album])

    async def save_albums(self, albums: List[Album]):
        """Save one or more albums to the current user’s “Your Music” library.

        Args:
            albums (List[Album]): Albums to save. Maximum: 50 albums.
        """
        pass

    async def remove_album(self, album: Album):
        """Remove the album from the current user’s “Your Music” library.

        Args:
            album (Album): Album to remove.
        """
        await self.remove_albums([album])

    async def remove_albums(self, albums: List[Album]):
        """Remove one or more albums from the current user’s “Your Music” library.

        Args:
            albums (List[Album]): Albums to remove. Maximum: 50 albums.
        """
        pass

    async def is_album_saved(self, album: Album) -> bool:
        """Check if the album is already saved in the current Spotify user’s “Your Music” library.

        Args:
            album (Album): Album to check.

        Returns:
            bool
        """
        return (await self.are_albums_saved([album]))[0]

    async def are_albums_saved(self, albums: List[Album]) -> List[bool]:
        """Check if one or more albums is already saved in the current Spotify user’s
        “Your Music” library.

        Args:
            albums (List[Album]): Albums to check. Maximum: 50 albums.

        Returns:
            List[bool]: List of True or False values, in the same order in which the tracks were
                specified.
        """
        pass
