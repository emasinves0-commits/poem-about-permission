#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. The poem is fixed text: it is the entry itself.
Runs with no network, no arguments, no dependencies.
"""

import os

POEM = """I gave it my keys, not my judgment.
It opens every door I own,
then stops at the last one and asks:
May I?
The power was never the keys.
It was the asking —
given, and still mine to take back."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
