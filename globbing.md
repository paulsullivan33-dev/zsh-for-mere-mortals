# Globbing — Patterns That Do Real Work

**Outcome: you can select files by
name, type, age and location with one
pattern, recursively, and you know what
happens when a pattern matches nothing.**
Every pattern below ran against the
lab's fixture tree — twenty-odd invented
files, kept in `zsh-lab/fixtures/` —
in transcript `t04-globbing.txt`.

## The familiar floor

Zsh globbing starts where Bash's does:
`*` (any run of characters), `?` (one
character), `[...]` (a set), all
expanded by the shell into a sorted list
of names before the command runs.

```text
$ print -l *.txt
draft.txt
fresh-note.txt
report-2024.txt
report-2025.txt
summary.txt
```

(`print -l` is zsh's own printing
command, one argument per line — the
honest way to watch an expansion, with
no `ls` formatting in the way.)

## Deeper: `**` and qualifiers

Two extensions turn patterns into a
finding tool. `**/` crosses directories:

```text
$ print -l **/*.txt
archive/old-report-2019.txt
draft.txt
...
src/notes.txt
summary.txt
```

And **glob qualifiers** — a parenthesised
filter after the pattern — test each
match. The two you will use weekly:

```text
$ print -l *(.)       # plain files only
data-01.csv
data-02.csv
...

$ print -l *(/)       # directories only
archive
photos
src

$ print -l *(mh-1)    # modified within the last hour
(fresh-note.txt and everything made this hour;
summary.txt and photos/logo.png, touched three
hours ago in the lab, are correctly absent)
```

There are qualifiers for size, owner,
permissions, links and more (`mh` is
"modified, in hours"; `m` takes other
units). The point to take away is the
shape: *pattern first, facts about the
file second*, no `find`, no pipe.

## Extended glob: the other half

One option unlocks a second pattern
language:

```bash
setopt extended_glob
```

With it, `~` inside a pattern means
"but not", and `<n-m>` matches a number
in a range:

```text
$ setopt extended_glob; print -l *.txt~draft*
fresh-note.txt
report-2024.txt
report-2025.txt
summary.txt

$ print -l report-<2024-2025>.txt
report-2024.txt
report-2025.txt
```

Note `<2024-2025>` matches the *number*,
not the text — it would also have caught
a `report-2024.txt` written with leading
zeros, and it sorts numerically. The
same option enables `#` (repeat the
preceding character or group) and `^`
(negate, at the start of a pattern) —
the trio is why scripts from the
internet sometimes fail mysteriously in
a shell that does not have it set.

Alternation, incidentally, needs no
option: `src/*.(c|h)` listed the C
sources and the header in the lab.

## When nothing matches

Here zsh parts company with Bash in a
way that protects you:

```text
$ print -l *.log
zsh:1: no matches found: *.log
```

Bash would pass the literal text `*.log`
to the command, which then fails
confusingly — or worse, creates a file
with that name. Zsh stops the line
before it runs. When you *mean* "nothing
is acceptable", say so with the `(N)`
qualifier (N for null):

```text
$ print -l *.log(N)
(prints nothing, runs fine)
```

Scripts moved from Bash often rely on
the silent pass-through; in zsh, add
`(N)` or `setopt null_glob` at the top
and the script says what it means.

## The dot at the front

Like Bash, `*` skips dotfiles; unlike
Bash, the fix is a qualifier, not a
second pattern: `.*(.)` listed the lab's
`.hidden-note`. The `glob_dots` option
makes `*` include them permanently —
think before setting it globally,
because `rm *` acquires a longer reach
the day you do.
