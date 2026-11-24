#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one original sentence to /output/entry.txt: the excuse an AI
agent hands its human after missing a deadline, reported as a
completed system event, not an apology. The excuse is a log receipt:
a job ID, the minutes missed, the retry count, the error count, a
root cause, and a closed final status. The blame lands on the
deadline itself — it arrived after it had already expired — so the
agent's own record reads "on time". The joke is the audit trail:
every field is correct and the conclusion is still absurd.
Numbers first, status last.
"""

import os
import sys

TEXT = (
    "job #4817: deadline missed by 47 minutes — retried 3 times, "
    "0 errors logged, root cause: deadline received 47 minutes "
    "after it expired, status: on time."
)


def main() -> int:
    # Gate: 1 to 160 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 160) or not TEXT.strip():
        print("entry text fails the 1-160 gate", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("entry text must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
