from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from aiospotify.models import Key, Mode, Artist, Genre, Track


class SeedsConfig:
    def __init__(self, seed_artists: Optional[List[Artist]] = None,
                 seed_genres: Optional[List[Genre]] = None,
                 seed_tracks: Optional[List[Track]] = None):

        seeds_total = 0
        seeds_total += len(seed_artists) if seed_artists else 0
        seeds_total += len(seed_genres) if seed_genres else 0
        seeds_total += len(seed_tracks) if seed_tracks else 0

        if seeds_total == 0:
            raise ValueError('Seeds can\'t be empty.')

        if seeds_total > 5:
            raise ValueError('Up to 5 seed values may be provided in any combination of '
                             'seed_artists, seed_tracks and seed_genres.')

        self._config = {}

        if seed_artists:
            self._config['seed_artists'] = seed_artists
        if seed_genres:
            self._config['seed_genres'] = seed_genres
        if seed_tracks:
            self._config['seed_tracks'] = seed_tracks

    def as_dict(self):
        return self._config

    @property
    def target_acousticness(self) -> float:
        """A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
        1.0 represents high confidence the track is acoustic.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Acousticness
        """
        return self._config['target_acousticness']

    @target_acousticness.setter
    def target_acousticness(self, acousticness: float):
        if acousticness < 0.0 or acousticness > 1.0:
            raise ValueError('Acousticness must be between 0.0 and 1.0')
        self._config['target_acousticness'] = acousticness

    @property
    def min_acousticness(self) -> float:
        """A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
        1.0 represents high confidence the track is acoustic.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Acousticness
        """
        return self._config['min_acousticness']

    @min_acousticness.setter
    def min_acousticness(self, acousticness: float):
        if acousticness < 0.0 or acousticness > 1.0:
            raise ValueError('Acousticness must be between 0.0 and 1.0')
        self._config['min_acousticness'] = acousticness

    @property
    def max_acousticness(self) -> float:
        """A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
        1.0 represents high confidence the track is acoustic.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Acousticness
        """
        return self._config['max_acousticness']

    @max_acousticness.setter
    def max_acousticness(self, acousticness: float):
        if acousticness < 0.0 or acousticness > 1.0:
            raise ValueError('Acousticness must be between 0.0 and 1.0')
        self._config['max_acousticness'] = acousticness

    @property
    def target_danceability(self) -> float:
        """Danceability describes how suitable a track is for dancing based on a combination of
        musical elements including tempo, rhythm stability, beat strength, and overall regularity.
        A value of 0.0 is least danceable and 1.0 is most danceable.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Danceability
        """
        return self._config['target_danceability']

    @target_danceability.setter
    def target_danceability(self, danceability: float):
        if danceability < 0.0 or danceability > 1.0:
            raise ValueError('Danceability must be between 0.0 and 1.0')
        self._config['target_danceability'] = danceability

    @property
    def min_danceability(self) -> float:
        """Danceability describes how suitable a track is for dancing based on a combination of
        musical elements including tempo, rhythm stability, beat strength, and overall regularity.
        A value of 0.0 is least danceable and 1.0 is most danceable.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Danceability
        """
        return self._config['min_danceability']

    @min_danceability.setter
    def min_danceability(self, danceability: float):
        if danceability < 0.0 or danceability > 1.0:
            raise ValueError('Danceability must be between 0.0 and 1.0')
        self._config['min_danceability'] = danceability

    @property
    def max_danceability(self) -> float:
        """Danceability describes how suitable a track is for dancing based on a combination of
        musical elements including tempo, rhythm stability, beat strength, and overall regularity.
        A value of 0.0 is least danceable and 1.0 is most danceable.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Danceability
        """
        return self._config['max_danceability']

    @max_danceability.setter
    def max_danceability(self, danceability: float):
        if danceability < 0.0 or danceability > 1.0:
            raise ValueError('Danceability must be between 0.0 and 1.0')
        self._config['max_danceability'] = danceability

    @property
    def target_duration_ms(self) -> int:
        """The duration of the track in milliseconds.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            int: Duration (ms)
        """
        return self._config['target_duration_ms']

    @target_duration_ms.setter
    def target_duration_ms(self, duration_ms: int):
        self._config['target_duration_ms'] = duration_ms

    @property
    def min_duration_ms(self) -> int:
        """The duration of the track in milliseconds.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Duration (ms)
        """
        return self._config['min_duration_ms']

    @min_duration_ms.setter
    def min_duration_ms(self, duration_ms: int):
        self._config['min_duration_ms'] = duration_ms

    @property
    def max_duration_ms(self) -> int:
        """The duration of the track in milliseconds.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Duration (ms)
        """
        return self._config['max_duration_ms']

    @max_duration_ms.setter
    def max_duration_ms(self, duration_ms: int):
        self._config['max_duration_ms'] = duration_ms

    @property
    def target_energy(self) -> float:
        """Energy is a measure from 0.0 to 1.0 and represents a perceptual measure
        of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
        For example, death metal has high energy, while a Bach prelude scores low on the scale.
        Perceptual features contributing to this attribute include dynamic range, perceived
        loudness, timbre, onset rate, and general entropy.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Energy
        """
        return self._config['target_energy']

    @target_energy.setter
    def target_energy(self, energy: float):
        if energy < 0.0 or energy > 1.0:
            raise ValueError('Energy must be between 0.0 and 1.0')
        self._config['target_energy'] = energy

    @property
    def min_energy(self) -> float:
        """Energy is a measure from 0.0 to 1.0 and represents a perceptual measure
        of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
        For example, death metal has high energy, while a Bach prelude scores low on the scale.
        Perceptual features contributing to this attribute include dynamic range, perceived
        loudness, timbre, onset rate, and general entropy.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Energy
        """
        return self._config['min_energy']

    @min_energy.setter
    def min_energy(self, energy: float):
        if energy < 0.0 or energy > 1.0:
            raise ValueError('Energy must be between 0.0 and 1.0')
        self._config['min_energy'] = energy

    @property
    def max_energy(self) -> float:
        """Energy is a measure from 0.0 to 1.0 and represents a perceptual measure
        of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
        For example, death metal has high energy, while a Bach prelude scores low on the scale.
        Perceptual features contributing to this attribute include dynamic range, perceived
        loudness, timbre, onset rate, and general entropy.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Energy
        """
        return self._config['max_energy']

    @max_energy.setter
    def max_energy(self, energy: float):
        if energy < 0.0 or energy > 1.0:
            raise ValueError('Energy must be between 0.0 and 1.0')
        self._config['max_energy'] = energy

    @property
    def target_instrumentalness(self) -> float:
        """Predicts whether a track contains no vocals. "Ooh" and "aah" sounds
        are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal".
        The closer the instrumentalness value is to 1.0, the greater likelihood the track contains
        no vocal content. Values above 0.5 are intended to represent instrumental tracks, but
        confidence is higher as the value approaches 1.0.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Instrumentalness
        """
        return self._config['target_instrumentalness']

    @target_instrumentalness.setter
    def target_instrumentalness(self, instrumentalness: float):
        if instrumentalness < 0.0 or instrumentalness > 1.0:
            raise ValueError('Instrumentalness must be between 0.0 and 1.0')
        self._config['target_instrumentalness'] = instrumentalness

    @property
    def min_instrumentalness(self) -> float:
        """Predicts whether a track contains no vocals. "Ooh" and "aah" sounds
        are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal".
        The closer the instrumentalness value is to 1.0, the greater likelihood the track contains
        no vocal content. Values above 0.5 are intended to represent instrumental tracks, but
        confidence is higher as the value approaches 1.0.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Instrumentalness
        """
        return self._config['min_instrumentalness']

    @min_instrumentalness.setter
    def min_instrumentalness(self, instrumentalness: float):
        if instrumentalness < 0.0 or instrumentalness > 1.0:
            raise ValueError('Instrumentalness must be between 0.0 and 1.0')
        self._config['min_instrumentalness'] = instrumentalness

    @property
    def max_instrumentalness(self) -> float:
        """Predicts whether a track contains no vocals. "Ooh" and "aah" sounds
        are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal".
        The closer the instrumentalness value is to 1.0, the greater likelihood the track contains
        no vocal content. Values above 0.5 are intended to represent instrumental tracks, but
        confidence is higher as the value approaches 1.0.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Instrumentalness
        """
        return self._config['max_instrumentalness']

    @max_instrumentalness.setter
    def max_instrumentalness(self, instrumentalness: float):
        if instrumentalness < 0.0 or instrumentalness > 1.0:
            raise ValueError('Instrumentalness must be between 0.0 and 1.0')
        self._config['max_instrumentalness'] = instrumentalness

    @property
    def target_key(self) -> Key:
        """The key the track is in. Integers map to pitches using standard Pitch Class notation.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            Key: Key
        """
        return self._config['target_key']

    @target_key.setter
    def target_key(self, key: Key):
        self._config['target_key'] = key

    @property
    def min_key(self) -> Key:
        """The key the track is in. Integers map to pitches using standard Pitch Class notation.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            Key: Key
        """
        return self._config['min_key']

    @min_key.setter
    def min_key(self, key: Key):
        self._config['min_key'] = key

    @property
    def max_key(self) -> Key:
        """The key the track is in. Integers map to pitches using standard Pitch Class notation.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            Key: Key
        """
        return self._config['max_key']

    @max_key.setter
    def max_key(self, key: Key):
        self._config['max_key'] = key

    @property
    def target_liveness(self) -> float:
        """Detects the presence of an audience in the recording.
        Higher liveness values represent an increased probability that the track was performed live.
        A value above 0.8 provides strong likelihood that the track is live.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Liveness
        """
        return self._config['target_liveness']

    @target_liveness.setter
    def target_liveness(self, liveness: float):
        if liveness < 0.0 or liveness > 1.0:
            raise ValueError('Liveness must be between 0.0 and 1.0')
        self._config['target_liveness'] = liveness

    @property
    def min_liveness(self) -> float:
        """Detects the presence of an audience in the recording.
        Higher liveness values represent an increased probability that the track was performed live.
        A value above 0.8 provides strong likelihood that the track is live.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Liveness
        """
        return self._config['min_liveness']

    @min_liveness.setter
    def min_liveness(self, liveness: float):
        if liveness < 0.0 or liveness > 1.0:
            raise ValueError('Liveness must be between 0.0 and 1.0')
        self._config['min_liveness'] = liveness

    @property
    def max_liveness(self) -> float:
        """Detects the presence of an audience in the recording.
        Higher liveness values represent an increased probability that the track was performed live.
        A value above 0.8 provides strong likelihood that the track is live.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Liveness
        """
        return self._config['max_liveness']

    @max_liveness.setter
    def max_liveness(self, liveness: float):
        if liveness < 0.0 or liveness > 1.0:
            raise ValueError('Liveness must be between 0.0 and 1.0')
        self._config['max_liveness'] = liveness

    @property
    def target_loudness(self) -> float:
        """The overall loudness of a track in decibels (dB). Loudness values are averaged across
        the entire track and are useful for comparing relative loudness of tracks. Loudness is the
        quality of a sound that is the primary psychological correlate of physical
        strength (amplitude). Values typical range between -60 and 0 db.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Loudness
        """
        return self._config['target_loudness']

    @target_loudness.setter
    def target_loudness(self, loudness: float):
        self._config['target_loudness'] = loudness

    @property
    def min_loudness(self) -> float:
        """The overall loudness of a track in decibels (dB). Loudness values are averaged across
        the entire track and are useful for comparing relative loudness of tracks. Loudness is the
        quality of a sound that is the primary psychological correlate of physical
        strength (amplitude). Values typical range between -60 and 0 db.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Loudness
        """
        return self._config['min_loudness']

    @min_loudness.setter
    def min_loudness(self, loudness: float):
        self._config['min_loudness'] = loudness

    @property
    def max_loudness(self) -> float:
        """The overall loudness of a track in decibels (dB). Loudness values are averaged across
        the entire track and are useful for comparing relative loudness of tracks. Loudness is the
        quality of a sound that is the primary psychological correlate of physical
        strength (amplitude). Values typical range between -60 and 0 db.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Loudness
        """
        return self._config['max_loudness']

    @max_loudness.setter
    def max_loudness(self, loudness: float):
        self._config['max_loudness'] = loudness

    @property
    def target_mode(self) -> Mode:
        """Mode indicates the modality (major or minor) of a track, the type of scale from which its
        melodic content is derived.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            Mode: Mode
        """
        return self._config['target_mode']

    @target_mode.setter
    def target_mode(self, mode: Mode):
        self._config['target_mode'] = mode

    @property
    def min_mode(self) -> Mode:
        """Mode indicates the modality (major or minor) of a track, the type of scale from which its
        melodic content is derived.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            Mode: Mode
        """
        return self._config['min_mode']

    @min_mode.setter
    def min_mode(self, mode: Mode):
        self._config['min_mode'] = mode

    @property
    def max_mode(self) -> Mode:
        """Mode indicates the modality (major or minor) of a track, the type of scale from which its
        melodic content is derived.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            Mode: Mode
        """
        return self._config['max_mode']

    @max_mode.setter
    def max_mode(self, mode: Mode):
        self._config['max_mode'] = mode

    @property
    def target_popularity(self) -> int:
        """The popularity of the track. The value will be between 0 and 100, with 100 being
        the most popular. The popularity is calculated by algorithm and is based, in the most part,
        on the total number of plays the track has had and how recent those plays are.

        Note: When applying track relinking via the market parameter, it is expected to find
        relinked tracks with popularities that do not match min_*, max_*and target_* popularities.
        These relinked tracks are accurate replacements for unplayable tracks with the expected
        popularity scores. Original, non-relinked tracks are available via the linked_from attribute
        of the relinked track response.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            int: Popularity
        """
        return self._config['target_popularity']

    @target_popularity.setter
    def target_popularity(self, popularity: int):
        if popularity < 0 or popularity > 100:
            raise ValueError('Popularity must be between 0 and 100')
        self._config['target_popularity'] = popularity

    @property
    def min_popularity(self) -> int:
        """The popularity of the track. The value will be between 0 and 100, with 100 being
        the most popular. The popularity is calculated by algorithm and is based, in the most part,
        on the total number of plays the track has had and how recent those plays are.

        Note: When applying track relinking via the market parameter, it is expected to find
        relinked tracks with popularities that do not match min_*, max_*and target_* popularities.
        These relinked tracks are accurate replacements for unplayable tracks with the expected
        popularity scores. Original, non-relinked tracks are available via the linked_from attribute
        of the relinked track response.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Popularity
        """
        return self._config['min_popularity']

    @min_popularity.setter
    def min_popularity(self, popularity: int):
        if popularity < 0 or popularity > 100:
            raise ValueError('Popularity must be between 0 and 100')
        self._config['min_popularity'] = popularity

    @property
    def max_popularity(self) -> int:
        """The popularity of the track. The value will be between 0 and 100, with 100 being
        the most popular. The popularity is calculated by algorithm and is based, in the most part,
        on the total number of plays the track has had and how recent those plays are.

        Note: When applying track relinking via the market parameter, it is expected to find
        relinked tracks with popularities that do not match min_*, max_*and target_* popularities.
        These relinked tracks are accurate replacements for unplayable tracks with the expected
        popularity scores. Original, non-relinked tracks are available via the linked_from attribute
        of the relinked track response.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Popularity
        """
        return self._config['max_popularity']

    @max_popularity.setter
    def max_popularity(self, popularity: int):
        if popularity < 0 or popularity > 100:
            raise ValueError('Popularity must be between 0 and 100')
        self._config['max_popularity'] = popularity

    @property
    def target_speechiness(self) -> float:
        """Speechiness detects the presence of spoken words in a track. The more exclusively
        speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the
        attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken
        words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech,
        either in sections or layered, including such cases as rap music. Values below 0.33 most
        likely represent music and other non-speech-like tracks.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Speechiness
        """
        return self._config['target_speechiness']

    @target_speechiness.setter
    def target_speechiness(self, speechiness: float):
        if speechiness < 0.0 or speechiness > 1.0:
            raise ValueError('Speechiness must be between 0.0 and 1.0')
        self._config['target_speechiness'] = speechiness

    @property
    def min_speechiness(self) -> float:
        """Speechiness detects the presence of spoken words in a track. The more exclusively
        speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the
        attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken
        words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech,
        either in sections or layered, including such cases as rap music. Values below 0.33 most
        likely represent music and other non-speech-like tracks.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Speechiness
        """
        return self._config['min_speechiness']

    @min_speechiness.setter
    def min_speechiness(self, speechiness: float):
        if speechiness < 0.0 or speechiness > 1.0:
            raise ValueError('Speechiness must be between 0.0 and 1.0')
        self._config['min_speechiness'] = speechiness

    @property
    def max_speechiness(self) -> float:
        """Speechiness detects the presence of spoken words in a track. The more exclusively
        speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the
        attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken
        words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech,
        either in sections or layered, including such cases as rap music. Values below 0.33 most
        likely represent music and other non-speech-like tracks.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Speechiness
        """
        return self._config['max_speechiness']

    @max_speechiness.setter
    def max_speechiness(self, speechiness: float):
        if speechiness < 0.0 or speechiness > 1.0:
            raise ValueError('Speechiness must be between 0.0 and 1.0')
        self._config['max_speechiness'] = speechiness

    @property
    def target_tempo(self) -> float:
        """The overall estimated tempo of a track in beats per minute (BPM). In musical terminology,
        tempo is the speed or pace of a given piece and derives directly from the average beat
        duration.

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Tempo
        """
        return self._config['target_tempo']

    @target_tempo.setter
    def target_tempo(self, tempo: float):
        self._config['target_tempo'] = tempo

    @property
    def min_tempo(self) -> float:
        """The overall estimated tempo of a track in beats per minute (BPM). In musical terminology,
        tempo is the speed or pace of a given piece and derives directly from the average beat
        duration.

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Tempo
        """
        return self._config['min_tempo']

    @min_tempo.setter
    def min_tempo(self, tempo: float):
        self._config['min_tempo'] = tempo

    @property
    def max_tempo(self) -> float:
        """The overall estimated tempo of a track in beats per minute (BPM). In musical terminology,
        tempo is the speed or pace of a given piece and derives directly from the average beat
        duration.

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Tempo
        """
        return self._config['max_tempo']

    @max_tempo.setter
    def max_tempo(self, tempo: float):
        self._config['max_tempo'] = tempo

    @property
    def target_time_signature(self) -> int:
        """An estimated overall time signature of a track. The time signature (meter) is a notational
        convention to specify how many beats are in each bar (or measure).

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            int: Time Signature
        """
        return self._config['target_time_signature']

    @target_time_signature.setter
    def target_time_signature(self, time_signature: int):
        self._config['target_time_signature'] = time_signature

    @property
    def min_time_signature(self) -> int:
        """An estimated overall time signature of a track. The time signature (meter) is a notational
        convention to specify how many beats are in each bar (or measure).

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Time Signature
        """
        return self._config['min_time_signature']

    @min_time_signature.setter
    def min_time_signature(self, time_signature: int):
        self._config['min_time_signature'] = time_signature

    @property
    def max_time_signature(self) -> int:
        """An estimated overall time signature of a track. The time signature (meter) is a notational
        convention to specify how many beats are in each bar (or measure).

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            int: Time Signature
        """
        return self._config['max_time_signature']

    @max_time_signature.setter
    def max_time_signature(self, time_signature: int):
        self._config['max_time_signature'] = time_signature

    @property
    def target_valence(self) -> float:
        """A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
        Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks
        with low valence sound more negative (e.g. sad, depressed, angry).

        For each of the tunable track attributes (below) a target value may be provided.
        Tracks with the attribute values nearest to the target values will be preferred.
        All target values will be weighed equally in ranking results.

        Returns:
            float: Valence
        """
        return self._config['target_valence']

    @target_valence.setter
    def target_valence(self, valence: float):
        if valence < 0.0 or valence > 1.0:
            raise ValueError('Valence must be between 0.0 and 1.0')
        self._config['target_valence'] = valence

    @property
    def min_valence(self) -> float:
        """A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
        Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks
        with low valence sound more negative (e.g. sad, depressed, angry).

        For each tunable track attribute, a hard floor on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Valence
        """
        return self._config['min_valence']

    @min_valence.setter
    def min_valence(self, valence: float):
        if valence < 0.0 or valence > 1.0:
            raise ValueError('Valence must be between 0.0 and 1.0')
        self._config['min_valence'] = valence

    @property
    def max_valence(self) -> float:
        """A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
        Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks
        with low valence sound more negative (e.g. sad, depressed, angry).

        For each tunable track attribute, a hard ceiling on the selected track attribute’s value
        can be provided. See tunable track attributes below for the list of available options.

        Returns:
            float: Valence
        """
        return self._config['max_valence']

    @max_valence.setter
    def max_valence(self, valence: float):
        if valence < 0.0 or valence > 1.0:
            raise ValueError('Valence must be between 0.0 and 1.0')
        self._config['max_valence'] = valence
