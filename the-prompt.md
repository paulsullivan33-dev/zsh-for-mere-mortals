# The Prompt — Yours, Without a Framework

**Outcome: you can build a prompt that
shows who you are, where you are, and
how the last command ended — coloured,
if you like — using nothing but zsh
itself.** The lab rendered every prompt
below with `print -P`, which expands a
string exactly as the prompt does
(transcript `t06-prompt.txt`), so what
is printed here is what the terminal
would draw.

## The string and its escapes

The prompt is the variable `PROMPT`
(also spelled `PS1`). Inside it, `%`
introduces an escape:

```bash
PROMPT='%n@%m %~ %# '
```

renders, for the lab's shell, as:

```text
root@myhost ~ #
```

The working set of escapes is small:
`%n` your username, `%m` the machine's
short name, `%~` the current directory
(with your home collapsed to `~`), `%#`
a `#` for root and `%` for everyone
else — which is why examples online
seem to end in either. Add `%*` for the
time, `%d` for the full path when `~`
abbreviation hides too much, and `%?`
for the last command's exit status.

## Say how the last command ended

A prompt that reports failure is the
single most useful customisation there
is. Zsh prompt strings contain a small
conditional syntax, `%(?.true.false)` —
"if the last exit status was 0":

```bash
PROMPT='%(?.ok.oops %?) %~ %# '
```

```text
$ false →  oops 1 ~ #
$ true  →  ok ~ #
```

(Transcript `t06` runs exactly this.)
Real prompts use colour or a symbol
instead of words; the mechanism is the
same, and the message is the one you
want: *the last thing I ran failed,
and here is its code*, visible before
you type the next command, not three
screens later.

## Colour

`%F{green}` starts a colour, `%f` ends
it; `%B`/`%b` do bold. The lab rendered
`%F{green}%~%f %# ` and printed the raw
codes to prove what the terminal
receives:

```text
ESC[32m ~ ESC[39m #
```

Colours are by name — black, red,
green, yellow, blue, magenta, cyan,
white — or by number (`%F{208}`) for the
256-colour palette. Restraint is a
feature: a prompt that shouts in four
colours gets ignored in all of them.

## A prompt that recomputes: prompt_subst

By default the prompt string is fixed
text with `%` escapes. One option,

```bash
setopt prompt_subst
```

makes the shell also run command and
variable substitutions inside `PROMPT`
*at every draw*. The lab put a clock in:

```bash
tick() { date +%T; }
PROMPT='[$(tick)] %~ %# '
```

and consecutive renders, two seconds
apart, printed `[01:03:02]` then
`[01:03:04]` — the function re-ran each
time. This is how prompts show git
branches, battery levels and the like:
a function computes a fact, the prompt
displays it. Two disciplines keep it
sane: keep the function *fast* (it runs
before every single prompt), and never
let it print errors into the prompt —
a failing substitution draws its
complaint across your screen each time.

## Themes, and the right-hand side

You do not have to compose strings by
hand to start. `autoload -Uz promptinit;
promptinit` loads the built-in theme
library, `prompt -l` lists the themes,
and `prompt adam1` (the wizard's choice)
applies one — themes are just somebody
else's well-tested `PROMPT` strings.
There is also `RPROMPT`, drawn at the
right edge of the line and erased the
moment you type over it — the tidy home
for the clock and the exit status, out
of the way of the command itself:

```bash
RPROMPT='%*'
```

Chapter 12 meets the frameworks that
take all of this further. Everything
they display, though, is assembled from
the pieces on this page — escapes,
conditionals, and functions run by
`prompt_subst`.
