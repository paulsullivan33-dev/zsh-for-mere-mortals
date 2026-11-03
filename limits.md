# Limits

**Outcome: you can name what zsh will
not do, so none of it surprises you in
production.** Everything here is either
demonstrated in the lab or a documented
property of the shell.

## It is not POSIX, and does not pretend

Zsh's default mode follows its own
tradition. Word splitting, array
numbering and echo escapes differ from
both Bash and POSIX `sh` (chapter 10
ran the proof). Consequence: **do not
write deployment scripts in zsh** unless
every machine that runs them has zsh
and knows it. The portable script still
belongs to `#!/bin/sh` or Bash; zsh's
kingdom is the interactive prompt and
your personal tooling. There is an
`emulate sh` mode and per-option
switches (`sh_word_split`,
`ksh_arrays`) for compatibility work —
surgical tools, not a personality.

## Nothing is on until you turn it on

A bare zsh has no intelligent
completion, no shared history, no
spell correction, a minimal prompt.
Every comfort in this guide is a line
in a startup file. That is a design
stance — predictability for scripts,
blank slate for users — but it means a
fresh zsh feels *worse* than a fresh
Fish, and the first hour of ownership
is assembly. The wizard (chapter 4)
closes most of the gap; the rest is
this guide.

## Two famous comforts are not built in

Fish-style **autosuggestions** (the
grey ghost text from your history) and
**syntax highlighting** at the prompt
are *not* zsh features. They exist as
excellent community plugins
(zsh-autosuggestions,
zsh-syntax-highlighting), loaded via a
plugin manager or by hand — which means
they are third-party code in every
shell, with a maintainer who is not
the zsh project (chapter 12). Readers
who consider them essential should
budget for that, or look at Fish.

## The configuration surface is enormous

Over 190 options, hundreds of `zstyle`
contexts, 500+ completion functions —
zsh can almost always be made to do
the thing, and the manual will take
real reading to find how. Answers
online age unevenly (advice from the
compctl era still circulates; compctl
is the *previous* completion system,
kept for compatibility). This guide
deliberately covers the modern system
and a working subset of the whole.

## Globbing's power cuts once each way

`rm **/*.tmp` across a tree is one
keystroke, and `(N)`, `nomatch` and
recursive patterns in a *script* can
select more than the author pictured —
the same reach that makes chapter 6
delightful makes an unreviewed
recursive delete unforgiving. Zsh will
not stop you; `setopt rm_star_wait` and
the dry-run habits of chapter 11 are
the guardrails that exist.

## Your history file is a diary

`~/.zsh_history` is plain text: every
command, including the ones with tokens,
passwords-as-arguments and private
paths that tools sometimes demand.
`hist_ignore_space` (chapter 7) exists
for a reason — lead a sensitive command
with a space and it never reaches the
file — shared machines multiply the
concern, and anything that backs up
your home directory backs up your
command diary with it. Chapter 7 names this plainly
because a memory you configure is a
memory you are responsible for.
