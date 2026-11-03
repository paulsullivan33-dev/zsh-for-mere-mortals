# Installing Zsh

**Outcome: a `zsh` on your machine that
states its version, and a clear picture
of the one step this guide does *not*
do for you — making it your login
shell.** The lab's machine already had
zsh in its package list; the checks
below are the ones that prove any
install, fresh or found.

## On Linux: the package manager

On Debian and Ubuntu:

```bash
sudo apt update
sudo apt install zsh
```

On Fedora it is `sudo dnf install zsh`;
on Arch, `sudo pacman -S zsh`. The
guide's lab machine reports (transcript
`t00-version.txt`):

```text
$ zsh --version
zsh 5.9 (x86_64-ubuntu-linux-gnu)

$ dpkg -l zsh | tail -1
ii  zsh  5.9-6ubuntu2  amd64  shell with lots of features
```

Zsh is a small, dependency-light
install — one program, its function
library under `/usr/share/zsh/`, and a
set of system startup files under
`/etc/zsh/` that you should know exist
but rarely edit.

## On macOS: already there

Every Mac since macOS Catalina (2019)
ships zsh as the default shell, and
Apple's copy is a recent 5.x release.
`zsh --version` in Terminal tells you
which. Homebrew offers a newer one
(`brew install zsh`) for readers who
want it; the two coexist, and everything
in this guide works on either.

## The acceptance test

Three questions, all answerable in one
sitting:

```bash
which zsh          # where the program lives
zsh --version      # what it is
zsh -c 'echo $ZSH_VERSION; echo $ZSH_PATCHLEVEL'
```

The lab's answers: `/usr/bin/zsh`,
`zsh 5.9 (x86_64-ubuntu-linux-gnu)`, and
patch level `ubuntu/5.9-6ubuntu2` — the
last is the distributor's stamp, and it
is why two machines can both say "5.9"
and differ in small behaviours.

## Trying it without committing

You do not have to change anything
permanent to follow this guide. From any
shell, type:

```bash
zsh
```

You are in zsh until you type `exit`.
Nearly everything here — configuration,
completion, globbing, history, prompts —
works in a session started this way.
That is exactly how the lab worked: it
never touched the machine's login shell.

## Making it your login shell

When you are ready, two conditions and
one command. The conditions: the zsh you
want must be listed in `/etc/shells`
(the lab's lists `/usr/bin/zsh` three
times over — package, snap and manual
entries all count once). The command:

```bash
chsh -s /usr/bin/zsh
```

It asks for your password, and the
change takes effect at your *next*
login, not in windows already open. To
go back, `chsh -s /bin/bash`. The lab
describes this step rather than running
it — changing the login shell of the
account that builds a guide is the kind
of side effect a lab notebook should not
have — so treat this paragraph as
documented procedure, verified in its
parts (the `/etc/shells` listing and the
version checks are in transcript `t00`)
rather than as a run it performed.

One warning worth heeding: on macOS,
use System Settings (Users & Groups,
right-click your account, Advanced
Options) or `chsh` the same way, and do
not edit `/etc/passwd` or its macOS
equivalent by hand on any system.
