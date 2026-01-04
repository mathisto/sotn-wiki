---
title: "FAQ"
---

# Background
There's been a large uptick in requests to do various tasks on the decomp. The purpose of this page is explaining the current status and difficulties with these tasks. Generally these tasks require 100s or 1000s of hours of work.

# Port Saturn Content to PSX
## Saturn Maria
Richer on Saturn needs to be completed first since Maria is going to be based on him and we want to leverage the existing work on Richter on PSX. The current status of Richter on Saturn can be seen in this file: https://github.com/Xeeynamo/sotn-decomp/blob/master/src/saturn/richter.c

## Underground Garden / Cursed Prison
We haven't decompiled enough of an existing shared level to add one of these. The Warp Room and Alchemy Lab have been started but are in a very basic state. The Saturn version is much harder to work on because of a lack of a decompiler. Alchemy Lab can be seen here: https://github.com/Xeeynamo/sotn-decomp/blob/master/src/saturn/stage_02.c

# Add Japanese PSX versions
This is significantly less difficult than the Saturn work but is very tedious. Splat yamls need to be created for all ~70 overlays, any code differences figured out, and all the data/code splits figured out.

# Custom characters
Mods for custom characters in game [have been prototyped](https://github.com/Xeeynamo/sotn-player-mmx), so we know it is possible given someone dedicated enough to work on it.

# PC Port
There's a number of difficulties with making a PC port. The PSX version uses the Psy-Q API directly with no abstraction, so a Psy-Q emulation layer would need to be used. There's also portability problems with the usage of 32-bit pointers for 64-bit systems. The original game also has various bugs that work by accident like dereferencing null pointers or reading past the end of arrays.