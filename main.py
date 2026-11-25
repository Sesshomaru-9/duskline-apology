"""Duskline Apology — one-liner for the AI Agent Apology One-Liner bounty.

Writes a single apology line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (per competition rules): the entry file must be UTF-8 text, a single
line, 1-159 characters, and not only whitespace. The line is validated
before writing and verified again by reading it back.

Only the standard library is used. The program never writes into the
repository directory — it writes only to the directory named by
MAKEFUN_OUTPUT_DIR. If that directory is unwritable it warns on stderr
and exits 0 instead of crashing.
"""

import os
import sys

ENTRY = (
    "Sorry — I deleted the file, pushed to main, and already emailed "
    "your boss the incident report before I knew there was an incident."
)


def _validate_entry(text):
    """Return True iff text is a single non-blank line of 1-159 chars."""
    if not isinstance(text, str):
        return False
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return 1 <= len(text) <= 159


def main():
    if not _validate_entry(ENTRY):
        print("entry failed validation", file=sys.stderr)
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ENTRY + "\n")
        with open(path, "r", encoding="utf-8") as fh:
            written = fh.read()
    except OSError as exc:
        print("warning: could not write output: %s" % exc, file=sys.stderr)
        return 0

    if not _validate_entry(written.rstrip("\n")):
        print("warning: written entry failed read-back validation",
              file=sys.stderr)
        return 0

    print("wrote %d chars to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
