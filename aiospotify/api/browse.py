"""Endpoints for getting playlists and new album releases featured on Spotify’s Browse tab."""

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from aiospotify.api import Connector
from aiospotify.models import Album, Category, Playlist, Recommendations, Genre

if TYPE_CHECKING:
    from aiospotify.models import SeedsConfig, SpotifyCategoryID


class Browse:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_featured_playlists(self, country: Optional[str] = None,
                                     locale: Optional[str] = None,
                                     timestamp: Optional[datetime] = None, limit: int = 20,
                                     offset: int = 0) -> List[Playlist]:
        """Get a list of Spotify featured playlists (shown, for example, on a Spotify player’s
            “Browse” tab).

        Args:
            country (str): Optional. A country: an ISO 3166-1 alpha-2 country code. Provide this
                parameter if you want the list of returned items to be relevant to a particular
                country. If omitted, the returned items will be relevant to all countries.
            locale (str): Optional. The desired language, consisting of a lowercase ISO 639 language
                code and an uppercase ISO 3166-1 alpha-2 country code, joined by an underscore.
                For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want
                the results returned in a particular language (where available).

                Note that, if locale is not supplied, or if the specified language is not available,
                all strings will be returned in the Spotify default language (American English).

                The locale parameter, combined with the country parameter, may give odd results if
                not carefully matched. For example country=SE&locale=de_DE will return a list of
                categories relevant to Sweden but as German language strings.
            timestamp (datetime): Optional. A timestamp. Use this parameter to specify the user's
                local time to get results tailored for that specific date and time in the day.
            limit (int): Optional. The maximum number of items to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first item to return.
                Default: 0 (the first object). Use with limit to get the next set of items.

        Returns:
            List[Playlist]: List of playlist objects.
        """
        pass

    async def get_new_releases(self, country: Optional[str] = None, limit: int = 20,
                               offset: int = 0) -> List[Album]:
        """Get a list of new album releases featured in Spotify (shown, for example, on a
            Spotify player’s “Browse” tab).

        Args:
            country (str): Optional. A country: an ISO 3166-1 alpha-2 country code. Provide this
                parameter if you want the list of returned items to be relevant to a particular
                country. If omitted, the returned items will be relevant to all countries.
            limit (int): Optional. The maximum number of items to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first item to return.
                Default: 0 (the first object). Use with limit to get the next set of items.

        Returns:
            List[Album]: List of album objects.
        """
        pass

    async def get_categories(self, country: Optional[str] = None,
                             locale: Optional[str] = None, limit: int = 20,
                             offset: int = 0) -> List[Category]:
        """Get a list of categories used to tag items in Spotify (on, for example, the
            Spotify player’s “Browse” tab).

        Args:
            country (str): Optional. A country: an ISO 3166-1 alpha-2 country code. Provide this
                parameter if you want to narrow the list of returned categories to those relevant
                to a particular country. If omitted, the returned items will be globally relevant.
            locale (str): Optional. The desired language, consisting of an ISO 639 language code
                and an ISO 3166-1 alpha-2 country code, joined by an underscore.
                For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want
                the category metadata returned in a particular language.

                Note that, if locale is not supplied, or if the specified language is not available,
                all strings will be returned in the Spotify default language (American English).

                The locale parameter, combined with the country parameter, may give odd results if
                not carefully matched. For example country=SE&locale=de_DE will return a list of
                categories relevant to Sweden but as German language strings.
            limit (int): Optional. The maximum number of categories to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first item to return.
                Default: 0 (the first object). Use with limit to get the next set of categories.

        Returns:
            List[Category]: List of category objects.
        """
        pass

    async def get_category(self, category_id: SpotifyCategoryID, country: Optional[str] = None,
                           locale: Optional[str] = None) -> Category:
        """Get a single category used to tag items in Spotify (on, for example, the
            Spotify player’s “Browse” tab).

        Args:
            category_id (SpotifyCategoryID): The Spotify category ID for the category.
            country (str): Optional. A country: an ISO 3166-1 alpha-2 country code. Provide this
                parameter to ensure that the category exists for a particular country.
            locale (str): Optional. The desired language, consisting of an ISO 639 language code
                and an ISO 3166-1 alpha-2 country code, joined by an underscore.
                For example: es_MX, meaning "Spanish (Mexico)". Provide this parameter if you want
                the category strings returned in a particular language.

                Note that, if locale is not supplied, or if the specified language is not available,
                the category strings returned will be in the Spotify default
                language (American English).

        Returns:
            Category: Category object.
        """
        pass

    async def get_category_playlists(self, category: Category, country: Optional[str] = None,
                                     limit: int = 20, offset: int = 0) -> List[Playlist]:
        """Get a list of Spotify playlists tagged with a particular category.

        Args:
            category (Category): Category object.
            country (str): Optional. A country: an ISO 3166-1 alpha-2 country code.
            limit (int): Optional. The maximum number of items to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first item to return.
                Default: 0 (the first object). Use with limit to get the next set of items.

        Returns:
            List[Playlist]: List of category objects.
        """
        pass

    async def get_recommendations_by_seeds(self, config: SeedsConfig, market: Optional[str] = None,
                                           limit: int = 20) -> Recommendations:
        """Create a playlist-style listening experience based on seed artists, tracks and genres.

        Recommendations are generated based on the available information for a given seed entity and
        matched against similar artists and tracks. If there is sufficient information about the
        provided seeds, a list of tracks will be returned together with pool size details.

        For artists and tracks that are very new or obscure there might not be enough data to
        generate a list of tracks.

        Args:
            config (SeedsConfig): Seeds and tuneable track attributes
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter if
                you want to apply Track Relinking. Because min_*, max_* and target_* are applied to
                pools before relinking, the generated results may not precisely match the filters
                applied. Original, non-relinked tracks are available via the linked_from attribute
                of the relinked track response.
            limit (int): Optional. The target size of the list of recommended tracks. For seeds
                with unusually small pools or when highly restrictive filtering is applied, it may
                be impossible to generate the requested number of recommended tracks.
                Debugging information for such cases is available in the response.
                Default: 20. Minimum: 1. Maximum: 100.

        Returns:
            Recommendations: Recommendations object.
        """
        pass

    async def get_available_genre_seeds(self) -> List[Genre]:
        """Get available recommendation seeds genres.

        Returns:
            List[Genre]: List of genres.
        """
        pass
