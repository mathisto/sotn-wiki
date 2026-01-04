---
title: "HD Version Matching"
---

Once you have a `us` function matched, there may be additional effort required to match it on the `hd` version.

Get the asm for both versions extracted like this:

```
make force_extract
VERSION=hd make extract
```

Now, we can run a tool to try and cross-reference the symbols:

```
./tools/symbols.py cross asm/us/dra/nonmatchings/5298C/func_800F9F40.s asm/hd/dra/nonmatchings/5298C/func_800F9E18.s 
```

You may get a message like

```
assemblies too different to be cross-referenced automatically
```

In that case, the files need to be matched manually. We can look at the asm to do this. We have matched scratches for both versions:

US version: [https://decomp.me/scratch/GdX90](https://decomp.me/scratch/GdX90)

HD version: [https://decomp.me/scratch/SoE2S](https://decomp.me/scratch/SoE2S)

In the HD version, we can see that the symbol names are different. For example `D_800DC778` corresponds to `D_800DC70C`. We need to add those symbols to `config/undefined_syms.hd.txt`

```
D_800DC70C = 0x800DC778;
D_800DC6EC = 0x800DC758;
func_800F99B8 = 0x800F98AC;
```

Then we can remove the #ifdef to enable the C version in the HD build.

```
- #if defined(VERSION_HD)
- INCLUDE_ASM("dra/nonmatchings/5298C", func_800F9F40);
- #else
```

We can check the build.

```
 VERSION=hd make build -j && VERSION=hd make check
```

Using vbindiff to find differences

```
vbindiff disks/pspeu/PSP_GAME/USRDIR/res/ps/hdbin/dra.bin ./build/hd/DRA.BIN
```