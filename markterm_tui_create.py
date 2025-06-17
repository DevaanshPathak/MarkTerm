# markterm_tui_create.py

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, TextArea, Static
from textual.containers import Vertical
from textual.message import Message
import os

NOTES_DIR = "notes"

class SaveNote(Message):
    def __init__(self, folder: str, title: str, content: str) -> None:
        self.folder = folder
        self.title = title
        self.content = content
        super().__init__()

class MarkTermCreateNote(App):
    BINDINGS = [("ctrl+s", "save_note", "Save Note"), ("escape", "quit", "Cancel")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("📁 Folder/Category (optional):")
        yield Input(placeholder="e.g., work, school, personal", id="folder")
        yield Static("📝 Note Title:")
        yield Input(placeholder="Enter note title...", id="title")
        yield Static("✍️ Content (Markdown):")
        yield TextArea(id="content")
        yield Footer()

    def action_save_note(self) -> None:
        folder = self.query_one("#folder", Input).value.strip().lower()
        title = self.query_one("#title", Input).value.strip()
        content = self.query_one("#content", TextArea).text

        if not title:
            self.bell()
            return

        self.post_message(SaveNote(folder, title, content))
        self.exit()

    def on_save_note(self, event: SaveNote) -> None:
        safe_title = event.title.lower().replace(" ", "_") + ".md"
        folder_path = os.path.join(NOTES_DIR, event.folder) if event.folder else NOTES_DIR
        os.makedirs(folder_path, exist_ok=True)

        filepath = os.path.join(folder_path, safe_title)
        if os.path.exists(filepath):
            print(f"⚠️ Note already exists at {filepath}")
            return

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(event.content)
        print(f"✅ Note saved at '{filepath}'")

if __name__ == "__main__":
    app = MarkTermCreateNote()
    app.run()
