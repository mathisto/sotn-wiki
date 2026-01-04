---
title: "Decompilation"
---

# Start decompiling and contribute

This page aims to help newcomers to help contributing into the project.

## Set-up

Be sure to follow the [Build guide](https://github.com/Xeeynamo/sotn-decomp/wiki/Build) first.

Open your `~/.zshrc` or `~/.bashrc` and add the following aliases to make the process more streamlined:

```
alias sotn="make clean && make -j extract && make -j build && make expected"
alias dec=".venv/bin/python3 ./tools/decompile.py"
alias differ=".venv/bin/python3 ./tools/asm-differ/diff.py -mow3 --overlay"
```

## Choosing a function to decompile
1. We have a list of all of the functions in the repository sorted by approximate difficulty [here](https://github.com/Xeeynamo/sotn-decomp/blob/gh-duplicates/functions.md).
1. The length of the function and number of branches gives an estimate of the difficulty. Generally, if the function is longer and has more complex control flow, it's going to be harder to get a match.
1. Jtbl indicates that the function uses jump tables. These require a special process to decompile, explained [here](https://github.com/Xeeynamo/sotn-decomp/wiki/Decompiling-functions-with-jump-tables).
1. A decomp.me scratch may already exist for the file you are interested in. These are listed in the last column and can be used as a starting point for your work.
1. Check if the function is a duplicate before starting it. You may be able to either use the decompiled version as-is, or with minor adjustments. See [here](#duplicate-functions).

## Function decompilation example

1. Run `sotn` at least once and ensure to get all `OK`
1. Choose a [function](https://github.com/Xeeynamo/sotn-decomp/blob/gh-duplicates/functions.md) to decompile
1. Check if the function is a [duplicate](#duplicate-functions)
1. With a CTRL+Shift+F search the function name. You will find a line which targets its assembly counterpart (eg. `INCLUDE_ASM("st/wrp/nonmatchings/6FD0", func_801873A0);`)
1. Run `dec func_801873A0` to decompile the function in the C code
1. Do a `differ OVERLAY_NAME FUNCTION_NAME` and check if you have to fix any compilation error before proceeding (eg. differ st/wrp func_801873A0)
1. When differ succeeds, you will get a screen that shows on the left how the original assembly looks like and on the right how your decompiled version translates into.
1. Keep refactoring the code until the two assemblies match.
1. Try refactoring and perform clean-ups while ensuring your C function still matches the original assembly code.
1. Create a commit on your fork and make a PR!

## Decompiling with decomp.me
These steps involve the website https://decomp.me/ which gives an easy user interface for decompiling.
1. Figure out the file that contains your function and run `SOURCE=path/to/my/function.c make context`
1. Click "Start Decompiling" on decomp.me
1. Select "PlayStation"
1. The compiler should be `gcc 2.6.3-psx + maspsx` and the preset should be `Castlevania: Symphony of the Night`.
1. Paste ctx.c into the "Context" pane.
1. Paste the assembly for your function into the "Target assembly" pane.
1. Click "Create scratch".

## Switch between the different game builds

Currently the decomp supports the following SOTN builds:
* `us`
* `hd`
* `pspeu`
* `saturn`

To switch to a different game build, simply invoke on a terminal `export VERSION=GAME_BUILD_ID` (e.g. to decompile the PSP build, do `export VERSION=pspeu`). By default the version is set to `us`, which is the US build of SOTN for PSX.

To restore the default version in your environment, run `unset VERSION` .

## Tips and tricks

1. Use [decomp.me](https://decomp.me/) with the "Castlevania: Symphony of the Night" preset.
1. The "context" section of decomp.me, is provided by the cmd `SOURCE=src/dra/42398.c make context`.
1. Use [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) to solve some mismatches.
1. Use [this](https://github.com/mkst/sssv/wiki/Jump-Tables) and [this](https://github.com/pmret/papermario/wiki/GCC-2.8.1-Tips-and-Tricks) guide to understand how some compiler patterns work.
1. Use the `#ifndef NON_MATCHING` if your code is logically equivalent but you cannot yet fully match it.
1. Some SotN specific register tricks can be found [here](https://github.com/Xeeynamo/sotn-decomp/wiki/Register-Mismatch-Decompilation-Tricks).

## Jump tables

See [Decompiling functions with jump tables](https://github.com/Xeeynamo/sotn-decomp/wiki/Decompiling-functions-with-jump-tables)

## The `rodata` section and strings

TODO

## Duplicate functions

Due to how the game is structured, a lot of duplicate code can be found across the different overlays. We track a [live list of duplicate functions](https://raw.githubusercontent.com/Xeeynamo/sotn-decomp/gh-duplicates/duplicates.txt). If you aim to decompile a duplicated function you might get around by just copy&pasting it into the right overlay

## Add new overlay

The game has multiple overlays, one for each [stage](https://github.com/Xeeynamo/sotn-decomp/wiki/Internals#stage), boss, and familiar. Adding new overlays to the decompilation requires prior agreement, either through GitHub Issues or via our Discord Server. This is because adding a new overlay significantly increases the project scope. Gradually adding overlays allows us to better tackle duplicate code and identify common patterns to automate the process.

If you're interested in adding a new overlay, please contact us. You can also add the same overlay from another version of the game. The reference version is `us`, but we're open to overlays from `hd`, `pspeu`, `eu`, `hk` and so on.

Below are the steps to add a new overlay, using `cen` with version `hd` as an example. You can also refer to [this pull request](https://github.com/Xeeynamo/sotn-decomp/pull/1608) for guidance.

### Get an OK with a new overlay 

1. Generate the splat config (e.g. `VERSION=hd tools/make-config.py cen`).
1. Add the SHA1 checksum of the targeted overlay in `config/check.{VERSION}.sha`.

After these steps, running `VERSION=hd make -j` should complete the process and give you an :ok:. Be sure the build path matches the version and overlay name of what you're targeting. Though time-consuming, this is just the first part.

### Add the overlay to the toolchain

1. In the `Makefile` add the new overlay to the `force_symbols`.
1. In the `Makefile` add the new overlay to the `disk_prepare`.
1. Add the overlay as a new `SrcAsmPair` object in `tools/dups/main.rs`.

### Add the overlay to the Progress Page

1. Add the overlay as a new `DecompProgressStats` object in `tools/progress.py`.
1. Add the overlay paths `asset_path`, `src_path`, `splat_config_path` to `assets.[version].yaml` to support decomp.dev

### Add any new source files to your commit

1. Find any source files generated by splat (e.g. `src/{type}/{overlay}/{VERSION}.c`) and add them to commit
1. Create an overlay header file and add it to the commit. For stages this is in the format (where `{OVERLAY}` is the overlay name:
```lang=c
// SPDX-License-Identifier: AGPL-3.0-or-later
#ifndef {OVERLAY}_H
#define {OVERLAY}_H

#include <stage.h>

#define OVL_EXPORT(x) {OVERLAY}_##x
#define STAGE_FLAG OVL_EXPORT(STAGE_FLAG)

typedef enum EntityIDs {
} EntityIDs;

#endif // {OVERLAY}_H
```

After completing these steps, submit a pull request with your changes.Additionally, make a separate pull request targeting the `docs` branch after adding the overlay to [gamemeta.js](https://github.com/Xeeynamo/sotn-decomp/tree/docs/src/gamemeta.js).

## Resources

* Project Documentation [Style Guide](https://github.com/Xeeynamo/sotn-decomp/blob/master/docs/STYLE.md)
* List of resource for sotn <https://github.com/TalicZealot/SotN-Utilities> (speedrun oriented, but still very useful).
* PS1's CPU R3000 instruction [manual](https://cgi.cse.unsw.edu.au/~cs3231/doc/R3000.pdf) and [cheat sheet](https://vhouten.home.xs4all.nl/mipsel/r3000-isa.html)
* [SOTN map viewer written in C](https://github.com/KernelEquinox/SotN-Editor)
* [PCSX emulator with debugger](https://github.com/grumpycoders/pcsx-redux/)
* [NO$PSX emulator with debugger](https://problemkaputt.de/psx.htm)
* Beginner friendly MIPS video lectures [1](https://www.youtube.com/watch?v=PlavjNH_RRU&list=PLylNWPMX1lPlmEeeMdbEFQo20eHAJL8hx), [2](https://www.youtube.com/watch?v=qzSdglU0SBc&list=PLylNWPMX1lPnipZzKdCWRj2-un5xvLLdK)