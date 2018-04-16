"""Endpoints for retrieving information about a user’s playlists and for managing
a user’s playlists."""

from datetime import datetime
from typing import Optional, List, TYPE_CHECKING, Dict, Union

from aiospotify.api import Connector
from aiospotify.models import Playlist, User, Track, SpotifyID, Snapshot

if TYPE_CHECKING:
    from aiospotify.models import Category


class Playlists:
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

    async def follow_playlist(self, playlist_owner: User, playlist: Playlist, public: bool = True):
        """Add the current user as a follower of a playlist.

        Args:
            playlist_owner (User): The Spotify user of the person who owns the playlist.
            playlist (Playlist): The Spotify playlist. Any playlist can be followed, regardless of
                its public/private status, as long as you know its playlist ID.
            public (bool): Optional, default true. If true the playlist will be included in user's
                public playlists, if false it will remain private. To be able to follow playlists
                privately, the user must have granted the playlist-modify-private scope.
        """
        pass

    async def unfollow_playlist(self, playlist_owner: User, playlist: Playlist):
        """Remove the current user as a follower of a playlist.

        Args:
            playlist_owner (User): The Spotify user of the person who owns the playlist.
            playlist (Playlist): The Spotify ID of the playlist that is to be no longer followed.
        """
        pass

    async def search_playlist(self):
        pass

    async def get_user_playlists(self, user: User, limit: int = 20,
                                 offset: int = 0) -> List[Playlist]:
        """Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user (User): The Spotify user.
            limit (int): Optional. The maximum number of playlists to return.
                Default: 20. Minimum: 1. Maximum: 50.
            offset (int): Optional. The index of the first playlist to return.
                Default: 0 (the first object). Maximum offset: 100.000.

        Returns:
            List[Playlist]: List of playlist objects.
        """
        pass

    async def get_playlist(self, user: User, playlist_id: SpotifyID, fields: Optional[str] = None,
                           market: Optional[str] = None) -> Playlist:
        """Get a playlist owned by a Spotify user.

        Args:
            user (User): he Spotify user.
            playlist_id (SpotifyID): The Spotify ID for the playlist.
            fields (str): Optional. Filters for the query: a comma-separated list of the fields
                to return. If omitted, all fields are returned.
                For example, to get just the playlist's description and URI:

                    `fields=description,uri`

                A dot separator can be used to specify non-reoccurring fields, while parentheses
                can be used to specify reoccurring fields within objects.
                For example, to get just the added date and user ID of the adder:

                    `fields=tracks.items(added_at,added_by.id)`

                Use multiple parentheses to drill down into nested objects, for example:

                    `fields=tracks.items(track(name,href,album(name,href)))`

                Fields can be excluded by prefixing them with an exclamation mark, for example:

                    `fields=tracks.items(track(name,href,album(!name,href)))`

            market (str): Optional. An ISO 3166-1 alpha-2 country code.
                Provide this parameter if you want to apply Track Relinking.

        Returns:
            Playlist: Playlist object.
        """
        pass

    async def get_playlist_tracks(self, user: User, playlist_id: SpotifyID,
                                  fields: Optional[str] = None, market: Optional[str] = None,
                                  limit: int = 100, offset: int = 0) -> List[Track]:
        """Get full details of the tracks of a playlist owned by a Spotify user.

        Args:
            user (User): The Spotify user.
            playlist_id (SpotifyID): The Spotify ID for the playlist.
            fields (str): Optional. Filters for the query: a comma-separated list of the fields
                to return. If omitted, all fields are returned.
                For example, to get just the playlist's description and URI:

                    `fields=description,uri`

                A dot separator can be used to specify non-reoccurring fields, while parentheses
                can be used to specify reoccurring fields within objects.
                For example, to get just the added date and user ID of the adder:

                    `fields=tracks.items(added_at,added_by.id)`

                Use multiple parentheses to drill down into nested objects, for example:

                    `fields=tracks.items(track(name,href,album(name,href)))`

                Fields can be excluded by prefixing them with an exclamation mark, for example:

                    `fields=tracks.items(track(name,href,album(!name,href)))`

            market (str): Optional. An ISO 3166-1 alpha-2 country code.
                Provide this parameter if you want to apply Track Relinking.
            limit (int): Optional. The maximum number of tracks to return.
                Default: 100. Minimum: 1. Maximum: 100.
            offset (int): Optional. The index of the first track to return.
                Default: 0 (the first object).

        Returns:
            List[Track]: List of track objects.
        """
        pass

    async def create_playlist(self, user: User, name: str, description: Optional[str] = None,
                              public: bool = True, collaborative: bool = False):
        """Create a playlist for a Spotify user. (The playlist will be empty until you add tracks.)

        Args:
            user (User): The Spotify user.
            name (str): The name for the new playlist.This name does not need to be unique;
                a user may have several playlists with the same name.
            description (str): Optional, value for playlist description as displayed
                in Spotify Clients and in the Web API.
            public (bool): Optional, default true. If true the playlist will be public,
                if false it will be private. To be able to create private playlists,
                the user must have granted the playlist-modify-private scope.
            collaborative (bool): Optional, default false. If true the playlist will
                be collaborative. Note that to create a collaborative playlist you must also set
                public to false. To create collaborative playlists you must
                have granted playlist-modify-private and playlist-modify-public scopes.
        """
        pass

    async def update_playlist(self, user: User, playlist: Playlist, name: Optional[str] = None,
                              description: Optional[str] = None, public: bool = True,
                              collaborative: bool = False):
        """Change a playlist’s name and public/private state.
        (The user must, of course, own the playlist.)

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            name (str): Optional. The new name for the playlist.
            description (str): Optional, value for playlist description as displayed
                in Spotify Clients and in the Web API.
            public (bool): Optional. If true the playlist will be public,
                if false it will be private.
            collaborative (bool): Optional. If true, the playlist will become collaborative and
                other users will be able to modify the playlist in their Spotify client.
                Note: You can only set collaborative to true on non-public playlists.
        """
        pass

    async def add_track_to_playlist(self, user: User, playlist: Playlist, track: Track,
                                    position: Optional[int] = None) -> Snapshot:
        """Add a track to a user’s playlist. Note that local tracks can’t be added.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            track (Track): Track to add.
            position (int): Optional. The position to insert the tracks, a zero-based index.
                For example, to insert the tracks in the first position: position=0; to insert
                the tracks in the third position: position=2. If omitted, the tracks
                will be appended to the playlist. Tracks are added in the order they are listed
                in the query string or request body.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def add_tracks_to_playlist(self, user: User, playlist: Playlist, tracks: List[Track],
                                     position: Optional[int] = None) -> Snapshot:
        """Add one or more tracks to a user’s playlist. Note that local tracks can’t be added.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            tracks (List[Tracks]): Tracks to add.
                A maximum of 100 tracks can be added in one request.
            position (int): Optional. The position to insert the tracks, a zero-based index.
                For example, to insert the tracks in the first position: position=0; to insert
                the tracks in the third position: position=2. If omitted, the tracks
                will be appended to the playlist. Tracks are added in the order they are listed
                in the query string or request body.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def remove_track_from_playlist(self, user: User, playlist: Playlist,
                                         track: Union[Track, Dict[Track, List[int]]],
                                         snapshot: Optional[Snapshot] = None) -> Snapshot:
        """Remove a track from a user’s playlist.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            track (Union[Track, Dict[Track, List[int]]]): Track to remove.
                You can remove a track from a certain position by specifying both the track
                and the zero-based track position in the playlist. If you specify incorrect
                information (for example, if the given track does not exist at the given position)
                an error will be returned and the entire request will fail.
            snapshot (Snapshot): Optional. The playlist's snapshot against which you want to make
                the changes. The API will validate that the specified tracks exist and in the
                specified positions and make the changes, even if more recent changes have been
                made to the playlist.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def remove_tracks_from_playlist(self, user: User, playlist: Playlist,
                                          tracks: Union[List[Track], Dict[Track, List[int]]],
                                          snapshot: Optional[Snapshot] = None) -> Snapshot:
        """Remove one or more tracks from a user’s playlist.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            tracks (Union[List[Track], Dict[Track, List[int]]]): Tracks to remove.
                You can remove a track from a certain position by specifying both the track
                and the zero-based track position in the playlist. If you specify incorrect
                information (for example, if the given track does not exist at the given position)
                an error will be returned and the entire request will fail.
                A maximum of 100 objects can be sent at once.
            snapshot (Snapshot): Optional. The playlist's snapshot against which you want to make
                the changes. The API will validate that the specified tracks exist and in the
                specified positions and make the changes, even if more recent changes have been
                made to the playlist.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def remove_track_from_playlist_by_position(self, user: User, playlist: Playlist,
                                                     position: int,
                                                     snapshot: Optional[
                                                         Snapshot] = None) -> Snapshot:
        """Remove a track from a user’s playlist.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            position (int): The position parameter is zero-indexed, that is the
                first track in the playlist has the value 0, the second track 1, and so on.
            snapshot (Snapshot): Optional. The playlist's snapshot against which you want to make
                the changes. The API will validate that the specified tracks exist and in the
                specified positions and make the changes, even if more recent changes have been
                made to the playlist.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def remove_tracks_from_playlist_by_positions(self, user: User, playlist: Playlist,
                                                       positions: List[int],
                                                       snapshot: Optional[
                                                           Snapshot] = None) -> Snapshot:
        """Remove one or more tracks from a user’s playlist.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            positions (List[int]): The positions parameter is zero-indexed, that is the
                first track in the playlist has the value 0, the second track 1, and so on.
                A maximum of 100 positions can be sent at once.
            snapshot (Snapshot): Optional. The playlist's snapshot against which you want to make
                the changes. The API will validate that the specified tracks exist and in the
                specified positions and make the changes, even if more recent changes have been
                made to the playlist.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def reorder_playlist_tracks(self, user: User, playlist: Playlist, range_start: int,
                                      insert_before: int, range_length: int = 1,
                                      snapshot: Optional[Snapshot] = None):
        """Reorder a track or a group of tracks in a playlist.
        When reordering tracks, the timestamp indicating when they were added and the user who
        added them will be kept untouched. In addition, the users following the playlists
        won’t be notified about changes in the playlists when the tracks are reordered.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            range_start (int): The position of the first track to be reordered.
            insert_before (int): The position where the tracks should be inserted.
                To reorder the tracks to the end of the playlist, simply set insert_before
                to the position after the last track.

                Examples
                    To reorder the first track to the last position in a playlist with 10 tracks,
                    set range_start to 0, and insert_before to 10.

                    To reorder the last track in a playlist with 10 tracks to the
                    start of the playlist, set range_start to 9, and insert_before to 0.

            range_length (int): The amount of tracks to be reordered. Defaults to 1 if not set.
                The range of tracks to be reordered begins from the range_start position, and
                includes the range_length subsequent tracks.

                Example
                    To move the tracks at index 9-10 to the start of the playlist, range_start
                    is set to 9, and range_length is set to 2.

            snapshot (Snapshot): The playlist's snapshot against which you want to make the changes.

        Returns:
            Snapshot: Snapshot object.
        """
        pass

    async def replace_playlist_tracks(self, user: User, playlist: Playlist, tracks: List[Track]):
        """Replace all the tracks in a playlist, overwriting its existing tracks.
        This powerful request can be useful for replacing tracks, re-ordering existing tracks,
        or clearing the playlist.

        Args:
            user (User): The Spotify user.
            playlist (Playlist): The Spotify playlist.
            tracks (List[Track]): List of tracks. A maximum of 100 tracks can be set in one request.
                An empty list will clear the playlist.
        """
        pass

    async def is_user_follows_playlist(self, user: User, playlist_owner: User,
                                       playlist: Playlist) -> bool:
        """Check to see if the Spotify user is following a specified playlist.

        Args:
            user (User): The Spotify user that you want to check to see if they follow the playlist.
            playlist_owner (User): The Spotify user of the person who owns the playlist.
            playlist (Playlist): The Spotify of the playlist.

        Returns:
            bool
        """
        return (await self.are_users_follow_playlist([user], playlist_owner, playlist))[0]

    async def are_users_follow_playlist(self, users: List[User], playlist_owner: User,
                                        playlist: Playlist) -> List[bool]:
        """Check to see if one or more Spotify users are following a specified playlist.

        Args:
            users (List[User]): The users that you want to check to see if they follow the playlist.
                Maximum: 5 ids.
            playlist_owner (User): The Spotify user of the person who owns the playlist.
            playlist (Playlist): The Spotify of the playlist.

        Returns:
            List[bool]: List of True or False values, in the same order in which the users were
                specified.
        """
        pass

    async def upload_playlist_cover(self):
        pass
