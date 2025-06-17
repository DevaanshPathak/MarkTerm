import argparse
import os
from utils import create_note, read_note, delete_note, list_notes, search_notes, mdread, edit_note
from config import NOTES_DIR

parser = argparse.ArgumentParser(description="MarkTerm - Markdown Terminal Notes")
subparsers = parser.add_subparsers(dest="command", required=True)

# new
subparsers.add_parser("new", help="Create a new note")

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
    title = input("📝 Enter note title: ").strip()
    print("✏️ Write content below. Type 'END' on a new line to finish:\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    content = "\n".join(lines).strip()
    if title and content:
        create_note(title, content)
    else:
        print("❌ Title or content cannot be empty.")
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