# Zsh for Mere Mortals

Every time you open a terminal, a shell
is the program receiving what you type.
On a Mac, that shell is already **zsh**;
on Linux it is one package away. In its
bare state, though, zsh can feel oddly
plain for a shell with thirty years of
reputation: no clever completion, no
shared history, a minimal prompt. Almost
everything zsh is famous for is
*switched on by a file in your home
directory* — and most guides either hand
you a framework that writes that file
for you, opaquely, or quote settings
without showing what they do.

This guide takes the other road. It
starts the shell with an empty home
directory and meets the configuration
wizard that greets a first-run user. It
takes apart the `.zshrc` that wizard
writes, block by block. Then it builds
the working shell by hand: the
completion system (including teaching it
a command of your own), globbing
patterns that do a finding tool's job,
a history shared between shells, and a
prompt assembled from the shell's own
escapes — no framework, no plugins —
before giving the frameworks their fair
hearing at the end, measured rather
than dismissed.

The lab behind this guide ran **zsh
5.9** (Ubuntu's `5.9-6ubuntu2`) on a
small Linux machine, with every
experiment fenced into a scratch home
directory via `ZDOTDIR`, so nothing
touched a real configuration. At a real
terminal — driven keystroke by
keystroke and recorded — it completed
filenames, names and its own custom
command; it shared history between two
sessions; it rendered prompts with
`print -P`, the same expansion the
prompt itself uses. In a fixture tree
of invented files it globbed by type,
age and number range, and it ran Bash
and zsh side by side on identical text
to show exactly where they part. It
also broke things on purpose: a
`.zshrc` with a bad option and an open
quote, a completion directory with
unsafe permissions, a spelling the
shell offered to correct.

What the lab did not do, it did not
fake. It never changed the machine's
login shell, so `chsh` is taught as a
verified-in-parts procedure, not a run.
Oh My Zsh was genuinely loaded and
measured, but its rival frameworks are
characterised from their documentation.
And the two comforts zsh does not ship
— autosuggestions and syntax
highlighting at the prompt — are named
as the third-party plugins they are,
not quietly implied. `criteria.md`
keeps the full ledger.

## What this guide covers

- [**What Zsh Is**](what-zsh-is.md) —
  the model: a Bourne-tradition shell
  whose riches are interactive, and
  switched on by you
- [**The Moving Parts**](the-moving-parts.md) —
  the program, the startup files, the
  line editor, the completion system,
  and the control panel of options
- [**Installing Zsh**](installing-zsh.md) —
  the package, the version checks, and
  the login-shell step, flagged honestly
- [**First Run and Startup Files**](first-run-and-startup-files.md) —
  the new-user wizard, the `.zshrc` it
  writes taken apart, and the proven
  order of all four startup files
- [**Completion — the System That Learns**](completion.md) —
  `compinit`, what Tab really does,
  case-tolerant matching, and writing a
  completion for your own command
- [**Globbing — Patterns That Do Real Work**](globbing.md) —
  `**`, qualifiers for type and age,
  extended glob, and `no matches found`
- [**History — a Memory You Configure**](history.md) —
  the variables, the sharing and
  de-duplicating options, and using the
  memory with `fc` and `!!`
- [**The Prompt — Yours, Without a Framework**](the-prompt.md) —
  escapes, colour, exit-status reporting
  and live segments via `prompt_subst`
- [**Aliases and Functions**](aliases-and-functions.md) —
  regular, global and suffix aliases;
  functions, and one-function-per-file
  with `autoload`
- [**Coming from Bash — the Differences That Bite**](coming-from-bash.md) —
  arrays from one, no word splitting,
  glob errors, echo escapes — each run
  under both shells
- [**Recipes**](recipes.md) — jump to a
  file's folder, pattern renames with
  `zmv`, newest-file selection, the
  `always` cleanup block
- [**The Neighbours**](the-neighbours.md) —
  Bash, Fish, Oh My Zsh measured and
  weighed, the plugin managers, and
  Starship
- [**Limits**](limits.md) — not POSIX,
  nothing on by default, two comforts
  that are plugins, and your history
  file is a diary
- [**Troubleshooting**](troubleshooting.md) —
  settings that "do nothing", startup
  errors that scroll past, insecure
  completion directories, the missing
  wizard
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Writing portable scripts — for scripts
other machines must run, the guide says
plainly to keep using `sh` or Bash, and
chapter 10 explains why. The plugin
ecosystem in depth (individual plugins
are characterised, not installed). The
`compctl` system, zsh's previous
completion machinery, kept for
compatibility and now of historical
interest. Programming zsh as a language
beyond what an interactive user needs —
its parameter flags alone could fill a
guide, and this one stops at the ones a
daily user will actually meet.

## How to use this guide

Read chapters 1 and 2 for the model,
chapter 4 before editing anything —
knowing which file is read when turns
later confusion into a named problem.
Chapters 5 to 9 each end with a feature
running in your own shell; chapter 10
is the one to read twice if you arrive
from Bash. The lab's transcripts live
in `zsh-lab/transcripts/`, its fixture
tree in `zsh-lab/fixtures/`, and the
sample configuration files it used
beside them, so every claim can be
re-run, not just read.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Bash for Mere Mortals](https://paulsullivan33-dev.github.io/bash-for-mere-mortals/)
- [Fish for Mere Mortals](https://paulsullivan33-dev.github.io/fish-for-mere-mortals/)
- [Starship for Mere Mortals](https://paulsullivan33-dev.github.io/starship-for-mere-mortals/)
- [Atuin for Mere Mortals](https://paulsullivan33-dev.github.io/atuin-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/zsh-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/zsh-for-mere-mortals/blob/main/LICENSE-CODE).
