SpotifyID = str
"""The base-62 identifier that you can find at the end of the Spotify URI (see above) for an artist,
track, album, playlist, etc. Unlike a Spotify URI, a Spotify ID does not clearly identify the type 
of resource; that information is provided elsewhere in the call.

Examples:
    6rqhFgbbKwnb9MLmUQDhG6
"""

SpotifyUserID = str
"""The unique string identifying the Spotify user that you can find at the end of the Spotify URI 
for the user.

Examples:
    wizzler
"""

SpotifyCategoryID = str
"""The unique string identifying the Spotify category.

Examples:
    party
"""

SpotifyURI = str
"""str: The resource identifier that you can enter, for example, in the Spotify Desktop client's
search box to locate an artist, album, or track.

Examples:
    spotify:track:6rqhFgbbKwnb9MLmUQDhG6
"""

SpotifyURL = str
"""An HTML link that opens a track, album, app, playlist or other Spotify resource in a Spotify 
client (which client is determined by the user's device and account settings at play.spotify.com).

Examples:
    http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
"""

Genre = str
"""str: See: https://developer.spotify.com/web-api/get-recommendations/#available-genre-seeds

Examples: 
    alt_rock
"""