import os
import subprocess

files = os.listdir("videos")

for file in files:
    # print(file)
    tutorial_num = file.split("-_Tutorial_")[1].split("_")[0]
    filename = file.split("_Sigma_")[0].replace("_", " ")
    print(tutorial_num, filename)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_num}_{filename}.mp3"])



