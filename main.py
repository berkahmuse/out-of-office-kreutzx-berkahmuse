#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry for @berkahmuse.

Writes one line of an out-of-office auto-reply (max 140 chars) to
/output/entry.txt. Fully deterministic: the same line every run.
"""

import os

ENTRY = "I'm out of office until Monday. If this is urgent, it isn't \u2014 I already asked my hammock, and it agrees with me."

# The competition gate, enforced here before anything is written:
# UTF-8 text, 1-140 characters, a single line, not only white space.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate allows 1-140"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
