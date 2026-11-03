# The Neighbours

Zsh lives among other shells and one
very famous framework built on top of
it. These are characterisations, not
benchmarks; the lab ran zsh itself
throughout, Bash alongside it for
chapter 10, and Oh My Zsh for one
measured session (transcript `t09`).

## Bash: the incumbent

Bash is the default shell of most Linux
systems and the language of most shell
scripts ever written. Its virtues are
ubiquity and stability: a Bash script
from 2005 runs today, everywhere. As an
*interactive* shell it is plainer —
completion is available but cruder,
history is per-shell unless configured,
and its defaults carry the word-splitting
behaviour chapter 10 examined. Plenty of
people sensibly keep Bash everywhere.
Zsh earns its place at the interactive
prompt, not by replacing Bash's résumé.

## Fish: the friendly one

Fish (which has its own guide in this
series) made the opposite bet from zsh:
sensible behaviour out of the box —
autosuggestions as you type, highlighting
that flags a wrong command before you
run it, completions that explain
themselves — at the price of a language
that is deliberately *not* Bourne-
compatible. If you mostly type and
rarely script, Fish's zero-configuration
polish is genuinely hard to beat. Zsh
asks you to assemble comparable comfort
from parts (this guide is that assembly
manual) and in exchange keeps the
Bourne grammar your scripts already
speak, plus the deeper completion and
globbing machinery.

## Oh My Zsh: the famous framework

Oh My Zsh is a community framework —
a managed `.zshrc` structure, **143
themes and 372 plugins** by the lab's
count of the current release — that
configures zsh for you: a themed prompt
with git status built in, and plugins
per tool (the `git` plugin alone defines
dozens of aliases: `gst` for
`git status`, `gco` for `git checkout`).
The lab loaded it for real:

```text
$ at a real terminal inside the repository, the prompt is drawn as:
➜  demorepo git:(master)
```

and measured startup at **60 ms plain
versus 77 ms** with one theme and one
plugin — on this small shared machine,
negligible. The honest ledger: Oh My
Zsh's cost is not speed at that scale;
it is *comprehension and surface area*.
Every plugin you enable is a stranger's
shell code sourced into every shell you
open — and there are 372 on the shelf
to be tempted by — startup cost grows
with each one added, and when behaviour
surprises you, the answer may live in a
plugin you forgot you enabled. Its benefit is equally
real: an afternoon of this guide's
assembly, done for you, maintained by
others. This guide's position is not
"never" — it is "second": learn what
the pieces are first (you now know
every mechanism Oh My Zsh uses:
`.zshrc`, `prompt_subst`, functions,
aliases, `fpath`), then adopt the
framework with your eyes open if its
convenience wins.

## The other frameworks: prezto, zinit, antidote

**Prezto** is the older, more curated
sibling — fewer, vetted modules, a
quieter aesthetic. **zinit** and
**antidote** are plugin *managers* in
the package-manager mould: they fetch,
version and lazily load individual
plugins (including the two most-wanted
extras zsh lacks natively —
fish-style autosuggestions and syntax
highlighting, both available as
community plugins) without a monolith.
Characterised here from their
documentation; the lab ran only Oh
My Zsh.

## Starship: the prompt from outside

Starship (its own guide in this series)
is not a shell at all but a prompt
program that works across shells,
zsh included: one configuration file,
fast Rust rendering, every segment
from git status to cloud context. If
chapter 8's hand-built prompt feels
like work, Starship is the respectable
shortcut — and because it is
shell-agnostic, what you learn carries
to Bash or Fish if you ever move.
