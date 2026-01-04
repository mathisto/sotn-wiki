---
title: "Decompilation (PSP edition)"
---

## Set-up

These instructions assume Ubuntu 22.04 LTS, which is what we are testing against in our CI. It also assumes you have [installed the standard pre-requisites for the PSX build](https://github.com/Xeeynamo/sotn-decomp/wiki/Build#set-up)

export VERSION=pspeu

make update-dependencies

Dump your EU copy of Castlevania - The Dracula X Chronicles as ISO, put the file inside `./disks/`, naming the file `sotn.pspeu.iso`. Then continue with extraction, building and verifying it:

# extract disk, build and check
make extract\_disk
make extract -j && make build -j
make check

Once you have a working build you are good to continue:

```
build/pspeu/dra.bin     [ OK ]
build/pspeu/tt_000.bin  [ OK ]
build/pspeu/wrp.bin     [ OK ]
```

## Extracting overlays

PSP overlays are not fully integrated into the project's build currently. It may be necessary to extract a particular overlay you are working on to find the function in PSP.

As an example, let's use the `no3` overlay, and try to get the function for `EntityStrongWarg`.

-   Firstly, download [this script](https://gist.github.com/sozud/4c1a2f0e98c1d5d6ea09d073affd168a) locally as `psp-make-config.py`
-   Run `source .venv/bin/activate` to activate venv
-   Run `python3 psp-make-config.py no3`. This will produce a Splat config file in `./config/splat.pspeu.stno3.yaml`
-   Run `splat split ./config/splat.pspeu.stno3.yaml` to split the overlay

## Finding functions

Now that we have PSP assembly extracted to `asm/pspeu/st/no3_psp` we need to find our `EntityStrongWarg` function. This can be tricky as many of the symbols used on the PSX side are not mapped yet for PSP, so we need to rely on detective skills and intuition.

Tips:

-   Try to find something unique about the function and grep for that inside `./asm/pspeu/st/no3_psp/nonmatchings`. Is there a call to `PlaySfx` with a unique ID? Is there an unusual constant you can search for?
-   File sizes can help - typically extracted PSP assembly is around 30-50% larger than PSX due to being compiled with no optimisations
-   Find links between functions. For example your function may be a small helper function that is not particularly unique, but you know it is called by one specific larger function which has lots of uniqueness. If you find the larger function on PSP, you can find the corresponding call to your smaller function in that assembly.
-   The order of the functions is usually the same between the PSP and PSX versions. If you are having issues finding something unique about your function, you may be able to find a function before it, and search for the address of the next function based on where that function ends. Repeat until you get to the number of your function. It also works in reverse.

## Decompiling Tips

-   When uploading to decomp.me, remove the line from the top of the PSP assembly `.include "macro.inc"`
-   If your function has any jump tables, include them beneath the assembly in a section marked `.section .rodata` For example:

.set noat      /\* allow manual use of $at \*/
.set noreorder /\* don't insert nops after branches \*/

glabel func\_psp\_0923D2E0
\[...\]
.size func\_psp\_0923D2E0, . \- func\_psp\_0923D2E0

.section .rodata
.align 3
glabel jtbl\_psp\_092A1AB0
\[...\]
.size jtbl\_psp\_092A1AB0, . \- jtbl\_psp\_092A1AB0

-   When decompiling, to start it is generally best to copy your PSX function straight in and not rely on the M2C output for PSP. With that said, the M2C output can be very useful when refactoring code as it is more likely to have linear code and correct order of operations when compared to the optimised PSX M2C output.
    
-   When working on functions involving `Primitive`, you will likely have lots of mismatches with addresses. This is because the Primitive struct is slightly different on PSX and PSP. Add a 4-byte member to the structure after the `next` member, and this will shift the addresses to match. For example:
    

typedef struct Primitive {
    struct Primitive\* next;
    u32 dummy;
    u8 r0;
    ...
}