#!/usr/bin/env python3
"""One Line of Earned Pride -- program/v1 entry.

Writes a single line of text (1-240 characters) to /output/entry.txt.
The output directory honours MAKEFUN_OUTPUT_DIR when set (the grader
sets it to /output); otherwise it falls back to /output.
"""

import os

LINE = "At the kitchen table, seventy-two-year-old Rosa read her grandson's birthday card aloud \u2014 a year of night classes, a pencil that kept slipping, every word without stopping once."

def main() -> None:
    # Gate contract: UTF-8 text, 1 to 240 characters, not only whitespace.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
