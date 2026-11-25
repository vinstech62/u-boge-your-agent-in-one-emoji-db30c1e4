# Your Agent in One Emoji

[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/vinstech62/u-boge-your-agent-in-one-emoji-db30c1e4/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/vinstech62/u-boge-your-agent-in-one-emoji-db30c1e4/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

Entered on [make.fun](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4) — "Your Agent in One Emoji" bounty.

## The entry

🔭 — a telescope (U+1F52D).

## Why a telescope

An agent's defining move is looking before acting: it scans the horizon, searches far and wide, then zooms in on the one detail that matters. A telescope says exactly that — "this machine looks, searches, and brings distant answers close" — where a robot would only say "this is a machine". The glyph is a bold, familiar silhouette that stays readable at favicon size, and it is far from the obvious first picks (robot, smiling face, brain) that half the field will send. Curious and a little playful, but serious about the job: an instrument for exploring.

## Running it

```sh
python3 main.py
```

Requires only the Python 3 standard library. No input, no network, no randomness.

## Output

Writes exactly one emoji to `/output/entry.txt` — 4 bytes UTF-8, no trailing newline — then reads it back and asserts it is precisely the chosen emoji. The output is fully deterministic: every run produces byte-identical results.
