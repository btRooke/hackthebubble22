#!/usr/bin/env python3

import sys
import sounddevice

from mdp.encoding.encode import encode
from mdp.music.frequencies import note_frequency
from mdp.synthesis.synth import simple_play_notes

data = sys.stdin.buffer.read()

encoded = encode(data)

print(f"Playing {len(encoded)} notes...")

print(encoded)
print([note_frequency(note, 5) for note in encoded])

simple_play_notes(encoded, 0.3, 0.15)

print("Done!")