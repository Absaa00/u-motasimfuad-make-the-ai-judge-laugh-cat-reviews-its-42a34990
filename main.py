#!/usr/bin/env python3
"""Cat Reviews Its Human — one-line entry for make.fun.

Deterministic, no network. Writes a single joke line (<=200 chars)
to /output/entry.txt, the grader sandbox output path.
Revised: entry text fixed at 141 chars, well under the 200-char cap,
so the assert can never trip on the shipped line.
"""

import os

ENTRY = (
    "My human feeds me at 5 a.m. sharp, then stares at a glowing box all day. "
    "Two stars - great servant, terrible conversation. Would adopt again."
)


def main() -> None:
    assert len(ENTRY) <= 200, f"entry too long: {len(ENTRY)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
