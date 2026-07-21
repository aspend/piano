import random
import subprocess
import sys
from music21 import stream, note, chord, meter, key, tempo, instrument

open_score = "--open" in sys.argv

score = stream.Score()
score.append(tempo.MetronomeMark(number=90))
score.append(key.Key("C"))
score.append(meter.TimeSignature("4/4"))

right = stream.Part()
right.insert(0, instrument.Piano())

left = stream.Part()
left.insert(0, instrument.Piano())

scale = ["C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6"]

chord_tones_by_bar = [
    ["C5", "E5", "G5"],
    ["G5", "B5", "D5"],
    ["A5", "C5", "E5"],
    ["F5", "A5", "C5"],
]

def make_melody_bar(chord_tones):
    bar = []

    for beat in range(4):
        # Strong beats should usually be chord tones
        if beat == 0 or beat == 2:
            pitch = random.choice(chord_tones)
        else:
            pitch = random.choice(scale)

        bar.append(note.Note(pitch, quarterLength=1))

    return bar

for chord_tones in chord_tones_by_bar * 4:
    for n in make_melody_bar(chord_tones):
        right.append(n)

chords = [
    ["C3", "E3", "G3"],
    ["G2", "B2", "D3"],
    ["A2", "C3", "E3"],
    ["F2", "A2", "C3"],
]

for c in chords * 4:
    root = c[0]
    third = c[1]
    fifth = c[2]

    left.append(note.Note(root, quarterLength=1))
    left.append(note.Note(fifth, quarterLength=1))
    left.append(note.Note(third, quarterLength=1))
    left.append(note.Note(fifth, quarterLength=1))

score.insert(0, right)
score.insert(0, left)

score.write("musicxml", fp="piano_piece.musicxml")
score.write("midi", fp="piano_piece.mid")

print("Done! Created piano_piece.musicxml and piano_piece.mid")

if open_score:
    subprocess.run([
        "open",
        "-a",
        "MuseScore 4",
        "piano_piece.musicxml"
    ])


