# Aliases and Functions

**Outcome: you can shorten what you
type three different ways — regular,
global and suffix aliases — and write a
function when an alias stops being
enough, including one that lives in a
file of its own.** The lab's definitions
live in `zsh-lab/zdot-a-zshrc`; the runs
are transcript `t07-aliases-functions.txt`.

## Aliases: the text is replaced before anything runs

```bash
alias ll="ls -l"
```

An alias is a *textual* substitution
that happens as the line is read: type
`ll src`, the shell runs `ls -l src`.
It takes no arguments of its own —
anything after it is simply the rest of
your line. `alias` with no arguments
lists the aliases in force; `unalias ll`
removes one. One trap the lab met head-
on: an alias defined *in the same line*
as its first use does not apply — the
shell reads the whole line before
running any of it, so the alias did not
exist yet when `ll` was read. Aliases
live in `.zshrc` precisely so they are
defined before you start typing.

## Global aliases: expansion anywhere

```bash
alias -g LOG="| tee run.log"
```

A global alias expands *wherever it
appears* on the line, not just in
command position:

```text
$ echo first line LOG
first line
first line        (once to the screen, once into run.log)
```

The classic uses are exactly this shape:
`| less`, `| grep pattern`, `2>/dev/null`
— suffixes you bolt onto any command.
They are powerful and therefore slightly
dangerous: pick names (all capitals is
the convention) that you will never type
by accident as data, because zsh *will*
expand them inside what you meant to be
plain text.

## Suffix aliases: the file chooses the program

```bash
alias -s md="head -n 2"
```

Now typing a filename whose extension
is `md` *runs* the associated command on
it:

```text
$ notes.md
sample contents for notes.md
```

Suffix aliases have their own list —
`alias -s` shows them, plain `alias`
does not, which puzzled the lab for a
minute and will puzzle you too if nobody
warns you. Readers use them for
`pdf`, `tar.gz`, image extensions: any
file type where "open it" means one
obvious program.

## Functions: when text substitution is not enough

The moment you need arguments in the
middle, a condition, or a local
variable, write a function:

```bash
count() {
  local n=$(ls "$1" | wc -l)
  echo "$1 holds $n entries"
}
```

```text
$ count photos
photos holds 4 entries
```

Functions are real shell code: `$1`,
`$2`, … are the arguments, `local` keeps
variables private, `return` sets an
exit status. `whence -f count` prints
the definition back (the lab's
transcript shows it), `whence -v` says
where it came from, and `unfunction
count` removes it. Prefer functions to
aliases for anything you would be
embarrassed to explain — an alias that
needs quoting gymnastics is a function
asking to be written.

## Autoload: one function per file

A library of your own commands should
not all be parsed at every startup.
Put each function in a file named after
it, in a directory on `fpath`:

```text
# file: ~/zsh-labwork/fpath/shout
echo ${@:u}
```

```bash
fpath=(~/zsh-labwork/fpath $fpath)
autoload -Uz shout
```

Nothing is read yet. The first time you
run `shout hello from a file`, zsh
loads the file, and the lab got
`HELLO FROM A FILE` — `${@:u}` is zsh's
parameter flag for "upper-case the
arguments", a taste of how much string
handling is built in. Afterwards
`whence -v shout` reports "a shell
function from …/fpath/shout": the same
mechanism the system itself uses for
`compinit`, the prompt themes, and the
wizard of chapter 4.
