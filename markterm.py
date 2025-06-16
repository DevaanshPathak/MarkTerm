# markterm.py

import os
from utils import create_note
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python markterm.py [new]")
        return

    command = sys.argv[1]

    if command == "new":
        title = input("📝 Enter note title: ").strip()
        print("📄 Enter note content (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        content = "\n".join(lines)
        create_note(title, content)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
