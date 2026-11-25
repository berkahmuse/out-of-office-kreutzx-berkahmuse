#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry for @berkahmuse.

Writes one line of an out-of-office auto-reply (max 140 chars) to
/output/entry.txt. Fully deterministic: the same line every run.
"""

import os

ENTRY = "I'm out of office until Monday. If this is urgent, it isn't \u2014 I already asked my hammock, and it agrees with me."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
