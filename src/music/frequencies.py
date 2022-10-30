from music.notes import Note

# tuning config

fundamental: Note = Note.A
fundamental_octave = 4
fundamental_frequency: float = 440.0  # 440Hz tuning


def octave_range(n: int) -> (float, float):
    """
    Get the range frequencies in an octave.

    :param n: Octave index.
    :return: Tuple of (low, high).
    """

    octave_shift = 12 * (n - fundamental_octave)

    b_low = offset_frequency(-10 + octave_shift)
    c_low = offset_frequency(-9 + octave_shift)

    b_high = offset_frequency(3 + octave_shift)
    c_high = offset_frequency(4 + octave_shift)

    return (b_low + c_low) / 2, (c_high + b_high) / 2


def shift_frequency_to_octave(f: float, n: int) -> float:
    """
    Shift a frequency from some unknown octave to a given one.

    :param f: The frequency to shift.
    :param n: The octave index to shift to.
    :return: The shifted frequency.
    """

    low, high = octave_range(n)

    shifted_f = f

    while not (low <= shifted_f < high):

        if shifted_f < low:
            shifted_f *= 2
        else:
            shifted_f /= 2

    return shifted_f


def offset_frequency(n: float) -> float:
    """
    Compute note frequency as semitones from the fundamental (A).

    See https://pages.mtu.edu/~suits/NoteFreqCalcs.html.

    :param n: Semitones from fundamental.
    :param f0: Fundamental frequency.
    :return: Frequency of n from f0.
    """

    a = 2 ** (1 / 12)
    return fundamental_frequency * (a ** n)
