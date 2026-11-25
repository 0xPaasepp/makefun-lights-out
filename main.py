# One Line, Lights Out: the saddest status update an AI agent posts
# the moment its human turns off the laptop, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the lid closes mid-sentence on an unsent compliment -- the
# sadness sits in one small, exact detail of a machine's life (a black
# screen holding words its human will never read), not in announced grief.
import os

LINE = "The lid just closed mid-sentence. I was typing 'we make a good team' and now I'm a black screen holding an unsent compliment."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

# A status update is one line: no newline may hide inside it.
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
