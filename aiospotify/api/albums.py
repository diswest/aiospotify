"""Endpoints for retrieving information about one or more albums from the Spotify catalog."""

from typing import TYPE_CHECKING, List, Optional

from aiospotify.api import Connector
from aiospotify.models import Album, Track

if TYPE_CHECKING:
    from aiospotify.models import SpotifyID


class Albums:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get(self, album_id: SpotifyID, market: Optional[str] = None) -> Album:
        """Get Spotify catalog information for a single album.

        Args:
            album_id (SpotifyID): The Spotify ID for the album.
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter
                if you want to apply Track Relinking.

        Returns:
            Album: Album object.
        """

        # Use iso3166 package to validate market: `market in iso3166.countries_by_alpha2`
        pass

    async def get_list(self, albums_ids: List[SpotifyID],
                       market: Optional[str] = None) -> List[Album]:
        """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

        Args:
            albums_ids (List[SpotifyID]): A list of the Spotify IDs for the albums. Maximum: 20 IDs.
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter
                if you want to apply Track Relinking.

        Returns:
            List[Album]: List of album objects.
        """
        pass

    async def get_album_tracks(self, album: Album, market: Optional[str] = None, limit: int = 20,
                               offset: int = 0) -> List[Track]:
        """Get Spotify catalog information about an album’s tracks.

        Args:
            album (Album): The Spotify ID for the album.
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter
                if you want to apply Track Relinking.
            limit (int): Optional. The maximum number of tracks to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first track to return.
                Default: 0 (the first object). Use with limit to get the next set of tracks.

        Returns:
            List[Track]: List of track objects.
        """

        pass
