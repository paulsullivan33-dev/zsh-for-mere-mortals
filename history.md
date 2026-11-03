# History — a Memory You Configure

**Outcome: your shell remembers commands
in a file you control, shares them
between open shells, forgets duplicates
the way you choose, and reruns any of
them by number or by name.** The lab ran
two real sessions against one history
file (transcript `t05-history.txt`).

## The three variables

Out of the box, zsh keeps history only
in memory and may not save it at all.
Three variables give it a home:

```bash
HISTFILE=~/.zsh_history
HISTSIZE=1000      # lines kept in memory
SAVEHIST=1000      # lines kept in the file
```

The wizard's recommended `.zshrc`
(chapter 4) sets exactly these, at 1000
lines each. Raise them freely — history
files are small, and a long memory is
the difference between archaeology and
typing. `HISTFILE` is also a privacy
fact: it is a plain-text list of what
you ran, sitting in your home directory.
Know it is there (chapter 12 returns to
this).

## The options that shape it

```bash
setopt share_history        # shells share one history, live
setopt inc_append_history   # write each command as it runs
setopt hist_ignore_all_dups # a repeat replaces its older copy
```

The lab's two sessions show what these
buy. In session A, `echo alpha` was run,
then `echo beta`, then `echo alpha`
again. The listing afterwards was:

```text
zsh> fc -l 1
    2  echo beta
    3  echo alpha
```

The first `echo alpha` is *gone* —
`hist_ignore_all_dups` removed the older
copy when the command repeated, leaving
the gap in the numbering as the receipt.
(Prefer gentler policies? `hist_ignore_dups`
drops only consecutive repeats, and
`hist_ignore_space` keeps commands that
start with a space out of the file
entirely — the classic way to keep a
one-off sensitive command unrecorded.)

Session B, started after A exited,
opened with A's commands already in its
history — `share_history` reads the file
at startup and keeps following it, so
*concurrently open* shells see each
other's commands as they go, not just
the next morning. `fc -l 1` is the
listing command (`fc` is the shell's
history editor; `history` is its alias).

## Using the memory

Four moves cover daily life:

- **Up-arrow / Ctrl-R.** The arrow walks
  back one command at a time; Ctrl-R
  searches by substring as you type.
- **`!!`** reruns the last command. The
  shell shows you the expansion before
  running it — the lab's session B:

  ```text
  zsh> !!
  echo gamma
  gamma
  ```

  That echo-back is your chance to catch
  a misremembered expansion; `!!` after
  the wrong command is a classic way to
  repeat a mistake at speed.
- **`!text`** reruns the most recent
  command *starting with* `text`;
  **`!42`** reruns event 42 from the
  listing.
- **`fc 42`** opens event 42 in your
  editor instead of running it — the
  grown-up way to fix a long command
  rather than rerunning it blind.

One honest caution belongs here:
history expansion happens *before* the
line runs and ignores quoting, so a
`!` inside a sentence you paste can
expand in surprising ways. Interactive
zsh prints the expansion for approval in
the default configuration — keep that
safety on, and prefer `fc` when an
expansion would be destructive.
