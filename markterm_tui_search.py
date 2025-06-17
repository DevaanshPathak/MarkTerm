from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, Label, Static
from textual.containers import Vertical
from textual.reactive import reactive
from rich.markdown import Markdown
from config import NOTES_DIR
from pathlib import Path

class NoteItem(ListItem):
    def __init__(self, display_name: str, path: Path):
        super().__init__(Label(display_name))
        self.note_path = path

class SearchApp(App):

    query = reactive("")
    results = reactive([])

    def on_key(self, event):
        if event.key == "escape":
            self.exit()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Input(placeholder="🔎 Search notes...", id="search_input"),
            ListView(id="results_view"),
            Static("📄 Note preview will appear here.", id="content_view", expand=True),
            Static("🔍 Type to search | ⬆⬇ to navigate | ⏎ to view | [Esc] to exit", id="footer", classes="footer")
        )


    def on_mount(self):
        self.query_input = self.query_one("#search_input", Input)
        self.results_view = self.query_one("#results_view", ListView)
        self.content_view = self.query_one("#content_view", Static)

    def on_input_changed(self, message: Input.Changed) -> None:
        self.query = message.value.strip().lower()
        self.results = self.search_notes(self.query)
        self.update_results()

    def search_notes(self, query):
        matched = []
        for path in Path(NOTES_DIR).rglob("*.md"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                name = str(path.relative_to(NOTES_DIR))[:-3].replace("_", " ").title()
                if query in name.lower() or query in content:
                    matched.append((name, path))
            except Exception as e:
                print(f"⚠️ Error reading {path}: {e}")
        return matched

    def update_results(self):
        self.results_view.clear()
        for display_name, path in self.results:
            self.results_view.append(NoteItem(display_name, path))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        note_item = event.item
        if isinstance(note_item, NoteItem):
            path = note_item.note_path
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.content_view.update(Markdown(content))
            except Exception as e:
                self.content_view.update(f"❌ Failed to load note: {e}")



    def view_note_item(self, item: ListItem):
        if isinstance(item, NoteItem):
            path = item.note_path
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.content_view.update(Markdown(content))
            except Exception as e:
                self.content_view.update(f"❌ Failed to load note: {e}")


# 👇 This is critical: it actually starts the app
if __name__ == "__main__":
    SearchApp().run()
