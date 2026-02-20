import whisper
import json 
import os


model = whisper.load_model("large-v2")

audios = os.listdir("audios")

for audio in audios:
    if ("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        result = model.transcribe(
            audio = f"audios/{audio}",
            language = "hi",
            task = "translate"
        )

        chunks = []
        segments = result["segments"]
        
        for segment in segments:
            chunks.append({
                "video_number" : number,
                "title": title,
                "start" : segment["start"],
                "end" : segment["end"],
                "text" : segment["text"]
            })

        chunks_of_metadata = {
            "chunks" : chunks,
            "text" : result["text"]
        }

        with open(f"jsons/{number}_{title}.json", "w") as f:
            json.dump(chunks_of_metadata, f)
