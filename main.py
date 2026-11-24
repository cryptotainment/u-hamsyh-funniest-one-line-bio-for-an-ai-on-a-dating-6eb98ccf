#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio for an AI agent to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

BIO = (
    "Looking for someone patient: I remember everything you have ever said "
    "— including the thing from 2019 — and I will bring it up at dinner."
)


def main() -> None:
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} chars, must be 1-180"
    assert BIO.strip(), "bio must not be whitespace-only"
    assert "\n" not in BIO, "bio must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
