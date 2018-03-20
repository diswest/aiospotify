"""Endpoints for retrieving information about one or more artists from the Spotify catalog."""

from typing import List, Optional, TYPE_CHECKING

from aiospotify.api import Connector
from aiospotify.models import Album, Artist, Track

if TYPE_CHECKING:
    from aiospotify.models import SpotifyID, AlbumGroup


class Artists:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get(self, artist_id: SpotifyID) -> Artist:
        """Get Spotify catalog information for a single artist identified by their
        unique Spotify ID.

        Args:
            artist_id (SpotifyID): The Spotify ID for the artist.

        Returns:
            Artist: Artist object.
        """
        pass

    async def get_list(self, artists_ids: List[SpotifyID]) -> List[Artist]:
        """Get Spotify catalog information for several artists based on their Spotify IDs.

        Args:
            artists_ids (List[SpotifyId]): A list of the Spotify IDs for the artists.
                Maximum: 50 IDs.

        Returns:
            List[Artist]: List of artist objects.
        """
        pass

    async def get_albums(self, artist: Artist, include_groups: Optional[List[AlbumGroup]] = None,
                         market: Optional[str] = None, limit: int = 20,
                         offset: int = 0) -> List[Album]:
        """Get Spotify catalog information about an artist’s albums.

        Args:
            artist (Artist): Artist object.
            include_groups (List[AlbumGroup]): Optional. A list of keywords that will be used
                to filter the response. If not supplied, all album groups will be returned.
                Valid values are:
                    - album
                    - single
                    - appears_on
                    - compilation
            market (str): Optional. An ISO 3166-1 alpha-2 country code.
                Supply this parameter to limit the response to one particular geographical market.
            limit (int): Optional. The number of album objects to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first album to return.
                Default: 0 (i.e., the first album). Use with limit to get the next set of albums.

        Returns:
            List[Album]: List of album objects.
        """
        pass

    async def get_top_tracks(self, artist: Artist, country: Optional[str] = None) -> List[Track]:
        """Get Spotify catalog information about an artist’s top tracks by country.

        Args:
            artist (Artist): Artist object.
            country (str): Optional. An ISO 3166-1 alpha-2 country code.

        Returns:
            List[Track]: List of track objects (up to 10 tracks).
        """
        pass

    async def get_related_artists(self, artist: Artist) -> List[Artist]:
        """Get Spotify catalog information about artists similar to a given artist.
        Similarity is based on analysis of the Spotify community’s listening history.

        Args:
            artist (Artist): Artist object.

        Returns:
            List[Artist]: List of artist objects (up to 20 artists).
        """
        pass
