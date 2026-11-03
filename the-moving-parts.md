# The Moving Parts

**Outcome: you can name the six parts a
zsh session is assembled from, and say
which part to blame when something
behaves unexpectedly.** The check: each
part below is paired with the command
that inspects it, so by the end you can
run `echo $ZSH_VERSION`, `setopt` and
`whence -v compinit` and know what the
answers mean.

## The shell itself

One program, `/usr/bin/zsh` on this
guide's machine, version **5.9**. It
parses what you type, expands patterns
and variables, runs programs, and draws
the prompt. Everything else on this page
is either a file the program reads, a
library it can load, or a function
written in its own language.

```bash
zsh --version
```

```text
zsh 5.9 (x86_64-ubuntu-linux-gnu)
```

## The startup files

Before your first prompt, the shell
reads a fixed sequence of files — some
from `/etc/zsh/`, then from your home
directory (or from `$ZDOTDIR`, if set,
which is how this guide's lab kept its
experiments out of the author's real
home). Which of them run depends on
whether the shell is a *login* shell and
whether it is *interactive*; chapter 4
walks the order with evidence. The one
you will edit is `~/.zshrc`, read by
every interactive shell.

## The line editor (zle)

The part that owns your keystrokes:
moving by words, recalling history,
editing a command before you run it,
and the Tab key's stage machinery. Its
settings are the `bindkey` command and
its own family of widgets; the completion
system plugs into it. When a key does
something surprising, zle is the part to
interrogate:

```bash
bindkey | head
```

## The completion system (compsys)

A library of functions — 965 small
files on the lab's machine, each
knowing how to complete the arguments
of a particular command — plus the
registrar, `compinit`,
that scans them once and writes a cache
(`~/.zcompdump`). It is loaded from your
`.zshrc`, styled with the `zstyle`
command, and extended by writing a
function named `_<command>` (chapter 5).

## Options, parameters, and functions

Behaviour switches (`setopt autocd`,
chapter 6 uses several) and variables
with special meanings (`HISTFILE`,
`PROMPT`, `fpath`) are the shell's
control panel. Functions you define —
in `.zshrc`, or one per file in a
directory on `fpath` and marked with
`autoload` — are how you add commands of
your own (chapter 9). Aliases are the
smaller, purely textual cousin
(chapter 9 again).

## The loadable modules

A handful of heavier machinery lives in
modules loaded on demand: `zsh/zpty`
(runs a program on a pretend terminal —
this guide's lab used it to capture
interactive sessions), `zsh/datetime`,
`zsh/files`. Most readers never name one;
they are listed here so that when a
recipe mentions `zmodload`, it is a part
you have met.

```bash
zmodload | head
```

That is the whole machine: one program,
a sequence of files, an editor, a
completion library, a control panel of
switches and variables, and a box of
optional modules. The chapters now take
them in the order you will meet them.
