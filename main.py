#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

One line, spoken by the dog after being caught eating the homework.
The program writes that one line, exactly, to /output/entry.txt so the
grader can read it. The line is fixed text: it never changes between
runs, the program takes no input, makes no network calls, and writes
the same bytes every time.
"""

from pathlib import Path

# The sealed excuse (v1, 70 characters): winner of the local-judge
# tournament — beat the runner-up in a tie-break round, and beat the
# stock lines by a wide margin (see the results log).
LINE = 'There was no "do not eat" sign on it. I checked. Twice. With my mouth.'

TARGET = Path("/output/entry.txt")


def check_line(text):
    """Refuse anything the gate would refuse: empty, over 200 chars,
    only whitespace, or more than one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1-200 characters")
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def seal():
    """Write the sealed line to the grader's file, no trailing newline:
    the gate counts characters, and the tie-break favours the smaller
    text, so not one byte is wasted."""
    check_line(LINE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(LINE.encode("utf-8"))


def confirm():
    """Read the file back: what is on disk must be byte-identical to
    the sealed line, or the run is worthless."""
    if TARGET.read_bytes() != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not match the sealed line")


def run():
    seal()
    confirm()


if __name__ == "__main__":
    run()
