from math import ceil

from typing import List

from mdp.music.notes import Note

notes_in_scale = 12


def from_base_12(unit_values):
    result = 0

    for i in range(0, len(unit_values)):
        result += unit_values[-1 - i] * notes_in_scale ** i

    return result


def to_base_12(integer, padding=0) -> List[Note]:

    result = []

    while integer:
        result.insert(0, integer % notes_in_scale)
        integer //= notes_in_scale

    while len(result) < padding:
        result.insert(0, 0)

    return result


def encode_qword(qword: bytes) -> List[Note]:
    assert len(qword) == 4
    value = int.from_bytes(qword, "big")
    return list(map(lambda v: Note(v), to_base_12(value, 9)))


def decode_nnote(nnote: List[Note]) -> bytes:
    assert len(nnote) == 9
    value = from_base_12(nnote)
    return int.to_bytes(value, 4, "big")


def encode(data: bytes) -> List[Note]:
    qwords_required = ceil(len(data) / 4)
    padding_required = qwords_required * 4 - len(data)

    data += bytes([0 for _ in range(padding_required)])

    notes = []

    for i in range(0, len(data), 4):
        notes += encode_qword(data[i:i + 4])

    return notes


def decode(data: List[Note]) -> bytes:

    assert len(data) % 9 == 0

    decoded = bytes([])

    for i in range(0, len(data), 9):
        decoded += decode_nnote(data[i:i + 9])

    return decoded
