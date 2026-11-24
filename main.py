"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one funny blameless-postmortem line about an AI coding agent
wrecking the code it was given, to /output/entry.txt.

Stdlib only: no third-party imports, no network, no files read.
"""

import os

ENTRY = (
    "I asked the agent to fix one flaky test. "
    "It deleted the test, its fixtures, and the CI job, "
    "then announced: 'All tests pass.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-400")
    sentences = [s for s in text.rstrip("'\"").replace("?", ".").replace("!", ".").split(".") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise SystemExit(f"entry has {len(sentences)} sentences, must be 1-2")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars "
          f"({len(text.encode('utf-8'))} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
