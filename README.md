# 📘 MarkTerm

A simple Markdown-based terminal note-taking app with both **CLI** and **TUI** interfaces.

---

## ✨ Features

* 📝 **Create** new notes from terminal
* 📖 **Read** and render notes with Markdown
* ✏️ **Edit** notes using default system editor
* ❌ **Delete** notes
* 🔍 **Search** notes using a beautiful **Textual-based TUI**
* 💾 **Backup** all notes into a `.zip` archive
* ♻️ **Restore** notes from a backup archive
* 📁 All notes are stored as `.md` files inside a folder structure

---

## 🚀 Usage

### 🔧 Command Syntax

```bash
python markterm.py <command> [options]
```

### 📋 Available Commands

| Command   | Description                                |
| --------- | ------------------------------------------ |
| `new`     | Create a new note                          |
| `list`    | List all existing notes                    |
| `read`    | Read a note by name                        |
| `edit`    | Edit a note using your system editor       |
| `delete`  | Delete a note                              |
| `search`  | Launch TUI to search and preview notes     |
| `backup`  | Create a `.zip` backup of all notes        |
| `restore` | Restore notes from a `.zip` backup archive |

---

## 🔍 TUI Search

Powered by [`textual`](https://github.com/Textualize/textual) — a modern TUI framework.

### 📚 Features:

* Real-time fuzzy search of note titles and content
* View note preview in a split-pane
* Click or press `Enter` to view full content
* Press `Esc` to exit the TUI

> Run it via:

```bash
python markterm.py search
```

---

## 💾 Backup & Restore

* To back up all your notes:

```bash
python markterm.py backup --output backup.zip
```

* To restore from a `.zip` file:

```bash
python markterm.py restore --input backup.zip
```

> ⚠️ Restore will **overwrite** existing notes if names match!

---

## 📁 Folder Structure

* All notes are stored inside `notes/` as `.md` files
* Subfolders are supported (e.g., `notes/school/physics.md`)

---

## 🛠️ Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
textual>=0.38.0
rich
```

---

## 📌 Future Ideas

* Tag-based filtering
* Search across specific folders
* Sync with cloud storage (Dropbox, Google Drive)

---

## 🧑‍💻 Author

**Devaansh Pathak**
Project: `MarkTerm`
A CLI + TUI markdown notes app built with love and Python ❤️
 