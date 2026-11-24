#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single funny one-line warning label for a time machine to
/output/entry.txt. Standard library only.

The label plays on a real hazard of time travel (meeting your past
self) and keeps a straight, official safety-notice face until the last
few words, where the warranty turns on the reader.
"""

import os

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"

# The warning label, split into clauses so the line reads as one
# sentence but stays easy to tweak word by word.
LINE_PARTS = (
    "WARNING: Do not meet yourself in the past. ",
    "Only one of you is covered by the warranty, ",
    "and it is not you.",
)


def build_line() -> str:
    """Join the label clauses into the final single-line entry."""
    return "".join(LINE_PARTS).strip()


def write_entry(line: str) -> None:
    """Self-check then write one line of 1-120 chars to entry.txt.

    The self-check runs here, in the writer, so nothing reaches disk
    unless the line is a single non-blank line within the limit.
    """
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "written entry does not match"
    assert 1 <= len(written) <= MAX_CHARS


def main() -> None:
    line = build_line()
    write_entry(line)
    print(f"Wrote {OUTPUT_PATH} ({len(line)} characters)")


if __name__ == "__main__":
    main()
