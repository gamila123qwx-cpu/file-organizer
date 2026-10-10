import os
import shutil

FOLDER = input("Enter the folder path: ").strip('"')

TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

for name in os.listdir(FOLDER):
    path = os.path.join(FOLDER, name)
    if not os.path.isfile(path):
        continue

    ext = os.path.splitext(name)[1].lower()

    target = "Others"
    for folder, exts in TYPES.items():
        if ext in exts:
            target = folder
            break

    dest = os.path.join(FOLDER, target)
    os.makedirs(dest, exist_ok=True)
    new_path = os.path.join(dest, name)
    shutil.move(path, new_path)
    print(f"Moved {name} -> {new_path}")

os.startfile(FOLDER)