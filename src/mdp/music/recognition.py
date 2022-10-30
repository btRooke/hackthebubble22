import numpy as np
from numpy import ndarray

from music.frequencies import offset_frequency, fundamental, shift_frequency_to_octave, fundamental_octave
from mdp.music.notes import Note

fundamental_octave_frequencies = [offset_frequency(i - int(fundamental)) for i in range(12)]


def closest_index(f: float, octave_frequencies: list[float]) -> int:
    octave_differences = [abs(v - f) for v in octave_frequencies]
    index_min = np.argmin(octave_differences)
    return index_min  # might be multiple, probably not!


def note_from_frequency(f: float) -> Note:

    """
    Given a frequency, return the closest note.

    Any octave.

    :param f: A frequency.
    :return: The closest note.
    """

    shifted_f = shift_frequency_to_octave(f, fundamental_octave)
    closest_note_index = closest_index(shifted_f, fundamental_octave_frequencies)
    return Note(closest_note_index)
