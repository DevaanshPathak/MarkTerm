# 📝 MarkTerm

**MarkTerm** is a simple terminal-based Markdown notes manager built with Python.  
It helps you quickly create, edit, read, search, and organize notes right from your terminal — all stored as `.md` files.

---

## ⚡ Features

- 🆕 Create new notes (Markdown format)
- 📜 Read notes beautifully rendered in the terminal using [`rich`](https://github.com/Textualize/rich)
- 🗂 List and organize notes in folders
- 🔎 Search notes by title or content
- 📝 Edit notes in your favorite `$EDITOR` (e.g., `vim`, `nano`, `code`)
- ❌ Delete notes easily
- 📦 Backup all notes to timestamped zip files
- 🔁 Restore notes from any backup
- 📁 Tag/folder support through subdirectories inside `notes/`
- 💻 Simple CLI interface using `argparse`

---

## 🛠 Requirements

- Python 3.7+
- `rich` library (install via pip)

```bash
pip install rich
````

---

## 🚀 Usage

### 1. Create a new note

```bash
python markterm.py new
```

### 2. List notes

```bash
python markterm.py list
```

### 3. Read a note

```bash
python markterm.py read
```

### 4. Edit a note

```bash
python markterm.py edit mynote.md
```

Set your preferred editor:

```bash
export EDITOR=vim       # or code, nano, notepad, etc.
```

### 5. Delete a note

```bash
python markterm.py delete
```

### 6. Search notes

```bash
python markterm.py search
```

### 7. Preview any Markdown file

```bash
python markterm.py mdread mynote.md
```

### 8. Backup all notes

```bash
python markterm.py backup
```

Creates a `.zip` in the `backups/` folder.

### 9. Restore a backup

```bash
python markterm.py restore backup_YYYY-MM-DD_HH-MM-SS.zip
```

---

## 📁 Project Structure

```
markterm/
├── markterm.py         # Main CLI script
├── utils.py            # Helper functions
├── notes/              # All your .md notes go here
├── backups/            # Automatic zip backups
└── README.md
```

---

## ✨ Inspired by

* Markdown
* Rich by Textualize
* Simplicity of the Unix philosophy

