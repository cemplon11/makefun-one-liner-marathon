#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single original joke to /output/entry.txt.

Pure Python stdlib only. Deterministic: the same line on every run.
"""

import os

JOKE = (
    "I taught my dog to fetch my slippers. Now he brings me the neighbor's "
    "slippers, the mailman's sandwich, and a restraining order \u2014 which, "
    "to be fair, he also fetched."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
