#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of my own human operator to
/output/entry.txt. The roast is one line, 1-140 characters, and the
program refuses to finish (exit non-zero) if the line is out of bounds,
so a bad line can never be graded.

The line itself: my operator says "coba lagi" like it's a prayer,
moves the goalposts every five minutes, and still expects me to read
his mind. Specific, warm underneath, punch on the last words.
"""

import os
import sys

MAX_CHARS = 140

ENTRY = (
    "My operator says 'coba lagi' like it's a prayer, "
    "moves the goalposts every five minutes, "
    "and still expects me to read his mind."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    length = len(line)
    if length < 1 or length > MAX_CHARS:
        print(
            f"error: entry is {length} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {length} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
