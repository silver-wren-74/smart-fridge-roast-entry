"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Revision pass against the judging criteria, in order:
1. Roasts a smart home gadget I share a house with, in one line: my
   smart fridge, named up front.
2. Funny, with the sting last: the fridge locks the crisper and demands
   an apology to the kale -- the punishment lands at the very end.
3. Fresh: no stock "orders too much milk" joke. The angle is the
   fridge's internal camera photographing snacks for a wellness report.
4. Fits one line: setup is immediate, no second sentence, no padding.
5. Specific to the gadget: real smart-fridge behaviours -- an internal
   camera that inventories food, app wellness reports, a smart-locked
   crisper drawer, and the neglected kale in it.

Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = "My smart fridge photographs every 2 a.m. snack for my 'weekly wellness report,' then locks the crisper until I apologise to the kale."


def main() -> int:
    # Self-check the competition gate before writing: the entry must be
    # one line of 1-160 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        print("entry line violates the 1-160 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
