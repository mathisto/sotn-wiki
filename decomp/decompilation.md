# SOTN Decompilation Guide

## Setup

Add these aliases to `~/.zshrc` or `~/.bashrc`:

```bash
alias sotn="make clean && make -j extract && make -j build && make expected"
alias dec=".venv/bin/python3 ./tools/decompile.py"
alias differ=".venv/bin/python3 ./tools/asm-differ/diff.py -mow3 --overlay"
```

## Workflow

### Choosing a Function

1. Browse the [function list](https://github.com/Xeeynamo/sotn-decomp/blob/gh-duplicates/functions.md) sorted by difficulty
2. **Length + branches = difficulty** — longer functions with complex control flow are harder
3. **Jtbl** = jump tables, requires [special handling](https://github.com/Xeeynamo/sotn-decomp/wiki/Decompiling-functions-with-jump-tables)
4. Check for existing decomp.me scratches (last column)
5. Check [duplicates list](https://raw.githubusercontent.com/Xeeynamo/sotn-decomp/gh-duplicates/duplicates.txt) — may already be decompiled elsewhere

### Decompilation Steps

1. Run `sotn` and ensure all `OK`
2. Choose a function from the list
3. Check if it's a duplicate
4. Search (`Ctrl+Shift+F`) for the function name to find `INCLUDE_ASM(...)` line
5. Run `dec func_801873A0` to decompile
6. Run `differ st/wrp func_801873A0` to compare assembly
7. Refactor until left (original) and right (your code) match
8. Clean up while maintaining the match
9. Commit and PR

## decomp.me Usage

1. Generate context: `SOURCE=path/to/my/function.c make context`
2. Go to [decomp.me](https://decomp.me/) → "Start Decompiling"
3. Select **PlayStation**
4. Compiler: `gcc 2.6.3-psx + maspsx`
5. Preset: `Castlevania: Symphony of the Night`
6. Paste `ctx.c` into "Context"
7. Paste function assembly into "Target assembly"
8. Click "Create scratch"

## Switching Game Versions

Supported: `us` (default), `hd`, `pspeu`, `saturn`

```bash
export VERSION=pspeu   # Switch to PSP EU
unset VERSION          # Restore to 'us'
```

## Tips & Tricks

1. Always use [decomp.me](https://decomp.me/) with the SOTN preset
2. Generate context with `SOURCE=src/dra/42398.c make context`
3. Use [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) for stubborn mismatches
4. Reference guides: [Jump Tables](https://github.com/mkst/sssv/wiki/Jump-Tables), [GCC 2.8.1 Tips](https://github.com/pmret/papermario/wiki/GCC-2.8.1-Tips-and-Tricks)
5. Use `#ifndef NON_MATCHING` for logically equivalent but non-matching code
6. See [Register Mismatch Tricks](https://github.com/Xeeynamo/sotn-decomp/wiki/Register-Mismatch-Decompilation-Tricks) for SOTN-specific patterns

## Duplicate Functions

Many functions are duplicated across overlays. Check the [live duplicates list](https://raw.githubusercontent.com/Xeeynamo/sotn-decomp/gh-duplicates/duplicates.txt) — you may be able to copy/paste an existing decompilation.

## Resources

| Resource | Link |
|----------|------|
| Style Guide | [docs/STYLE.md](https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/STYLE.md) |
| SOTN Utilities | [SotN-Utilities](https://github.com/TalicZealot/SotN-Utilities) |
| R3000 Manual | [PDF](https://cgi.cse.unsw.edu.au/~cs3231/doc/R3000.pdf) |
| R3000 Cheat Sheet | [Link](https://vhouten.home.xs4all.nl/mipsel/r3000-isa.html) |
| Map Viewer | [SotN-Editor](https://github.com/KernelEquinox/SotN-Editor) |
| PCSX Redux (debugger) | [GitHub](https://github.com/grumpycoders/pcsx-redux/) |
| NO$PSX (debugger) | [Download](https://problemkaputt.de/psx.htm) |
| MIPS Lectures | [Part 1](https://www.youtube.com/watch?v=PlavjNH_RRU&list=PLylNWPMX1lPlmEeeMdbEFQo20eHAJL8hx), [Part 2](https://www.youtube.com/watch?v=qzSdglU0SBc&list=PLylNWPMX1lPnipZzKdCWRj2-un5xvLLdK) |
