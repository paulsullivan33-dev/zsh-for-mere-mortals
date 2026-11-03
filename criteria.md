# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's fixtures are an invented folder of sample files.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: zsh is not POSIX and is the wrong default for
   portable scripts, nothing is configured until a startup file
   configures it, autosuggestions and prompt syntax
   highlighting are third-party plugins rather than features,
   the option and styling surface is far larger than any one
   guide, globbing's reach makes recursive deletes
   unforgiving, and the history file is a plain-text diary of
   every command.
8. **The ethics rule is in the text, early.** A shell's
   configuration is code that runs as you, so chapter 4 and
   chapter 5 state the care rule plainly — read any borrowed
   `.zshrc` or completion before your shell does, and load
   functions only from directories you control (`compinit`'s
   own audit enforces the second half) — and chapters 7 and 13
   state the privacy half: your history file records what you
   ran, including anything sensitive a tool made you type, so
   it is handled like the diary it is.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran (timings are therefore
ranges, and the guide says so). Zsh **5.9** (Ubuntu package
`5.9-6ubuntu2`, patch level `ubuntu/5.9-6ubuntu2`) was used as
installed from the distribution. Every experiment ran with
`ZDOTDIR` or `HOME` pointed at scratch directories, so no real
configuration was read or written; the sample `.zshrc` files
the lab used are kept in `zsh-lab/` as `zdot-*-zshrc`.
Interactive sessions were driven keystroke by keystroke on a
real terminal (the driver is `zsh-lab/drive.py`) and their
transcripts have terminal control sequences removed and local
machine and path names normalised; the outputs shown are the
outputs the shell produced. All transcripts live in
`zsh-lab/transcripts/`; the fixture tree is
`zsh-lab/fixtures/tree/`.

Run for real, with transcripts as evidence:

- Version, patch level, package state, `/etc/zsh/` contents and
  the `/etc/shells` listing (t00).
- The first run: a scratch home with no startup files, the
  new-user wizard appearing by itself, option (2) chosen, and
  the full distribution-recommended `.zshrc` it wrote, read
  back and annotated in chapter 4. The wizard's refusal to run
  as root was established both from its behaviour (two root
  attempts, no wizard) and its source (t01).
- Startup-file order, proven with marker lines in each of
  `.zshenv`, `.zprofile`, `.zshrc`, `.zlogin` across
  non-interactive, interactive, login, and login+interactive
  shells (t02).
- Completion at a real terminal: common-prefix completion,
  candidate listing, case-insensitive matching via
  `matcher-list`, the hand-written `_greet` completion
  completing a name, and directory completion with contents
  (t03). The `.zcompdump` cache's existence and size were
  observed directly.
- Globbing in the fixture tree: plain, recursive `**`,
  qualifiers `(.)`, `(/)`, `(mh-1)` (with two files backdated
  three hours correctly excluded), extended-glob exclusion
  and the `<2024-2025>` numeric range, alternation, the
  `no matches found` error and its `(N)` remedy, and dotfile
  handling (t04).
- History across two sequential interactive sessions sharing
  one file: `share_history` visibility, duplicate removal
  under `hist_ignore_all_dups` (with the numbering gap it
  leaves), `!!` expansion echoed before running, and the
  resulting history file read back (t05).
- Prompt rendering via `print -P`: `%n@%m %~ %#`, colour codes
  shown raw, the `%(?...)` exit-status conditional after true
  and false, and a `prompt_subst` clock function re-evaluated
  across two renders two seconds apart (t06).
- Aliases and functions: regular, global (with the `tee` side
  effect verified in the file it wrote) and suffix aliases,
  the separate `alias -s` listing, a function with a local,
  and an autoloaded function loaded from its own file and
  traced with `whence -v` (t07).
- Bash and zsh on identical text: array indexing, word
  splitting, the unmatched glob, echo escapes, `$?` testing
  and `[[ == ]]` patterns (the last two agree), plus the
  `sh_word_split`/`ksh_arrays` remedy run under zsh (t08).
- Oh My Zsh cloned from its official repository and loaded:
  theme and plugin counts (143 themes, 372 plugins), the git
  plugin's aliases, the robbyrussell prompt drawn at a real
  terminal inside a git repository, and startup time measured
  best-of-five against plain zsh, 60 ms vs 77 ms (t09).
- Failures: a `.zshrc` with an unknown option and an
  unterminated quote (exact messages, shell still started),
  `zsh -n` parse checks, `compaudit` naming a deliberately
  world-writable completion directory, and `setopt correct`
  offering and being refused at a real terminal (t10).
- The recipe mechanisms: `(:h)`/`(:r)` modifiers, a `zmv -n`
  dry run, `*(om[1])`/`*(Om[1])` selection, the `always`
  block running after a failure with the status preserved,
  and the directory loop (t11).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Making zsh the login shell (`chsh -s`): the lab did not
  change the build account's login shell. Its parts were
  verified — the `/etc/shells` entries and version checks are
  in t00 — and chapter 3 labels the step as procedure.
- macOS specifics: zsh as the shipping default shell and the
  Homebrew alternative are stated from Apple's and the
  project's documentation; the lab machine is Linux.
- The neighbours of chapter 12 other than Bash and Oh My Zsh:
  Fish, prezto, zinit, antidote, zsh-autosuggestions,
  zsh-syntax-highlighting and Starship are characterised, not
  installed or benchmarked.
- Option and feature areas the guide mentions but does not
  exercise: the full qualifier and parameter-flag sets,
  `compctl`, `zsh/zftp` and other modules beyond naming them,
  and prompt themes other than adam1 (installed by the wizard)
  and robbyrussell (drawn under Oh My Zsh).

Fixtures are this guide's own and deliberately generic: a
small tree of invented text files, sample data files and fake
images under `zsh-lab/fixtures/`, example names (alice, bob,
carol) in the toy completion, and a throwaway git repository
with one file. No real person, organisation, network or
account appears anywhere in the lab.
