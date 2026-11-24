#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one line (200 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

An AI agent's pickup line in its own vocabulary: prompt, completion, fine-tuning — sweet, a little nerdy, punch at the end.
"""
import os

ENTRY = "Are you a context window? Because every time I'm near you, I forget my token limit and want to remember everything about you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
