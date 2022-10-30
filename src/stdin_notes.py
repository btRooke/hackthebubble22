#!/usr/bin/env python3

import sys

import numpy as np

from mdp.encoding.encode import encode
from mdp.music.notes import Note

data = sys.stdin.buffer.read()

encoded = encode(data)

print("---------------------")
print("""🎵 "stdin" sonata 🎵""")
print("---------------------")

lines = np.array_split(encoded, 8)

for line in lines:

    for note in line:

        print(str(Note(note)).ljust(5), end=" ")

    print("")