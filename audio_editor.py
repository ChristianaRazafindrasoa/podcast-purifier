from pydub import AudioSegment
from segment_classifier import ads
import json

audio = AudioSegment.from_file("samples/original_podcast.mp3")
timestamps = []

with open("samples/whisper_output_example.json", "r") as f:
    segments = json.load(f)["segments"]

for segment in segments:
    timestamps.append([segment["start"], segment["end"]])

trimmed = audio[0:0]

for i in range(len(timestamps)):
    if i not in ads:
        start = timestamps[i][0] * 1000
        end = timestamps[i][1] * 1000
        trimmed += audio[start:end]

trimmed.export("samples/trimmed_podcast.mp3", format="mp3")
print("Podcast purified!")