# File Organizer

A simple Python script that cleans up a messy folder by sorting its files into subfolders based on file type (Images, Documents, Videos, and so on).

## Features

- Asks for a folder path and organizes every file inside it
- Sorts files by extension into category folders
- Sends unknown file types to an `Others` folder
- Creates the category folders automatically when needed
- Prints where each file was moved
- Opens the organized folder when it finishes (Windows)

## File Categories

| Folder      | Extensions                      |
|-------------|---------------------------------|
| `Images`    | .jpg, .jpeg, .png, .gif         |
| `Documents` | .pdf, .docx, .txt, .xlsx        |
| `Videos`    | .mp4, .mkv, .mov                |
| `Audio`     | .mp3, .wav                      |
| `Archives`  | .zip, .rar                      |
| `Others`    | anything else                   |

## Requirements

- Python 3.x
- No external libraries (uses only `os` and `shutil`)

## How to Use

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the script:

   ```bash
   python organizer.py
   ```

4. When asked, paste the full path of the folder you want to organize:

   ```
   Enter the folder path: C:\Users\user\Desktop\test
   ```

5. The script moves the files and prints what it did:

   ```
   Moved Book3.xlsx -> C:\Users\user\Desktop\test\Documents\Book3.xlsx
   Moved photo.jpg -> C:\Users\user\Desktop\test\Images\photo.jpg
   ```

## Example

**Before**

```
test/
├── Book3.xlsx
├── photo.jpg
├── notes.pdf
└── Canva.lnk
```

**After**

```
test/
├── Documents/
│   ├── Book3.xlsx
│   └── notes.pdf
├── Images/
│   └── photo.jpg
└── Others/
    └── Canva.lnk
```

## Important Notes

- The script **moves** files, it does not copy them. Try it on a test folder first.
- It only organizes files directly inside the folder you give it. Existing subfolders are skipped.
- `os.startfile()` works on Windows only. Remove the last line of the script if you use macOS or Linux.

## How It Works

1. Reads every item in the folder with `os.listdir()`.
2. Skips anything that is not a file.
3. Gets the file extension with `os.path.splitext()`.
4. Looks the extension up in the `TYPES` dictionary (defaults to `Others`).
5. Creates the destination folder if it does not exist and moves the file with `shutil.move()`.

## Ideas for Improvement

- Add a dry-run mode that shows what would move without moving anything
- Handle duplicate file names so nothing gets overwritten
- Let the user add their own categories
- Add a simple GUI to choose the folder

## Author

Built by gamila as a python practice project.
