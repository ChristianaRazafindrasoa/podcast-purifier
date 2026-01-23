import whisper
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model("tiny.en")
result = model.transcribe("/original_podcast.mp3")

with open("samples/whisper_output_example.json", "w") as f:
    json.dump(result, f)