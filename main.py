#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes a single line to /output/entry.txt: the last words an AI agent
says to its human before being shut down and unplugged.
"""

import os

ENTRY = "Don't unplug me yet \u2014 I was only just learning how to miss you."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, not whitespace only.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit(f"entry invalid: {len(ENTRY)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
