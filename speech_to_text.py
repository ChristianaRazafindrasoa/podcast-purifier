import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model("tiny.en")
result = model.transcribe("/original_podcast.mp3")

timestamps = []
texts = []

for segment in result["segments"]:
    timestamps.append(segment["end"])
    texts.append(segment["text"])

print(timestamps)
print(texts)