#!/usr/bin/env python3
"""Strip ANSI escapes, CRs and bracketed-paste markers from a raw pty
capture, collapse the blank runs the terminal leaves behind, and print
the readable session."""
import re, sys

data = open(sys.argv[1], "rb").read().decode("utf-8", "replace")
data = re.sub(r"\x1b\[[0-9;?]*[ -/]*[@-~]", "", data)   # CSI sequences
data = re.sub(r"\x1b\][^\x07\x1b]*(\x07|\x1b\\)", "", data)  # OSC sequences
data = data.replace("\x1b>", "").replace("\x1b=", "")
data = data.replace("\r\n", "\n").replace("\r", "\n")
lines = [ln.rstrip() for ln in data.split("\n")]
out, blank = [], 0
for ln in lines:
    if ln.strip() == "":
        blank += 1
        if blank <= 1:
            out.append("")
    else:
        blank = 0
        out.append(ln)
while out and out[0] == "":
    out.pop(0)
while out and out[-1] == "":
    out.pop()
print("\n".join(out))
