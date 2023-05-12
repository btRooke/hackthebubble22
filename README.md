# Musical "Datagram" Protocol

Built with [@Sean-AP](https://github.com/Sean-AP/) in under 12 hours for Hack the Bubble 2022.

Data link/ physical layer protocol to send and receive arbitrary data using the 12 notes of the Western musical scale.

We came 2nd place overall!

## Encoding

To keep things simple we just used the 12 named notes in the Western musical scale (C, Db, D ... B) as our _symbols_ for transmission.

If we say that C = 0, Db = 1 and so forth, we've just got a base 12 number system, which we can easily translate bytes to.

An issue is that a byte can hold $2^8=256$ values and so this requires at least 3 symbols in base 12 to hold. To demonstrate, $12^2=144$ is too low, $12^3=1728$ is enough.

This means, however, that only $\frac{256}{1728}=0.148$ of the available _"encoding space"_ in the base 12 system will ever be used.

We attempted to combat this by sending batches of bytes; 4 bytes fits fine into 9 notes - $2^{(8\times4)} = 4294967296 \simeq 5159780352 = 12^9$.

This way we're using $\frac{4294967296}{5159780352} = 0.832$ of our encoding space. More intuitively, this means we get 9 notes for 4 bytes vs 12 notes for 4 bytes in the old system.

This of course means:
- Non-aligned data must be padded
- A single corrupted note transmission out of 9 will
  corrupt the entire datagram
- This is not particularly ideal and it might be worth 
  investigating a simplified (3 notes = 1 byte) version
  for stability
- Definitely worth investing some time into ECC in the
  unused $\sim0.17$ of each datagram
- Could add a timestamp or addressing information as well

**TLDR:** We send data in batches (datagrams) of 4 bytes for efficiency, this requires 9 notes. It can cause some reliability issues.

## Decoding

A fourier transform is performed many times a second to identify the _most prominent_ frequency being played at the current moment in time.

This frequency is then shifted to the correct octave and the closest note is found.

This can then be but into a buffer until 9 notes are detected for decoding.

## Scripts

- `stdin_notes.py` - Tells you the notes for arbitrary data on standard input, you might wish to play these on an instrument of your choice.
- `play_stdin.py` - Plays the bytes as notes synthesized by Python, this is the only way we got it to work.
- `listen.py` - Will listen to the notes and print our any bytes it detects.

Example `stdin_notes` run:
```
$ echo "Hello, World!" | python stdin_notes.py 
---------------------
🎵 "stdin" sonata 🎵
---------------------
D     A     Bb    A     D     
A     D     B     Ab    E     
E     C     G     Ab    C     
G     Ab    G     E     E     
D     D     D     D     
Ab    Ab    E     Db    
Eb    F     G     G     
F     F     A     E     
```

## Future

- Add metadata to the datagrams
  - Timestamps
  - Addressing
  - Metadata
- Variable length datagrams
- Create an actual network interface to send real data over via MDP
- Chords for better bandwidth
- Actually make the music sound good?
