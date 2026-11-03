# Troubleshooting

The failures the lab met for real,
roughly in the order a new user meets
them. Transcript `t10-failures.txt`
holds the messages unless another
transcript is named.

## My change to .zshrc "does nothing"

Three causes, in the order to check
them. First, the shell you are testing
in started *before* the edit — startup
files are read once, at startup; open
a new shell or `source ~/.zshrc`.
Second, the setting is in the wrong
file for the shell you are testing:
chapter 4's table is the authority
(interactive things belong in `.zshrc`;
a non-interactive test shell never
reads it, which is why the lab's own
first alias test failed — the alias was
defined in a `zsh -c` string and used
in the same breath, and chapter 9
explains that trap). Third, something
*later* in the file — or a framework —
set it back.

## "no such option" and the shell starts anyway

```text
~/.zshrc:setopt:2: no such option: no_such_option
~/.zshrc:4: unmatched "
```

The lab's deliberately broken `.zshrc`
produced both lines — and then the
shell started and ran the command it
was given. Zsh reports errors in
startup files *and carries on*, which
means a configuration can be silently
half-applied for weeks: the option
that failed is simply not set. The
messages name the file and line
number; believe them. To check a file
without living in it:

```bash
zsh -n ~/.zshrc
```

parses the file and reports syntax
errors — the lab's run reported the
unmatched quote at line 4 — while
saying nothing about unknown options,
which are a runtime, not a parse,
matter. Parse first, then start one
test shell and read its complaints.

## "no matches found" stops my command

Not a bug: the pattern matched nothing
and zsh refuses to guess (chapter 6).
If the command should tolerate
nothing, add the `(N)` qualifier to
that pattern. If it happens inside a
script ported from Bash, the script
was relying on Bash passing the pattern
through as text — add `(N)` or set
`null_glob` in that script, and say
which you chose in a comment, because
the next reader will wonder.

## compinit complains about insecure directories

```text
There are insecure directories:
~/zsh-labwork/badcomp
```

Completion functions are code that runs
in your shell, so `compinit` audits
the directories it loads them from and
refuses ones that strangers can write
to — a shared `fpath` directory with
loose permissions is a real attack
route, not pedantry. `compaudit` (the
lab ran it against a deliberately
world-writable directory) lists the
offenders. Fix the permissions
(`chmod 755`, owned by you or root),
or, if you understand a specific
directory to be safe, `compinit -i`
skips insecure ones silently and
`compinit -u` uses them anyway — know
which you typed.

## The wizard never appeared

You are probably root (the wizard
refuses, silently — chapter 4), or a
`.zshrc` already exists, however
empty: existence, not content, is what
silences it. To invite it deliberately:
`autoload -Uz zsh-newuser-install;
zsh-newuser-install -f`, as a normal
user, in a home whose startup files
you have moved aside.

## It corrects commands I meant literally

```text
zsh: correct 'sl' to 'ls' [nyae]? n
zsh: command not found: sl
```

That is `setopt correct` doing its job
(the lab's session, transcript `t10`:
`n` declined, and the original text
ran and failed honestly). The keys are
`y` run the correction, `n` run what
you typed, `a` abort, `e` edit the
line. If the offers annoy more than
they save, `unsetopt correct` — and
note `correct_all` exists and corrects
every word; almost nobody wants it.

## History is not being saved

Work the chain: is `HISTFILE` set
(`echo $HISTFILE`)? Is `SAVEHIST`
greater than zero? Is the shell
interactive (scripts do not save
history by design)? And is another
shell overwriting the file — the
pre-`share_history` pattern, where
each shell writes its own memory at
exit and the last exit wins. Chapter
7's three options are the fix, and
transcript `t05` shows the file they
produce.
