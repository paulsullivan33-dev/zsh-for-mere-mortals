# What Zsh Is

You type commands; a program reads them,
runs the ones that name programs, and
keeps the whole conversation feeling
instant and forgiving. That program is a
**shell**. **Zsh** — pronounced "zee
shell", named the Z shell after a Yale
login, `zsh`, belonging to an early
contributor — is one of the oldest and
most capable shells still in daily use.
It began in 1990 as a student's project
to build a better Bourne shell, and it
has been accumulating good ideas ever
since: a completion system that can be
taught new tricks per command, globbing
(filename patterns) powerful enough to
replace small scripts, a prompt you can
bend into an instrument panel, and a
line editor with thirty years of polish.

**Outcome of this chapter: you can say
what zsh is, what it is not, and whether
it is likely to be your kind of shell.**
The check is the last section: if the
reader it describes sounds like you, the
rest of the guide is worth your time.

Zsh is the default shell on macOS — it
has been since 2019 — so if you use a
Mac terminal you have probably already
met it, possibly without noticing. On
Linux it is one package away. It is
largely compatible with Bash for the
scripts and habits you already have,
but it is *not* Bash, and chapter 10 is
devoted to the handful of differences
that bite people who assume otherwise.

Three ideas organise everything zsh
does, and this guide follows them:

- **The shell is configured by files in
  your home directory**, above all
  `~/.zshrc`. Almost every feature in
  this guide is switched on, tuned or
  defined there (chapters 4 and 5).
- **Options are named switches**
  (`setopt` / `unsetopt`). Zsh has over
  190 of them; this guide uses about a
  dozen, each introduced when it earns
  its place. The defaults are sensible
  but conservative — several of zsh's
  best features are off until you ask.
- **The interactive experience is the
  point.** Zsh can run scripts and does
  it well, but its riches — completion,
  globbing at the prompt, shared
  history, spelling correction — are
  aimed at the person typing, not the
  script file.

## A first taste

In a zsh session, with the setup this
guide builds, an ordinary moment looks
like this (transcript `t03` has the
full session):

```text
zsh> cat rep[TAB]
```

Tab does not merely finish the filename.
The shell works out that both
`report-2024.txt` and `report-2025.txt`
fit, completes the part they share —
`report-202` — and, on a second Tab,
lists what remains. Completion knows
about commands, options, users, hosts,
git branches and hundreds of other
things, and chapter 5 shows how to teach
it a command of your own.

## What it is not

Zsh is not a programming language project
you must learn before touching it: at
the prompt it behaves like the shell you
know, and the differences arrive one
feature at a time. It is not a terminal
emulator — it runs *inside* Terminal,
iTerm, GNOME Terminal and their kin, and
would run just as happily on a bare
console. It is not a plugin framework:
one famous framework, Oh My Zsh, is
built *on* zsh, and chapter 12 is honest
about what it adds and what it costs.
And it is not POSIX-strict by default:
zsh aims at the Bourne tradition with
its own judgment, which is precisely why
chapter 10 exists.

## Who it is for

The Mac user who wants the terminal they
already have to stop feeling dumb. The
Linux user who lives at a prompt and
wants completion and history that work
as hard as they do. The Bash user who is
mostly happy but keeps tripping over
quoting, splitting and one-based arrays
— zsh removes several of those traps by
design. And the tinkerer: no mainstream
shell rewards an hour with its manual
quite like this one.

## The honest catch, up front

Zsh's power is *opt-in and textual*.
Nothing is set up until a file in your
home directory says so, the configuration
language is the shell language itself,
and the community's favourite answers
online often assume a framework (Oh My
Zsh) that this guide deliberately teaches
you to live without first — so that if
you adopt one later, you know what it is
doing on your behalf. Chapter 12 gives
the framework its fair hearing.
