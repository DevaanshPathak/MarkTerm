import sys
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, TextArea
from textual.containers import Vertical
from textual import events
from textual.reactive import reactive

class MarkTermEditNote(App):
    TITLE = "✏️ Edit Note - MarkTerm"

    BINDINGS = [
        ("ctrl+s", "save_note", "Save"),
        ("ctrl+q", "quit", "Quit"),
    ]

    status_message = reactive("")

    def __init__(self, folder: str, title: str):
        super().__init__()
        self.folder = folder
        self.title = title
        self.note_path = Path("notes") / folder / f"{title}.md"
        self.note_content = self.note_path.read_text(encoding="utf-8") if self.note_path.exists() else ""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static(f"📂 Editing: {self.title}.md in /{self.folder}", id="note-title"),
            TextArea(id="content", text=self.note_content),
            Static("", id="status-bar"),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(2, self.clear_status)

    def clear_status(self) -> None:
        status_bar = self.query_one("#status-bar", Static)
        if self.status_message:
            self.status_message = ""
            status_bar.update("")

    def action_save_note(self) -> None:
        text_area = self.query_one("#content", TextArea)
        content = text_area.text
        self.note_path.write_text(content, encoding="utf-8")
        self.status_message = "💾 Saved!"
        self.query_one("#status-bar", Static).update(self.status_message)

    def on_shutdown(self) -> None:
        self.action_save_note()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Usage: python markterm_tui_edit.py <folder> <title>")
        sys.exit(1)

    folder_arg = sys.argv[1]
    title_arg = sys.argv[2]
    app = MarkTermEditNote(folder_arg, title_arg)
    app.run()
