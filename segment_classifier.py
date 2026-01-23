from transformers import pipeline
import json

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

with open("samples/whisper_output_example.json", 'r') as f:
    data = json.load(f)

labels = ["commercial advertisement sponsor promotion", "podcast educational content"]
ads = []

for segment in data["segments"]:
    text = f" Classify this segment: {segment['text']}"
    result = classifier(text, labels)
    classification = "ad segment" if result["labels"][0] == "commercial advertisement sponsor promotion" else "content segment"
    
    if classification == "ad segment":
        ads.append(segment["id"])