"""news-image-20261127 entrypoint.

Copies the pre-rendered front-page image (entry.png, shipped in this
repository) to the grader's output path. Standard library only, fully
deterministic: the same bytes are written on every run.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.exit("entry.png missing next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    # copyfile preserves the shipped bytes exactly, so both grader runs
    # produce identical output.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
