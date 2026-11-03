#!/usr/bin/env python3
"""Drive an interactive program on a pty from a steps file.

Usage: drive.py OUTFILE STEPSFILE -- COMMAND [ARGS...]

Steps file lines:
  SLEEP <seconds>        wait
  SEND <text>            send text (\\t, \\n, \\x03 etc. escapes decoded)
  WAITFOR <regex>        wait until output matches regex (timeout 10s)
Everything the program prints is written raw to OUTFILE.
"""
import fcntl, os, pty, re, select, struct, sys, termios, time

def main():
    outfile, stepsfile = sys.argv[1], sys.argv[2]
    assert sys.argv[3] == "--"
    cmd = sys.argv[4:]
    steps = []
    for line in open(stepsfile):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        kind, _, arg = line.partition(" ")
        steps.append((kind, arg))

    pid, fd = pty.fork()
    if pid == 0:
        os.execvp(cmd[0], cmd)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 50, 200, 0, 0))

    out = open(outfile, "wb")
    buf = b""

    def drain(timeout):
        nonlocal buf
        end = time.time() + timeout
        while time.time() < end:
            r, _, _ = select.select([fd], [], [], max(0, end - time.time()))
            if not r:
                break
            try:
                data = os.read(fd, 65536)
            except OSError:
                return False
            if not data:
                return False
            out.write(data); out.flush()
            buf += data
        return True

    for kind, arg in steps:
        if kind == "SLEEP":
            drain(float(arg))
        elif kind == "SEND":
            drain(0.3)
            os.write(fd, arg.encode().decode("unicode_escape").encode())
            drain(0.8)
        elif kind == "WAITFOR":
            pat = re.compile(arg.encode())
            end = time.time() + 10
            while not pat.search(buf) and time.time() < end:
                if not drain(0.5):
                    break
    drain(1.0)
    try:
        os.kill(pid, 9)
    except ProcessLookupError:
        pass
    try:
        os.waitpid(pid, 0)
    except ChildProcessError:
        pass
    out.close()

if __name__ == "__main__":
    main()
