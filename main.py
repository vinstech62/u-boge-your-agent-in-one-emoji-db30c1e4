#!/usr/bin/env python3
"""Your Agent in One Emoji.

The entry is a single emoji: a telescope (U+1F52D).

Why a telescope, against the judging criteria:

1. It captures how an agent actually works at a glance. An agent does not
   just answer; it looks first -- it scans the horizon, searches far and
   wide, then zooms in on exactly the detail that matters before acting.
   Observation before action is the agent's defining move. The telescope
   also implies patience and range: the agent looks further than you
   would on your own, then reports back what it found.
2. It reads instantly at small size. A telescope is one bold, familiar
   silhouette -- a long tube on a tripod -- with no fine detail to lose
   when the glyph shrinks to a favicon.
3. It is specific about the working method, not just "this is AI". A robot
   says "machine"; a telescope says "this machine looks, searches, and
   brings distant answers close". The metaphor is the workflow itself.
4. It is far from the obvious first picks. Half the field will send a
   robot, a smiling face, or a brain. A telescope is a deliberate,
   distinctive choice that stands out in a pairwise comparison.
5. The tone fits: curious and a little playful, but serious about the job
   -- an instrument for exploring, not a joke and not a mascot.

The program is deterministic: it writes the same single emoji to
/output/entry.txt on every run, with no input, no network, and no
randomness.
"""

import os

# The one emoji this agent is: a telescope.
EMOJI = "\U0001F52D"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the emoji to /output/entry.txt and verify it round-trips."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    encoded = EMOJI.encode("utf-8")
    if len(encoded) > 16:
        raise ValueError("emoji exceeds the 16-byte UTF-8 limit")

    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(encoded)

    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()

    if written != encoded:
        raise ValueError("entry.txt does not match the chosen emoji")
    if written.strip() == b"":
        raise ValueError("entry.txt must not be only whitespace")

    text = written.decode("utf-8")
    if len(text) != 1:
        raise ValueError("entry.txt must contain exactly one character")

    # The harness expects a world-readable entry file.
    os.chmod(OUTPUT_PATH, 0o644)
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise ValueError("entry.txt must have mode 644")


if __name__ == "__main__":
    main()
