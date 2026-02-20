import numpy as np 
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests


def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "nomic-embed-text",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    return response

df = joblib.load("embeddings.joblib")


incoming_query = input("Ask a question: ")
query_embedding = create_embedding(incoming_query)[0]

# cosine_similarity function takes 2D arrays as an input
# np.vstack --> stacks arrays on top of each other (row-wise).
similarities = cosine_similarity(np.vstack(df["embedding"]), [query_embedding]).flatten()
# print(similarities)
top_results = 5
max_idx = similarities.argsort()[::-1][0:top_results]
# print(max_idx)

new_df = df.loc[max_idx]
# print(new_df[["video_number", "title", "text"]])

prompt = f''' I am teaching Web Development using Sigma Web Development course. Here are the video subtitle video chunks which contains the video number, video title, start time in seconds, end time in seconds, text at that timestamp.

{new_df[["video_number", "title", "start", "end", "text"]].to_json(orient= "records")}
--------------------------------------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer where and how much content is taught (in which video and at what timestamp, timestamp should not be in this form --> 275.5 seconds it should be converted to minutes and seconds and should be shown as for example: 4 minutes 58 secs or 4:58s) and guide the user to go to that particular video.
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)
