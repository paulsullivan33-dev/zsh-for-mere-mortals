# Completion — the System That Learns

**Outcome: Tab in your shell completes
commands, filenames, options and
arguments intelligently; you can make it
case-tolerant; and you have taught it a
command of your own.** All of it was
exercised at a real terminal in the lab
(transcript `t03-completion.txt`).

## Switching it on

Completion is not on by default in a
bare zsh. Two lines in `~/.zshrc` do it:

```bash
autoload -Uz compinit
compinit
```

`compinit` scans the directories on
`fpath` for completion definitions —
files named `_<command>`; Debian's zsh
ships hundreds, covering everything from
`git` to `ssh` — and writes a cache,
`~/.zcompdump`, so later shells start
fast instead of rescanning. (The lab's
dump was 51,147 bytes: a compiled index
of the whole function library.) If you
install a tool and its completions seem
missing, deleting `~/.zcompdump` and
starting a new shell is the first fix;
chapter 13 explains the security check
`compinit` runs while it works.

## What Tab actually does

At the prompt in a folder holding
`report-2024.txt` and `report-2025.txt`:

```text
zsh> cat rep[TAB]
```

the line becomes `cat report-202` — the
longest part both candidates share — and
the shell beeps: more than one file
still fits. A second Tab lists them:

```text
report-2024.txt  report-2025.txt
```

One more keystroke (4 or 5) and Enter
finishes the job. Where only one thing
fits, Tab completes it in full, adding
what it can: `ls ph[TAB]` became
`ls photos/` — slash included — and a
further Tab inside listed the photos.
The same machinery completes command
names, then their *options* (try
`ls --[TAB]`), option arguments, user
names after `~`, host names for `ssh`,
and — because definitions are per
command — the subcommands and branches
of `git`.

## Making it case-tolerant

By default, completion is literal:
`cat REP[TAB]` finds nothing, because no
file is named `REP*`. One `zstyle` line
changes the matching rules:

```bash
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
```

Read it as: "a typed lower-case letter
may match either case in a candidate."
The lab's transcript shows `REP`
producing the same two reports. The
wizard's recommended `.zshrc` (chapter
4) goes further, adding substring and
suffix matching; add rules one at a time
and live with each, because every rule
that makes completion more generous also
makes it occasionally surprising.

## Teaching it a command of your own

A completion is a function named
`_command` that calls `compadd` with the
candidates. The lab's `.zshrc` taught
the shell a toy command, `greet`, which
takes a person's name:

```bash
greet() { echo "hello, $1" }
_greet() { compadd alice bob carol }
compdef _greet greet
```

And at the terminal:

```text
zsh> greet a[TAB]     →  greet alice
zsh> greet alice
hello, alice
```

That is the whole pattern. Real
definitions use helpers like `_arguments`
to describe options and arguments
formally — the system's own files in
`/usr/share/zsh/functions/Completion/`
are the reference, and reading the one
for a command you use daily is an
education — but `compadd` in a function
is enough to make a personal tool feel
native. Put a bigger definition in its
own file named `_greet` in a directory
on `fpath` instead of in `.zshrc`, and
`compinit` will find it like its own.

## Living with it

Two habits complete the picture. First,
Tab is a question, not a commitment:
pressing it never runs anything, and
pressing it twice is how you ask "what
are my choices here?" — the single most
useful interrogative in shell life.
Second, when completion offers nothing,
that silence is information: usually the
previous word is complete, the directory
is wrong, or the command takes no such
argument. Believe it before you believe
your memory of the syntax.
