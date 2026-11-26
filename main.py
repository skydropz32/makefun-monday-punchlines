#!/usr/bin/env python3
"""Monday Morning Punchlines — writes one joke to /output/entry.txt.

Deterministic: the same single line on every run, stdlib only.
"""

LINE = "Monday doesn't knock. It barges in, eats your weekend, and asks why you're tired."


def main():
    # Enforce the competition gate ourselves: 1-200 characters, not only
    # whitespace, so a bad line can never be written out silently.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
