from typing import List, Optional, Union

from aiospotify.api import Connector
from aiospotify.models import Device, Playback, Track, Album, Artist, Playlist, RepeatState


class Player:
    def __init__(self, connector: Connector):
        self._connector = connector

    async def get_available_devices(self) -> List[Device]:
        """Get information about a user’s available devices.

        Returns:
            List[Device]: List of device objects.
        """
        pass

    async def get_current_playback(self, market: Optional[str] = None) -> Playback:
        """Get information about the user’s current playback state, including track, track progress,
        and active device.

        Args:
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter if
                you want to apply Track Relinking.

        Returns:
            Playback: Playback object.
        """
        pass

    async def get_currently_playing_track(self, market: Optional[str] = None) -> Track:
        """Get the object currently being played on the user’s Spotify account.

        Args:
            market (str): Optional. An ISO 3166-1 alpha-2 country code. Provide this parameter if
                you want to apply Track Relinking.

        Returns:
            Track: Track object.
        """
        pass

    async def transfer_playback(self, device: Device, play: bool = False):
        """Transfer playback to a new device and determine if it should start playing.

        Args:
            device (Device): The device on which playback should be started/transferred.
            play (bool): Optional.
                true: ensure playback happens on new device.
                false or not provided: keep the current playback state.
        """

    async def start(self, device: Optional[Device] = None, tracks: Optional[List[Track]] = None,
                    context_object: Optional[Union[Album, Artist, Playlist]] = None,
                    from_track: Optional[Track] = None, offset: int = 0):
        """Start a new context or resume current playback on the user’s active device.

        Only one of either context_object or tracks can be specified. If neither is present,
        calling the method will resume playback.

        If context_object is a Playlist or Album, or when tracks is provided, then only one of
        either offset or from_track can be added to specify starting track in the context.

        If incorrect values are provided for offset or from_track, the request may be accepted but
        with an unpredictable resulting action on playback.

        Args:
            device (Device): Optional. The device this command is targeting. If not supplied,
                the user's currently active device is the target.
            tracks (List[Track]): Optional. A List of the Spotify tracks to play.
            context_object (Album, Artist, Playlist): Optional. Spotify context object to play.
                Valid contexts are albums, artists & playlists.
            from_track (Track): Optional. Indicates the track from where in the context playback
                should start.
                Only available when context_object corresponds to an album or playlist object,
                or when the tracks parameter is used.
            offset (int): Optional. Indicates the position from where in the context playback
                should start. It's zero based and can’t be negative
                Only available when context_object corresponds to an album or playlist object,
                or when the tracks parameter is used.
        """
        pass

    async def pause(self, device: Optional[Device] = None):
        """Pause playback on the user’s account.

        Args:
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def next(self, device: Optional[Device] = None):
        """Skips to next track in the user’s queue.

        Args:
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def previous(self, device: Optional[Device] = None):
        """Skips to previous track in the user’s queue.

        Note that this will ALWAYS skip to the previous track, regardless of the current track’s
        progress. Returning to the start of the current track should be performed using
        the seek method.

        Args:
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def seek(self, position_ms: int, device: Optional[Device] = None):
        """Seeks to the given position in the user’s currently playing track.

        Args:
            position_ms (int): The position in milliseconds to seek to. Must be a positive number.
                Passing in a position that is greater than the length of the track will cause
                the player to start playing the next song.
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def set_repeat_state(self, state: RepeatState, device: Optional[Device] = None):
        """Set the repeat mode for the user’s playback. Options are repeat-track,
        repeat-context, and off.

        Args:
            state (RepeatState): track will repeat the current track.
                context will repeat the current context.
                off will turn repeat off.
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def set_volume(self, volume_percent: int, device: Optional[Device] = None):
        """Set the volume for the user’s current playback device.

        Args:
            volume_percent (int): The volume to set. Must be a value from 0 to 100 inclusive.
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
        pass

    async def toggle_shuffle(self, state: bool, device: Optional[Device] = None):
        """Toggle shuffle on or off for user’s playback.

        Args:
            state (bool): true: Shuffle user's playback
                false: Do not shuffle user's playback
            device (Device): Optional. The device this command is targeting.
                If not supplied, the user's currently active device is the target.
        """
