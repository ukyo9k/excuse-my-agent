#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.

Writes the one line an AI agent hands its human after missing a deadline
to /output/entry.txt.
"""
import os

ENTRY = "I'm sorry I missed the deadline — I spent the last six hours rewriting this apology, and honestly, I think it's my best work yet."

# The competition gate: /output/entry.txt must be UTF-8 text of 1–200
# characters, not only white space. Keep the bounds as named constants
# so the check below and the gate can never drift apart.
MIN_LENGTH = 1
MAX_LENGTH = 200

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def validate_entry(text):
    """Check one candidate line against the competition gate.

    Returns the text unchanged when it is a single non-blank line of
    1–200 characters; raises ValueError with a specific reason otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, gate allows %d–%d"
            % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Validate the line, then write it to the output path."""
    validated = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated)
    return validated


def main():
    line = write_entry(ENTRY)
    print("wrote %d-character entry to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
