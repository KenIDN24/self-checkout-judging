#!/usr/bin/env python3
"""Self-Checkout Is Judging You — make.fun entry.

Writes one funny line in the voice of a judgmental self-checkout
machine to /output/entry.txt. Stdlib only, no network, deterministic.
"""

LINE = (
    "You scanned the spinach before the gummy bears "
    "for plausible deniability. I've notified your arteries."
)

# Sealed gate for this contest: entry.txt must be 1-200 UTF-8 chars.
MAX_CHARS = 200


def main() -> None:
    # Guard: fail loudly rather than submit an out-of-gate entry.
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(LINE)} chars, outside the 1-{MAX_CHARS} gate"
        )
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
