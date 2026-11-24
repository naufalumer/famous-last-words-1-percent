"""Famous Last Words at 1 Percent.

The entry is one line: the last words a phone says when its battery
hits 1 percent. This program writes that single line, exactly as it
stands below, to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when
the variable is unset). Standard library only, no input, no network.
"""

import os
import sys

ENTRY = "I have been at 1 percent for twenty minutes. I stayed alive just to see who you would call first."

MAX_CHARS = 199


def entry_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def main() -> int:
    text = ENTRY
    if not text.strip() or len(text) > MAX_CHARS or "\n" in text or "\r" in text:
        print("entry must be one line of 1-199 non-blank characters", file=sys.stderr)
        return 1
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
