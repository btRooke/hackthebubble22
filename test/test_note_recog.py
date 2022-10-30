import unittest

from mdp.music.notes import Note
from music.recognition import note_from_frequency


class RecogTests(unittest.TestCase):

    def test_octave_calc(self):
        self.assertEqual(note_from_frequency(440), Note.A)
        self.assertEqual(note_from_frequency(369.99), Note.Gb)
        self.assertEqual(note_from_frequency(2217.46), Note.Db)
        self.assertEqual(note_from_frequency(2222.33), Note.Db)  # high oct
        self.assertEqual(note_from_frequency(87.31), Note.F)  # low oct
