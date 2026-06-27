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

melody = ["C5", "D5", "E5", "G5", "E5", "D5", "C5", "G4"]

for pitch in melody:
    right.append(note.Note(pitch, quarterLength=1))

chords = [
    ["C3", "E3", "G3"],
    ["G2", "B2", "D3"],
    ["A2", "C3", "E3"],
    ["F2", "A2", "C3"],
]

for c in chords * 2:
    left.append(chord.Chord(c, quarterLength=2))

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


