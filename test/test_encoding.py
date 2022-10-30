import unittest

from encoding.encode import encode, to_base_12, decode
from music.frequencies import octave_range, shift_frequency_to_octave


class EncodingTest(unittest.TestCase):

    def test_encode(self):

        to_send = "Hello, world!".encode()

        notes = encode(to_send)

        print(decode(notes))
