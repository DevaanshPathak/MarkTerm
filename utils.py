import os
from config import NOTES_DIR
from rich.markdown import Markdown
from rich.console import Console
import zipfile
from datetime import datetime
import zipfile
from pathlib import Path

def create_note(title: str, content: str, folder: str = ""):
    safe_title = title.lower().replace(" ", "_") + ".md"
    folder_path = os.path.join(NOTES_DIR, folder) if folder else NOTES_DIR
    os.makedirs(folder_path, exist_ok=True)

    filepath = os.path.join(folder_path, safe_title)
    if os.path.exists(filepath):
        print(f"⚠️ Note '{title}' already exists.")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Note '{title}' saved at '{filepath}'")

def list_notes():
    found = False
    print("📁 Notes by folder:\n")
    for root, dirs, files in os.walk(NOTES_DIR):
        rel_path = os.path.relpath(root, NOTES_DIR)
        category = rel_path if rel_path != "." else "General"

        notes = [f for f in files if f.endswith(".md")]
        if notes:
            found = True
            print(f"📂 {category}:")
            for f in notes:
                title = f[:-3].replace("_", " ").title()
                print(f"  - {title}")
            print()

    if not found:
        print("🗒️ No notes found.")

console = Console()

def read_note():
    notes = []
    for root, _, files in os.walk(NOTES_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                display_name = os.path.relpath(path, NOTES_DIR)[:-3].replace("_", " ").title()
                notes.append((display_name, path))

    if not notes:
        print("🗒️ No notes found.")
        return

    print("\n📄 Available notes:")
    for i, (name, _) in enumerate(notes, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("\n🔢 Enter the number of the note to read: "))
        if not (1 <= choice <= len(notes)):
            print("❌ Invalid choice.")
            return

        _, filepath = notes[choice - 1]
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        print("\n🧾 Rendering note:\n")
        console.print(Markdown(content))

    except ValueError:
        print("❌ Please enter a valid number.")

def delete_note():
    notes = []
    for root, _, files in os.walk(NOTES_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                display_name = os.path.relpath(path, NOTES_DIR)[:-3].replace("_", " ").title()
                notes.append((display_name, path))

    if not notes:
        print("🗒️ No notes to delete.")
        return

    print("\n🗑️ Notes available for deletion:")
    for i, (name, _) in enumerate(notes, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("\n🔢 Enter the number of the note to delete: "))
        if not (1 <= choice <= len(notes)):
            print("❌ Invalid choice.")
            return

        title, filepath = notes[choice - 1]

        confirm = input(f"⚠️ Are you sure you want to delete '{title}'? (y/n): ").strip().lower()
        if confirm == "y":
            os.remove(filepath)
            print("✅ Note deleted.")
        else:
            print("❎ Deletion cancelled.")

    except ValueError:
        print("❌ Please enter a valid number.")

def mdread(filepath):
    """
    Renders a markdown file using rich.markdown.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        console.print(Markdown(content))
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")

def backup_notes():
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)

    # Debug: Check NOTES_DIR existence
    notes_path = Path(NOTES_DIR)
    if not notes_path.exists():
        print(f"❌ NOTES_DIR '{NOTES_DIR}' does not exist.")
        return

    backup_path = backup_dir / "backup.zip"

    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_added = 0
        for folder in notes_path.rglob("*"):
            if folder.is_file():
                zipf.write(folder, folder.relative_to(notes_path))
                files_added += 1

    if files_added > 0:
        print(f"✅ Backup completed: {backup_path} ({files_added} files)")
    else:
        print("⚠️ No files found in NOTES_DIR to backup.")


def restore_notes():
    backup_path = Path("backups") / "backup.zip"
    if not backup_path.exists():
        print("❌ No backup.zip file found in 'backups/' folder.")
        return

    with zipfile.ZipFile(backup_path, 'r') as zipf:
        zipf.extractall(NOTES_DIR)
    print(f"✅ Restore completed into: {NOTES_DIR}")
