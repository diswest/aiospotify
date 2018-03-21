"""Endpoints for retrieving information about the user’s listening habits."""
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from aiospotify.api import Connector
from aiospotify.models import Artist, Track

if TYPE_CHECKING:
    from aiospotify.models import TimeRange


class Personalization:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_top_artists(self, time_range: TimeRange = TimeRange.MEDIUM_TERM, limit: int = 20,
                              offset: int = 0) -> List[Artist]:
        """Get the current user’s top artists based on calculated affinity.

        Affinity is a measure of the expected preference a user has for a particular track or
        artist.  It is based on user behavior, including play history, but does not include actions
        made while in incognito mode. Light or infrequent users of Spotify may not have sufficient
        play history to generate a full affinity data set.

        As a user’s behavior is likely to shift over time, this preference data is available over
        three time spans. See time_range in the query parameter table for more information.

        For each time range, the top 50 artists are available for each user.
        In the future, it is likely that this restriction will be relaxed.
        This data is typically updated once each day for each user.

        Args:
            time_range (TimeRange): Optional. Over what time frame the affinities are computed.
                Valid values: long_term (calculated from several years of data and including all
                new data as it becomes available), medium_term (approximately last 6 months),
                short_term (approximately last 4 weeks). Default: medium_term.
            limit (int): Optional. The number of entities to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first entity to return.
                Default: 0 (i.e., the first artist). Use with limit to get the next set of entities.

        Returns:
            List[Artist]: List of artist objects.
        """
        pass

    async def get_top_tracks(self, time_range: TimeRange = TimeRange.MEDIUM_TERM, limit: int = 20,
                             offset: int = 0) -> List[Track]:
        """Get the current user’s top tracks based on calculated affinity.

        Affinity is a measure of the expected preference a user has for a particular track or
        artist.  It is based on user behavior, including play history, but does not include actions
        made while in incognito mode. Light or infrequent users of Spotify may not have sufficient
        play history to generate a full affinity data set.

        As a user’s behavior is likely to shift over time, this preference data is available over
        three time spans. See time_range in the query parameter table for more information.

        For each time range, the top 50 tracks are available for each user.
        In the future, it is likely that this restriction will be relaxed.
        This data is typically updated once each day for each user.

        Args:
            time_range (TimeRange): Optional. Over what time frame the affinities are computed.
                Valid values: long_term (calculated from several years of data and including all
                new data as it becomes available), medium_term (approximately last 6 months),
                short_term (approximately last 4 weeks). Default: medium_term.
            limit (int): Optional. The number of entities to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first entity to return.
                Default: 0 (i.e., the first track). Use with limit to get the next set of entities.

        Returns:
            List[Track]: List of track objects.
        """
        pass

    async def get_recently_played_tracks(self, limit: int = 20, after: Optional[datetime] = None,
                                         before: Optional[datetime] = None) -> List[Track]:
        """Get tracks from the current user’s recently played tracks.

        Returns the most recent 50 tracks played by a user. Note that a track currently playing
        will not be visible in play history until it has completed. A track must be played for more
        than 30 seconds to be included in play history.

        Any tracks listened to while the user had “Private Session” enabled in their client will
        not be returned in the list of recently played tracks.

        The endpoint uses a bidirectional cursor for paging. Follow the next field with the before
        parameter to move back in time, or use the after parameter to move forward in time. If you
        supply no before or after parameter, the endpoint will return the most recently played
        songs, and the next link will page back in time.

        Args:
            limit (int): Optional. The maximum number of items to return.
                Default: 20. Minimum: 1. Maximum: 50.
            after (datetime): Optional. Returns all items after (but not including) this cursor
                position. If after is specified, before must not be specified.
            before (datetime): Optional. Returns all items before (but not including) this cursor
                position. If before is specified, after must not be specified.

        Returns:
            List[Track]: List of track objects.
        """
        pass
