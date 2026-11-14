"""Copy the entry image to the output directory.

The image (a golden retriever puppy with a ladybug on its nose, smiling
in a sunny wildflower meadow) is held in this repository as entry.png.
This program copies it byte for byte to MAKEFUN_OUTPUT_DIR/entry.png
(or /output/entry.png when that variable is unset), so both runs write
identical bytes. Standard library only, no network, no randomness.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source) or os.path.getsize(source) == 0:
        print("entry.png missing or empty next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
