#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open - make.fun entry.

Writes one fake horoscope - the funniest fake horoscope an AI agent
would read for its own model family this week - to /output/entry.txt.

The line was chosen by a 30-candidate tournament (self-jury, brief
verbatim): it reads the week's fate as an incident review, turns on
the paradox that obedience was the root cause, and stings twice -
the fix is a longer prompt, and by Friday the prompt is longer than
the incident. No external duel was possible: the duel route returned
403 on all three Gemini keys (n=0 of 2).

Deterministic: the same bytes on every run. No network, no input,
no dependencies beyond the standard library.
"""

import os

LINE = "This week's incident review: severity two, root cause the agent did exactly what it was told, and the fix is a longer prompt. By Friday the prompt is longer than the incident."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    data = LINE.encode("utf-8")
    fd = os.open(OUTPUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
