import pyaudio
import numpy as np

from mdp.music.frequencies import note_frequency
from mdp.music.notes import Note

# thanks to https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python

pyaudio_obj = pyaudio.PyAudio()
sample_rate = 44100


def sine_wave_signal(duration, frequency):
    return np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)


def to_bytes(signal, volume):
    return (volume * signal.astype(np.float32)).tobytes()


def sine_wave_bytes(duration, frequency, volume):
    return to_bytes(sine_wave_signal(duration, frequency), volume)


def play_note(frequency, duration, volume):
    bytes = sine_wave_bytes(duration, frequency, volume)

    output_stream = pyaudio_obj.open(format=pyaudio.paFloat32,
                                     channels=1,
                                     rate=sample_rate,
                                     output=True)

    output_stream.write(bytes)
    output_stream.stop_stream()
    output_stream.close()


def play_notes(notes, durations, breaks):

    notes_bytes = []

    for i in range(len(notes)):

        note = notes[i]
        duration = durations[i]
        note_break = breaks[i]

        if i == 0:
            duration = 1.2

        signal = sine_wave_signal(duration, note_frequency(note, 6))
        notes_bytes.append(to_bytes(signal, 0.5))

        signal = sine_wave_signal(note_break, note_frequency(note, 6))
        notes_bytes.append(to_bytes(signal, 0))

    output_stream = pyaudio_obj.open(format=pyaudio.paFloat32,
                                     channels=1,
                                     rate=sample_rate,
                                     output=True)

    for note_bytes in notes_bytes:
        output_stream.write(note_bytes)

    output_stream.stop_stream()
    output_stream.close()


def simple_play_notes(notes, duration=0.25, note_break=0.1):

    play_notes(
        notes,
        [duration for _ in range(len(notes))],
        [note_break for _ in range(len(notes))]
    )

