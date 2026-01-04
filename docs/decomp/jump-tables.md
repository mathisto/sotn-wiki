---
title: "Decompiling functions with jump tables"
---

-   Functions with jump tables will load an address named `jpt_XXXXXXXX` or `jtbl_XXXXXXXX` and jump to it using `jr`.

### Creating a scratch on decomp.me

-   Copy the function assembly into the "Target Assembly" field.
-   Copy the jump tables below the function assembly. Make sure you have `.section .rodata` before the jump tables.
-   The result should look similar to the following:

```
.set noat      /* allow manual use of $at */
.set noreorder /* don't insert nops after branches */

glabel MyFunction
... (function asm continues here)

.section .rodata

glabel jtbl_801A7B40
... (jump table continues)

glabel jtbl_801A7B58
... (jump table continues)
```

-   The jump tables will not be visible in the Target/Current panes of the editor, but if the decompilation shows one or more switches then it worked.

### Adding to the repo

-   When decompilation is complete these functions need to have the `.rodata` where the jump table is located ignored. The new jump table from the decompiled function will be used instead.
-   This is done by modifying the splat yaml. The jump table needs to be extracted to its own file like this:

```
      - [0x3B560, rodata] # jpt_800E55C4
      - [0x3B720, rodata]
```

-   We have a tool, `tools/split_jpt_yaml/split_jpt_yaml.py` to automate part of this process.
-   It splits all of the jump tables into their own files. Usage is like this:
-   It's possible the tool has already been run on the overlay you are looking at, in that case, you don't need to run it again.

```
# split DRA (uses jpt_ prefix)
# python3 tools/split_jpt_yaml/split_jpt_yaml.py config/splat.us.dra.yaml asm/us/dra/data/ jpt_

# split NO3 (uses jtbl_ prefix)
# python3 tools/split_jpt_yaml/split_jpt_yaml.py config/splat.us.stno3.yaml asm/us/st/no3/data/ jtbl_
```

-   Look for the `Cut below this line:` print and copy the output below that.
-   Paste the resulting output back into the yaml. For example in `DRA`:

```
segments:
  - name: dra
    type: code
    start: 0x00000000
    vram:  0x800A0000
    subalign: 4
    subsegments:
      (paste output here)
```

-   The new function needs to be split into a new file. For example if our original C file is the following, and we want to decompile `func_80133BDC`, `func_80133BDC` needs to be at the start of the new file.

```
// 75F54.c
INCLUDE_ASM("asm/us/dra/nonmatchings/75F54", func_80133960);
INCLUDE_ASM("asm/us/dra/nonmatchings/75F54", func_80133BDC);
INCLUDE_ASM("asm/us/dra/nonmatchings/75F54", func_80133FCC);
```

-   So we will have:

```
// 75F54.c
INCLUDE_ASM("asm/us/dra/nonmatchings/75F54", func_80133960);

// 93BDC.c
INCLUDE_ASM("asm/us/dra/nonmatchings/93BDC", func_80133BDC);
INCLUDE_ASM("asm/us/dra/nonmatchings/93BDC", func_80133FCC);
```

-   The function contains `jpt_80133C10` as the jump table. So we will modify the yaml like this:

```
# before
      - [0x4208C, rodata] # jpt_80133C10
      - [0x420B4, rodata] # jpt_80135058

# after
      - [0x4208C, .rodata, 93BDC] # jpt_80133C10
      - [0x420B4, rodata] # jpt_80135058
```

-   The `.` in `.rodata` indicates that the segment should be ignored in the final compilation and the table from `93BDC.c` should be used instead.
    
-   Make sure to change the file paths for the `INCLUDE_ASM`s.