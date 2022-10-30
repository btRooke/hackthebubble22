#!/usr/bin/env python3
import pyaudio
from ..logic import listener, translater

# Set up stream and translater
(audio, stream) = listener.create_stream(pyaudio.paInt16, 44100)

t = translater.Translater(44100, 2048)


listener.listen(stream, t)