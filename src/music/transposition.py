from encoding.encode import notes_in_scale
from music.notes import Note


def transpose_note(note: Note, key: Note):
    difference = int(key) - int(Note.C)
    return Note((int(note) + difference) % notes_in_scale)


def transpose_notes(notes: list[Note], key: Note):
    return [transpose_note(n, key) for n in notes]
