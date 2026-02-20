# How to use RAG AI Teaching Assistant on your own data?

## STEP 1: Collect your Videos

Move all your video files to videos folder

## STEP 2: Convert videos to mp3

Install ffmpeg.exe for converting videos to audios

ffmpeg for Windows:
https://github.com/BtbN/FFmpeg-Builds/releases

Convert all your video files to mp3 by running videos_to_mp3.py

## STEP 3: Convert mp3 to json

Inorder to create the text chunks of the video lecture, user openAI Whisper model
https://github.com/openai/whisper/blob/main/README.md

Install openAI Whisper model:
pip install -U openai-whisper

Convert all mp3 files to json by running mp3_to_json.py

## STEP 4 - Convert json files to Vectors

Download Ollama:
https://ollama.com/download

Download an Embedding model:

cmd --> ollama pull bge-m3
https://ollama.com/library/nomic-embed-text

Use bge-m3 or nomic-embed-text
It converts text into vectors (numbers).

Use the file preprocess_json.py to convert json files to a dataframe of Vectors(Embeddings) and save it as a joblib pickle (embeddings.joblib)

## STEP 5 - Prompt generation and feeding to the LLM

Download an LLM model of your choice.
https://ollama.com/library/llama3.1
cmd --> ollama run llama3.1

Read the joblib file and load it to the memory.
Then, create a relavent prompt as per the user query and feed it to the LLM.
