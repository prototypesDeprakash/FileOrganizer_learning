# TidyDir

A lightweight desktop file organizer built with **Python** and **CustomTkinter**.

TidyDir helps you clean up cluttered folders by automatically organizing files based on their extensions. Simply select a directory, and TidyDir will scan it, create category folders, and move each file into its appropriate location.

---

## Features

- Browse and select any directory
- Automatically scan all files
- Categorize files by extension
- Create folders for each file category
- Move files into their corresponding folders
- Live terminal-style status output
- Organization summary after completion
- Clean cyber-terminal inspired interface

---

## How It Works

### 1. Select a Directory

Choose the folder you want to organize.

<img width="790" height="630" alt="Directory Selection" src="https://github.com/user-attachments/assets/cfdd5d75-3e28-4d9f-ab93-0bb3191b55a3" />

---

### 2. Scan Files

TidyDir scans the selected directory and groups files by their extensions.

Example:

```python
{
    "jpg": ["photo1.jpg", "photo2.jpg"],
    "pdf": ["notes.pdf", "resume.pdf"],
    "mp3": ["song.mp3"]
}
```

---

### 3. Create Category Folders

A folder is created for every detected file category.

Example:

```
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Audio/
├── Archives/
└── Others/
```

---

### 4. Organize Files

Files are moved into their respective folders while the application displays real-time progress.

<img width="989" height="505" alt="image" src="https://github.com/user-attachments/assets/1dd8f9e8-abfb-4f8d-9926-2a60e0228032" />

---

## Project Structure

```
TidyDir/
│
├── main.py
├── scanner.py
├── categorizer.py
├── folder_manager.py
├── mover.py
├── helper.py
└── ui.py
```

| Module | Responsibility |
|---------|----------------|
| `main.py` | Starts the application |
| `scanner.py` | Scans the selected directory |
| `categorizer.py` | Groups files by extension |
| `folder_manager.py` | Creates destination folders |
| `mover.py` | Moves files into folders |
| `helper.py` | Utility functions |
| `ui.py` | CustomTkinter user interface |

---

## Screenshots

### Main Window

<img width="800" height="628" alt="Main Window" src="https://github.com/user-attachments/assets/56d6f747-8cc0-4a59-90be-fe877fc58eef" />

### Before Organization 

<img width="762" height="537" alt="Status Window" src="https://github.com/user-attachments/assets/3d051dcb-ea0f-4f32-ad72-3a2a639cc737" />

<img width="798" height="855" alt="Summary" src="https://github.com/user-attachments/assets/09a04f79-ed55-4b8b-badd-837d4dc8177c" />

<img width="791" height="892" alt="Summary Details" src="https://github.com/user-attachments/assets/43442dfa-27e5-4e3a-8dcd-cb3832c0cdf2" />

<img width="803" height="848" alt="Result" src="https://github.com/user-attachments/assets/bb0f75a6-73c1-4d06-8991-18617f8fb608" />

### Organized Folder


<img width="989" height="505" alt="image" src="https://github.com/user-attachments/assets/1dd8f9e8-abfb-4f8d-9926-2a60e0228032" />


---

## Technologies Used

- Python 3
- CustomTkinter
- Tkinter
- os
- shutil

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/TidyDir.git
```

Go to the project folder:

```bash
cd TidyDir
```

Install dependencies:

```bash
pip install customtkinter
```

Run the application:

```bash
python main.py
```

---

## Roadmap

- [ ] Undo last organization
- [ ] Duplicate file detection
- [ ] Drag-and-drop support
- [ ] Custom organization rules
- [ ] Progress bar
- [ ] Export summary report
- [ ] User preferences
- [ ] Additional themes

---

## License

This project is licensed under the MIT License.
