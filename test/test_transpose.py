import unittest

from encoding.encode import encode, to_base_12, decode
from music.frequencies import octave_range, shift_frequency_to_octave
from mdp.music.notes import Note
from music.transposition import transpose_note


class TranspositionTest(unittest.TestCase):

    def test_transpose(self):
        self.assertEqual(transpose_note(Note.D, Note.Bb), Note.C)
        self.assertEqual(transpose_note(Note.C, Note.F), Note.F)
