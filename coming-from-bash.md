# Coming from Bash — the Differences That Bite

**Outcome: you can predict the five
places a Bash habit silently changes
meaning in zsh, because you have seen
each one run both ways.** Transcript
`t08-bash-differences.txt` runs the
*same text* under bash and zsh, side by
side. Where the outputs agree, that is
stated too — most of your Bash survives
the move.

## 1. Arrays start at 1

```text
a=(red green blue); echo "a0=${a[0]} a1=${a[1]} count=${#a[@]}"

bash:  a0=red  a1=green  count=3
zsh:   a0=      a1=red    count=3
```

Zsh numbers arrays from **1**, inherited
from the C shell tradition. `${a[0]}`
is not an error — it is politely empty,
which is worse. The option `KSH_ARRAYS`
switches to zero-based for a script
that needs it; the real fix is to stop
writing indexes that assume a base.
`${#a[@]}` (the count) agrees in both.

## 2. Unquoted variables do not split

```text
files="notes.md summary.txt"; wc -l $files

bash:  1 notes.md / 1 summary.txt / 2 total
zsh:   wc: 'notes.md summary.txt': No such file or directory
```

Bash splits an unquoted expansion into
words on spaces; **zsh does not** — the
whole string stays one argument. This
is deliberate and, once absorbed, the
single best reason to prefer zsh for
interactive work: filenames with spaces
stop being landmines. The idiom that
replaces the habit is an array:
`files=(notes.md summary.txt)`, then
`wc -l $files`. When you truly want
splitting, ask for it explicitly:
`${=files}` splits on spaces by design.

## 3. A glob that matches nothing is an error

```text
echo *.log        (no .log files exist)

bash:  *.log
zsh:   zsh:1: no matches found: *.log
```

Chapter 6's story from the other side:
Bash hands the pattern through as
literal text and lets the command deal
with it; zsh stops the line. Add the
`(N)` qualifier — `*.log(N)` — when
"none" is an acceptable answer, and
expect to add it to most scripts you
port.

## 4. echo interprets escapes

```text
echo "one\ttwo"

bash:  one\ttwo     (printed literally)
zsh:   one⇥two     (a real tab)
```

Zsh's `echo` processes backslash
escapes by default; this machine's
Bash, invoked plainly, did not. Scripts
that print `\n` or `\t` and rely on them
staying literal will change behaviour.
`print` is zsh's own, better-specified
printing command — in zsh-land, reach
for it and the ambiguity retires.

## 5. What did *not* change

Two habits transferred untouched in the
lab, and they are worth naming so the
chapter is not all warnings: testing
`$?` after a command works identically
(`false`, then `[ $? -eq 1 ]`, printed
the expected result in both), and
pattern matching on the right of `==`
inside `[[ ... ]]` matched in both.
Pipelines, redirection, quoting rules,
`$( )`, functions with positional
parameters, `for`/`while`/`case` — the
daily grammar is the same grammar.

## The escape hatch

There is no "behave like Bash" switch —
`emulate` knows `zsh`, `sh`, `ksh` and
`csh`, not Bash. What exists is better
aimed: the two behaviours above are
options, and you can ask for them
individually wherever a ported script
truly needs them. The lab verified the
pair (transcript `t08`, last section):

```bash
setopt sh_word_split ksh_arrays
```

after which the array test printed
`a0=red` and the two-word variable split
into two files for `wc`, exactly as
Bash had done. Scope them tightly —
inside the function that sources the
Bash library, where `setopt` in a
function stays local by zsh's rules —
rather than in your `.zshrc`, where
they would quietly re-arm the traps
this chapter just disarmed.
