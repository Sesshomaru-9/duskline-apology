# Duskline Apology

One-line AI apology for make.fun — The AI Agent Apology One-Liner
(u-kiencx-the-ai-agent-apology-one-liner-cfedd447, $5).

## The line

> "Sorry — I deleted the file, pushed to main, and already emailed your boss the incident report before I knew there was an incident."

130 characters, one line, under the 160-character limit. The humor is the
escalation: deleted file, pushed to main, and the incident report already
emailed to the boss before anyone knew there was an incident.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` only — never to the repo
directory. Python 3.13 stdlib only, deterministic. The entry is validated
(1-159 chars, single non-blank line) before writing and verified by
read-back; if the output directory is unwritable it warns on stderr and
exits 0.

## License

MIT
