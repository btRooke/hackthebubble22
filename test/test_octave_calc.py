import unittest

from music.frequencies import octave_range, shift_frequency_to_octave


class FrequencyTests(unittest.TestCase):

    def test_octave_calc(self):
        low, high = octave_range(3)
        self.assertEqual(round(low, 2), 127.14)
        self.assertEqual(round(high, 2), 269.40)

    def test_octave_shift(self):
        shifted = shift_frequency_to_octave(739.99, 3)
        self.assertEqual(round(shifted, 2), 185.00)
