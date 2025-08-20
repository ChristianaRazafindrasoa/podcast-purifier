import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model("tiny.en")
result = model.transcribe("/Users/christiana/Desktop/project/audio/ted_tech_phone_batteries.mp3")

timestamps = []
texts = []

for segment in result["segments"]:
    timestamps.append(segment["end"])
    texts.append(segment["text"])

print(timestamps)
print(texts)