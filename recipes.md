# Recipes

**Outcome: six small jobs done the zsh
way.** The mechanisms that are new here
— modifiers, `zmv`, sort qualifiers,
the `always` block — were each run in
the lab before being written up, in
transcript `t11-recipes.txt`; the rest
reuse earlier chapters' verified parts.

## 1. Jump to a directory by its contents' name

You remember the file, not the folder:

```bash
cd **/old-report-2019.txt(:h)
```

The `(:h)` is a *modifier* — it takes
the head (directory part) of each name
the glob found, and the lab's run
landed in `archive/`, where that old
report lives. Chapter 6's `**` finds
the file anywhere below you; `:h` turns
the answer into the directory to enter.
Its partner `:t` (tail) keeps just the
filename part.

## 2. Rename a set of files by pattern

The fixture reports, re-dated in one
line, using zsh's own `zmv` tool (it
ships with the shell; load it once):

```bash
autoload -Uz zmv
zmv 'report-(*).txt' 'summary-$1.txt'
```

`zmv` shows its work with `-n` first
(`zmv -n ...` is a dry run — use it).
For the same job in a pipeline, the
modifier form works on any expansion:
`print -l *.txt(:r)` prints the names
with their extension removed (`:r`,
root), the usual first step in a
conversion loop.

## 3. The newest file, without ls -t

```bash
echo newest: *(om[1])
```

Qualifiers again (chapter 6): `om`
sorts by modification time, newest
first, and `[1]` takes the first match.
Oldest is `*(Om[1])`. No pipe, no
parsing of `ls` output, no race with
filenames containing newlines.

## 4. Run a command in every project folder

```bash
for d in */; do (cd "$d" && git status -s); done
```

The trailing slash on the glob means
only directories are listed, so `$d` is
always a folder the shell actually
found, spaces in its name and all, and
the quoting stays simple. The lab ran
the same loop with `pwd` (transcript
`t11`) and visited all three fixture
folders in turn.

## 5. A scratch directory that cleans itself

```bash
tmp=$(mktemp -d)
{ ...work... } always { rm -rf $tmp }
```

`always` is zsh's try/finally: the
second block runs even if the first
errors or is interrupted — the right
shape for cleanup, lock release and
"put the terminal back" code.

## 6. Repeat a check until it passes

```bash
until curl -sf http://127.0.0.1:8080/ >/dev/null; do sleep 2; done
echo up
```

Nothing zsh-specific here except the
reminder that `until` exists and reads
better than `while !` — and that
chapter 7's history will remember the
one-liner whole, so next time it is
two keystrokes away.
