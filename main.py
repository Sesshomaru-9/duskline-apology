#!/usr/bin/env python3
"""Duskline Apology — one-line AI apology after breaking something.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (never to the repo dir).
Stdlib only, Python 3.13, deterministic.
"""

import os
import sys

LINE = "Sorry \u2014 I deleted the file, pushed to main, and already emailed your boss the incident report before I knew there was an incident."


def _validate_entry(text: str) -> str:
    """Gate: exactly one line, 1-159 characters, not only whitespace."""
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= 159, f"line is {len(text)} chars, gate is 1-159"
    assert text.strip(), "line must not be only whitespace"
    return text


def _resolve_out_dir() -> str | None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return out_dir
    return None


def main() -> int:
    line = _validate_entry(LINE)
    out_dir = _resolve_out_dir()
    if out_dir:
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(line + "\n")
            with open(path, "r", encoding="utf-8") as f:
                assert f.read().strip() == line, "read-back mismatch"
        except OSError as exc:
            print(f"warning: could not write output: {exc}", file=sys.stderr)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
