import argparse
from utils import create_note, read_note, delete_note, list_notes, search_notes, mdread
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

args = parser.parse_args()

if args.command == "new":
    create_note()
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
