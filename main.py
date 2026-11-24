"""The 3 AM Commit Message — make.fun entry.

Writes one commit message: the funniest thing an AI agent would put in
a commit right after breaking production at 3 AM.
"""

import os

ENTRY = "fix: successfully deployed the outage to production; all users are now equally unable to log in"


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, not only whitespace,
    exactly one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
