import os
import shutil

files = [f for f in os.listdir(".") if f.endswith(".png")]

for file in files:
    folder_path = file[0]

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    shutil.move(file, f"{folder_path}/{file}")

folders = [f for f in os.listdir(".") if os.path.isdir(f) and len(f) == 1]


for folder in folders:
    shutil.move(folder, f"alphabets/{folder}")