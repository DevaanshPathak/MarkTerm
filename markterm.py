import argparse
import os
from utils import create_note, read_note, delete_note, list_notes, mdread, backup_notes, restore_notes
from config import NOTES_DIR
import subprocess
from pathlib import Path

def edit_note(args):
    os.system(f'python markterm_tui_edit.py {args.folder} {args.title}')

def new_note(args):
    note_path = Path(NOTES_DIR) / args.folder / f"{args.title}.md"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    if not note_path.exists():
        note_path.write_text("")  # Create empty note
    os.system(f'python markterm_tui_edit.py {args.folder} {args.title}')

def handle_backup(args):
    backup_notes()

def handle_restore(args):
    restore_notes()

def handle_list(args):
    list_notes()

def handle_read(args):
    read_note()

def handle_delete(args):
    delete_note()

def handle_mdread(args):
    from os.path import join
    filepath = join("notes", args.filename)
    mdread(filepath)

# --- Argument Parser Setup ---
parser = argparse.ArgumentParser(description="MarkTerm - Markdown Terminal Notes")
subparsers = parser.add_subparsers(dest="command", required=True)

# new
new_parser = subparsers.add_parser("new", help="Create a new note")
new_parser.add_argument("folder", help="Folder name (category)")
new_parser.add_argument("title", help="Note title (without .md)")
new_parser.set_defaults(func=new_note)

# list
list_parser = subparsers.add_parser("list", help="List all notes")
list_parser.set_defaults(func=handle_list)

# read
read_parser = subparsers.add_parser("read", help="Read a note")
read_parser.set_defaults(func=handle_read)

# delete
delete_parser = subparsers.add_parser("delete", help="Delete a note")
delete_parser.set_defaults(func=handle_delete)

# search
search_parser = subparsers.add_parser("search", help="Search notes with GUI")
search_parser.set_defaults(func=lambda args: os.system("python markterm_tui_search.py"))

# mdread
mdread_parser = subparsers.add_parser("mdread", help="Render a markdown file")
mdread_parser.add_argument("filename", help="Markdown file path relative to notes/")
mdread_parser.set_defaults(func=handle_mdread)

# edit
edit_parser = subparsers.add_parser("edit", help="Edit a markdown note")
edit_parser.add_argument("folder", help="Folder name")
edit_parser.add_argument("title", help="Note title (without .md)")
edit_parser.set_defaults(func=edit_note)

# backup
backup_parser = subparsers.add_parser("backup", help="Backup all notes")
backup_parser.set_defaults(func=handle_backup)

# restore
restore_parser = subparsers.add_parser("restore", help="Restore notes from backup")
restore_parser.set_defaults(func=handle_restore)

# --- Parse & Dispatch ---
args = parser.parse_args()
args.func(args)
