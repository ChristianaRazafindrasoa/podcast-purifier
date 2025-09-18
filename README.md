# 🎧 Podcast Purifier

A tool to automatically identify and classify advertisement segments in podcast transcripts using AI.

## ✨ Features

- 🎯 Classifies podcast segments as either advertisements or content
- 🤖 Uses zero-shot classification with BART model
- 📝 Processes Whisper transcription output

## 📋 Requirements

- transformers
- whisper
- pydub
- json

## Usage

1. Ensure you have a Whisper output file named `whisper_output_example.json`
2. Run the segment classifier:
   ```bash
   python segment_classifier.py
   ```

The tool will identify advertisement segments and store their IDs for removal or skipping.