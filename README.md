# Subtitle Encoding Fixer

A simple Python application with a graphical user interface (GUI) to fix encoding issues in subtitle files. It converts subtitles from `Windows-1256` (or similar) to `UTF-8` encoding for better compatibility.

---

## Features

- Supports common subtitle file types: `.srt`, `.txt`, `.sub`, `.ass`, `.ssa`, `.vtt`.
- Automatically generates a fixed file with `_fixed` appended to the original file name.
- Intuitive and user-friendly GUI using `tkinter`.
- Handles errors gracefully with alerts for invalid input or processing issues.

---

## How It Works

1. Launch the application.
2. Click **Browse** to select a subtitle file with encoding issues.
3. The application will automatically save a fixed version of the file in the same directory, with `_fixed` added to its name.

**Example:**
- Input: `movie.srt`
- Output: `movie_fixed.srt`

---

## Prerequisites

Make sure you have **Python 3.6+** installed on your system.

Install required libraries (if necessary):
```bash
pip install tkinter
```

> **Note:** `tkinter` is typically included with Python by default. If it’s missing, you may need to install it manually.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ZaikOSS/SubtitleEncodingFixer.git
   cd SubtitleEncodingFixer
   ```

2. Run the script:
   ```bash
   python SubtitleEncodingFixer.py
   ```

---

## Screenshots

**Main Interface:**

![image](https://github.com/user-attachments/assets/d2b65858-f34e-4e56-a003-a380489fb29d)

![image](https://github.com/user-attachments/assets/1964b596-3adb-4493-bc24-3d7a07f9478a)


---

## File Structure

```
SubtitleEncodingFixer/
|
├── SubtitleEncodingFixer.py   # Main script
├── README.md                  # Project documentation
```

---

## Contributing

Contributions are welcome! If you have suggestions or find bugs, feel free to open an issue or submit a pull request.

---



