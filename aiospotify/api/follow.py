"""These endpoints allow you manage the artists, users and playlists that a Spotify user follows."""

from typing import TYPE_CHECKING, List, Optional

from aiospotify.api import Connector
from aiospotify.models import Artist, User

if TYPE_CHECKING:
    from aiospotify.models import Playlist


class Follow:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_followed_artists(self, limit: int = 20,
                                   after: Optional[Artist] = None) -> List[Artist]:
        """Get the current user’s followed artists.

        Args:
            limit (int): Optional. The maximum number of items to return.
                Default: 20. Minimum: 1. Maximum: 50.
            after (Artist): Optional. The last artist retrieved from the previous request.

        Returns:
            List[Artist]: List of artist objects.
        """
        pass

    async def follow_artist(self, artist: Artist):
        """Add the current user as a follower of the artist.

        Args:
            artist (Artist): Artist to follow.
        """
        await self.follow_artists([artist])

    async def follow_artists(self, artists: List[Artist]):
        """Add the current user as a follower of one or more artists.

        Args:
            artists (List[Artist]): Artists to follow.
                A maximum of 50 artists can be sent in one request.
        """
        pass

    async def unfollow_artist(self, artist: Artist):
        """Remove the current user as a follower of the artist.

        Args:
            artist (Artist): Artist to unfollow.
        """
        await self.unfollow_artists([artist])

    async def unfollow_artists(self, artists: List[Artist]):
        """Remove the current user as a follower of one or more artists.

        Args:
            artists (List[Artist]): Artists to unfollow.
                A maximum of 50 artists can be sent in one request.
        """
        pass

    async def is_follows_artist(self, artist: Artist) -> bool:
        """Check to see if the current user is following the artist.

        Args:
            artist (Artist): Artist to check.

        Returns:
            bool
        """
        return (await self.is_follows_artists([artist]))[0]

    async def is_follows_artists(self, artists: List[Artist]) -> List[bool]:
        """Check to see if the current user is following one or more artists.

        Args:
            artists (List[Artist]): Artists to check.

        Returns:
            List[bool]: List of True or False values, in the same order in which the artists were
                specified.
        """
        pass

    async def follow_user(self, user: User):
        """Add the current user as a follower of the Spotify user.

        Args:
            user (User): User to follow.
        """
        await self.follow_users([user])

    async def follow_users(self, users: List[User]):
        """Add the current user as a follower of one or more Spotify users.

        Args:
            users (List[User]): Users to follow.
                A maximum of 50 users can be sent in one request.
        """
        pass

    async def unfollow_user(self, user: User):
        """Remove the current user as a follower of the Spotify user.

        Args:
            user (User): User to unfollow.
        """
        await self.unfollow_users([user])

    async def unfollow_users(self, users: List[User]):
        """Remove the current user as a follower of one or more Spotify users.

        Args:
            users (List[User]): Users to unfollow.
                A maximum of 50 users can be sent in one request.
        """
        pass

    async def is_follows_user(self, user: User) -> bool:
        """Check to see if the current user is following the Spotify user.

        Args:
            user (User): User to follow.

        Returns:
            bool
        """
        return (await self.is_follows_users([user]))[0]

    async def is_follows_users(self, users: List[User]) -> List[bool]:
        """Check to see if the current user is following one or more Spotify users.

        Args:
            users (List[User]): Users to check.

        Returns:
            List[bool]: List of True or False values, in the same order in which the users were
                specified.
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
