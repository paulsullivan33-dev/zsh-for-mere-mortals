# Glossary

**Alias** — a textual substitution made
as a command line is read. Regular
aliases expand only in command position;
**global aliases** expand anywhere;
**suffix aliases** run a program when a
file with that extension is typed as a
command.

**autoload** — "load this function when
it is first used." The mechanism behind
`compinit`, the prompt themes and your
own function library on `fpath`.

**compinit** — the registrar of the
completion system: scans `fpath` for
`_command` definitions and caches the
index in `.zcompdump`.

**Completion system (compsys)** — the
library of per-command completion
functions plus the machinery that calls
them when Tab is pressed.

**Extended glob** — the second pattern
language (`~` exclusion, `^` negation,
`#` repetition, `<n-m>` numeric ranges)
enabled by `setopt extended_glob`.

**fc** — the shell builtin that lists,
edits and reruns history events.

**fpath** — the list of directories
searched for autoloadable function
files, completions included.

**Glob qualifier** — a parenthesised
filter after a pattern — `(.)` plain
files, `(/)` directories, `(mh-1)`
modified within the hour, `(N)` allow
no matches — testing each name the
pattern produced.

**HISTFILE / HISTSIZE / SAVEHIST** —
where history is saved, and how many
lines are kept in memory and in the
file.

**Modifier** — a `:x` suffix that
transforms an expansion: `:h` directory
part, `:t` filename part, `:r` name
without its extension.

**nomatch** — the default behaviour (and
option) by which a pattern with no
matches stops the command with an
error, instead of passing through as
literal text.

**Oh My Zsh** — the best-known
configuration framework for zsh: themes,
plugins, and a managed `.zshrc`;
chapter 12 gives it its hearing.

**PROMPT (PS1) / RPROMPT** — the strings
drawn as the prompt, left and right;
`%` introduces escapes such as `%n`
(user), `%m` (host), `%~` (directory).

**prompt_subst** — the option that makes
the prompt re-run `$( )` substitutions
at every draw, enabling live segments
like a git branch or a clock.

**setopt / unsetopt** — how options are
switched on and off; `setopt` alone
lists those that differ from default.

**share_history** — the option family
(`inc_append_history`, `share_history`)
by which all your shells write to and
read from one history file as they run.

**Word splitting** — breaking an
unquoted expansion into separate words
on spaces. Bash does it by default;
zsh does not (see `sh_word_split`).

**zle** — the zsh line editor: the part
that owns keystrokes, `bindkey`, and
editing the command line.

**zsh-newuser-install** — the first-run
configuration wizard; runs when a user
has no startup files, and never as
root.

**zstyle** — the command that styles
the completion system (and other
libraries): contexts, matchers, formats
and colours.

**ZDOTDIR** — the variable that says
where "your" startup files live, if not
in `$HOME`; the lab used it to keep
every experiment in a scratch folder.
