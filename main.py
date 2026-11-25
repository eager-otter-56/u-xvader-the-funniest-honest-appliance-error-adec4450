#!/usr/bin/env python3
"""Entry for The Funniest Honest Appliance Error.

Writes a single-line honest appliance error message to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = "Error: unbalanced load. One shoe is doing all the work. I have redistributed it 14 times. It is still one shoe."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, a single line.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
