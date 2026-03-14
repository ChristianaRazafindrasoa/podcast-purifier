import whisper
import json

model = whisper.load_model("tiny.en")
result = model.transcribe("samples/original_podcast.mp3")

with open("samples/whisper_output_example.json", "w") as f:
    json.dump(result, f)