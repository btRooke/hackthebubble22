#!/usr/bin/env python3
import sounddevice
import pyaudio
from mdp.logic import listener
from mdp.logic import translater
from mdp.music import recognition
from mdp.encoding.encode import decode

# Set up stream and translater
(audio, stream) = listener.create_stream(pyaudio.paInt16, 44100)

t = translater.Translater(44100, 2048)

frequencies = []

print("Listening...")

while True:

    frequencies.append(next(listener.listen(stream, t)))

    if len(frequencies) < 9:
        continue

    print(frequencies)

    notes = list([recognition.note_from_frequency(x) for x in frequencies])
    print(notes)

    char = decode(notes)
    print(char)
    
    frequencies.clear()