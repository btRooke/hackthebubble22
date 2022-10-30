#!/usr/bin/env python3

import sys
import sounddevice

from mdp.encoding.encode import encode
from mdp.synthesis.synth import simple_play_notes

data = sys.stdin.buffer.read()

if len(data) == 0:
    print(f"Usage: {sys.argv[0]} < <file to play>")

encoded = encode(data)
print(f"Playing {len(encoded)} notes...")
simple_play_notes(encoded)
print("Done!")