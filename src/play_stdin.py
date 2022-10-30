#!/usr/bin/env python3

import sys
import sounddevice

from mdp.encoding.encode import encode
from mdp.music.frequencies import note_frequency
from mdp.music.notes import Note
from mdp.synthesis.synth import simple_play_notes

data = sys.stdin.buffer.read()

encoded = encode(data)

print(f"Playing {len(encoded)} notes...")

simple_play_notes(encoded, 0.4, 0.3)

print("Done!")