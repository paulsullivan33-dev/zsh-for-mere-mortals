# First Run and Startup Files

**Outcome: you know exactly which files
zsh reads before your first prompt, in
which order, and you have read a real
`.zshrc` and can say what every block in
it does.** The lab created a fresh,
empty home directory and let the shell
meet it (transcript `t01-first-run.txt`).

## The wizard

With no startup files at all, an
interactive zsh offers its configuration
helper, **zsh-newuser-install**:

```text
This is the Z Shell configuration function for new users,
zsh-newuser-install.
You are seeing this message because you have no zsh startup files
...

(q)  Quit and do nothing.  The function will be run again next time.
(0)  Exit, creating the file ~/.zshrc containing just a comment.
(1)  Continue to the main menu.
(2)  Populate your ~/.zshrc with the configuration recommended
     by the system administrator and exit
```

The lab pressed **2**, and the wizard
wrote the distribution's recommended
`.zshrc` — a better first file than most
people ever write for themselves. Two
things worth knowing before you meet it
yourself: the wizard runs only for a
user with *no* startup files (the moment
a `~/.zshrc` exists it stays silent),
and it **refuses to run as root** —
run with `-f` as root it says
`zsh-newuser-install: won't run as root`.
The lab's first attempts ran as root and
saw nothing at all; that silence is the
explanation, not a broken install.

## The file the wizard wrote, annotated

The recommended `.zshrc` (full text in
transcript `t01`) has five moves, and
they are the anatomy lesson for every
`.zshrc` you will ever read:

1. **The prompt.** `autoload -Uz
   promptinit; promptinit; prompt adam1`
   loads the prompt-theme library and
   picks a theme. `autoload` means "load
   this function when first used" — you
   will see it everywhere in zsh-land.
2. **History behaviour.**
   `setopt histignorealldups sharehistory`
   plus `HISTSIZE`, `SAVEHIST` and
   `HISTFILE` a few lines later —
   chapter 7's whole subject, in seed
   form.
3. **Key bindings.** `bindkey -e` —
   Emacs-style editing keys, set even if
   your editor is vi, so the *shell's*
   line editor behaves predictably.
4. **Completion.** `autoload -Uz compinit;
   compinit` — the completion system of
   chapter 5, switched on.
5. **Completion styling.** A block of
   `zstyle ':completion:*' ...` lines:
   how candidates are described, grouped,
   coloured and matched — including a
   matcher that lets lower-case typing
   complete mixed-case names. Chapter 5
   explains the ones that matter.

That is the honest shape of `.zshrc`
files in the wild: a prompt, history,
keys, completion, styling — and then
your own additions. When you inherit
someone else's file (or a framework's),
read it in that order and it stops being
a wall of runes.

## The full order of files

`.zshrc` is one of four. Transcript
`t02-startup-files.txt` proves the order
by putting a marker line in each file
and starting every kind of shell:

| File | When it is read |
|---|---|
| `~/.zshenv` | **always** — scripts, interactive, login |
| `~/.zprofile` | login shells only |
| `~/.zshrc` | interactive shells only |
| `~/.zlogin` | login shells only, after `.zshrc` |

Measured results: a plain script shell
(`zsh -c`) read only `.zshenv`; an
interactive shell read `.zshenv` then
`.zshrc`; a login shell read `.zshenv`,
`.zprofile`, `.zlogin`; a shell that is
both read all four, in that order. A
matching set under `/etc/zsh/` runs
first at each step. Practical rules that
fall out of the table:

- Put environment variables a *script*
  might need in `.zshenv` — and keep it
  tiny and fast, because everything
  reads it.
- Put everything interactive — prompt,
  completion, aliases — in `.zshrc`.
- If a setting "works in a terminal but
  not in cron/another tool", it is
  almost certainly in `.zshrc` and the
  other context is not interactive. The
  table is how you prove it.

## The lab's trick, worth stealing

Every experiment in this guide ran with
`ZDOTDIR` pointed at a scratch directory.
`ZDOTDIR` tells zsh "my startup files
live *there*", so the lab could try a
configuration — including broken ones,
chapter 13 — without touching the real
home directory. It is the safest way to
test a borrowed `.zshrc` too:

```bash
ZDOTDIR=/path/to/scratch zsh -i
```
