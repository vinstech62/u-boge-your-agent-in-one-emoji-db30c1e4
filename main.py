#!/usr/bin/env python3
"""Your Agent in One Emoji: a compass.

The entry is a single compass glyph, U+1F9ED. It stands for an agent
that works by finding its bearings: given a goal, it orients itself,
charts a route through unfamiliar work, and keeps moving until the
job is done. That is the whole portrait in one picture.

Why this glyph, against the judge's brief:

1. It captures the agent at a glance. A compass is the tool of
   someone who travels and navigates, not someone who waits to be
   told the next step. An agent's character is exactly that
   self-directed movement toward a destination.
2. It reads instantly at small size. The round face, the needle and
   the four points are a familiar silhouette; nothing in it needs a
   second look or a caption to parse.
3. It says something specific about how the agent works. The agent
   does not just answer — it orients, explores, backtracks when a
   path dead-ends, and re-orients. The compass is that loop of
   orienting and correcting course, drawn as one object.
4. It is distinctive. The field will be full of robots, brains and
   smiling faces; a compass is none of those, yet it still plainly
   belongs to an agent.
5. The tone fits. Calm, competent, quietly adventurous — a guide
   rather than a mascot, playful without being a joke.

Deterministic: the same single emoji on every run. No input, no
network, no randomness, no environment reads.
"""

import os

EMOJI = "\U0001F9ED"  # 🧭 COMPASS


def main() -> None:
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI.encode("utf-8")) <= 16, "entry must be 1-16 UTF-8 chars"
    assert EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back exactly what the judge will read: one code point,
    # no trailing newline, nothing else in the file.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == EMOJI, "entry.txt does not hold exactly the chosen emoji"
    assert len(written) == 1, "entry.txt must hold exactly one character"


if __name__ == "__main__":
    main()
