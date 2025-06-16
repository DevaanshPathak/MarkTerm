# utils.py

import os
from config import NOTES_DIR

def create_note(title, content):
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

    safe_title = title.strip().lower().replace(" ", "_")
    filename = os.path.join(NOTES_DIR, f"{safe_title}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(content)

    print(f"✅ Note saved as {filename}")
