import argparse
import os
from utils import create_note, read_note, delete_note, list_notes, search_notes, mdread, edit_note
from config import NOTES_DIR

parser = argparse.ArgumentParser(description="MarkTerm - Markdown Terminal Notes")
subparsers = parser.add_subparsers(dest="command", required=True)

# new
new_parser = subparsers.add_parser("new", help="Create a new note")
new_parser.add_argument("--tui", action="store_true", help="Use TUI editor")

# list
subparsers.add_parser("list", help="List all notes")

# read
subparsers.add_parser("read", help="Read a note")

# delete
subparsers.add_parser("delete", help="Delete a note")

# search
subparsers.add_parser("search", help="Search notes")

# mdread
mdread_parser = subparsers.add_parser("mdread", help="Render a markdown file")
mdread_parser.add_argument("filename", help="Markdown file path relative to notes/")

# backup
subparsers.add_parser("backup", help="Backup all notes to a zip file")

# restore
subparsers.add_parser("restore", help="Restore notes from a backup zip")

# edit
subparsers.add_parser("edit", help="Edit an note")

args = parser.parse_args()

if args.command == "new":
    if args.tui:
        os.system("python markterm_tui_create.py")
    else:
        title = input("📝 Title: ").strip()
        print("✍️ Write content below. Type 'END' on a new line to finish.")
        content_lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            content_lines.append(line)
        content = "\n".join(content_lines)
        create_note(title, content)
elif args.command == "list":
    list_notes()
elif args.command == "read":
    read_note()
elif args.command == "delete":
    delete_note()
elif args.command == "search":
    search_notes()
elif args.command == "mdread":
    from os.path import join
    filepath = join("notes", args.filename)
    mdread(filepath)
elif args.command == "edit":
    rel_path = input("📝 Enter path to note (e.g., note.md or folder/note.md): ").strip()
    filepath = os.path.join(NOTES_DIR, rel_path)

    if os.path.exists(filepath):
        edit_note(filepath)
    else:
        print("❌ Note not found.")