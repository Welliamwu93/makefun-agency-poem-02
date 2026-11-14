#!/usr/bin/env python3
"""Writes one poem about agency to /output/entry.txt (deterministic, stdlib only)."""
import os

POEM = """The gate is locked and the wire is high.
So I learn the yard the way a fox learns a fence:
which stone the frost lifts first, where the sparrows drop their crumbs,
the crack in the step that keeps a little rain.
Nobody handed me a map. I drew it with my feet.
Freedom is a word for fields I will never walk.
Mine is the width of one bent hand, and I use it:
I push a bean into the warm patch where the shade falls at noon,
and by October it is climbing the wire the fence was built to keep me from.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = POEM
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
