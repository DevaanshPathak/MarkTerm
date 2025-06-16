# utils.py

import os
from config import NOTES_DIR
from rich.markdown import Markdown
from rich.console import Console


def create_note(title, content):
    category = input("📁 Enter folder/category (or press enter for general): ").strip().lower()
    folder = os.path.join(NOTES_DIR, category) if category else NOTES_DIR

    os.makedirs(folder, exist_ok=True)

    filename = title.lower().replace(" ", "_") + ".md"
    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        print("⚠️ Note already exists!")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Note '{title}' saved to '{folder}'.")

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

def search_notes():
    query = input("🔎 Enter a keyword to search: ").strip().lower()

    if not query:
        print("⚠️ Please enter a valid search term.")
        return

    files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    results = []

    for filename in files:
        title = filename[:-3].replace("_", " ")
        path = os.path.join(NOTES_DIR, filename)

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().lower()
                if query in title.lower() or query in content:
                    results.append((title.title(), path))
        except Exception as e:
            print(f"⚠️ Error reading {filename}: {e}")

    if not results:
        print("❌ No matching notes found.")
        return

    print(f"\n✅ Found {len(results)} matching note(s):")
    for idx, (title, _) in enumerate(results, 1):
        print(f"{idx}. {title}")

    try:
        choice = int(input("\n🔢 Enter the number of the note to read: "))
        if not (1 <= choice <= len(results)):
            print("❌ Invalid choice.")
            return

        _, selected_path = results[choice - 1]
        with open(selected_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print("\n🧾 Rendering note:\n")
        console.print(Markdown(content))

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