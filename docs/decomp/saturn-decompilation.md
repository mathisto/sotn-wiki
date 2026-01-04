---
title: "Saturn Decompilation"
---

## Internals

### Overlays

File Name

Stage

STAGE\_00.PRG

Final Stage: Bloodlines

STAGE\_0X.PRG

Entrance (1st visit)

STAGE\_01.PRG

Entrance (2nd visit)

STAGE\_02.PRG

Alchemy Laboratory

STAGE\_03.PRG

Marble Gallery

STAGE\_04.PRG

Outer Wall

STAGE\_14.PRG

Center / Maria Boss

STAGE\_15.PRG

Underground Garden / Skeleton Leader

STAGE\_16.PRG

Cursed Prison

BOSS\_02.PRG

Slogra & Gaibon

LOGO.PRG

Intro copyright logo

TITLE.PRG

Title screen and main menu

### Memory mapping (Alucard)

Address

End addr.

Memory Area

File name

Description

`06004080`

`~060505df`

High Work Ram

`0.BIN`

A mix of SEGA libraries and some DRA.BIN

`06066000`

`~0608008b`

High Work Ram

`GAME.PRG`

Similar to DRA.BIN

`060A5000`

High Work Ram

`ALUCARD.PRG`

Alucard code overlay

`060CF000`

`~060d5fff`

High Work Ram

`T_BAT.PRG` etc.

Familiar code overlay

### Memory mapping (Richter/Maria)

Address

End addr.

Memory Area

File name

Description

`00232000`

Low Work Ram

`RICHTER.CHR`/`MARIA.CHR`

Secondary player sprite graphics

`06004080`

High Work Ram

`0.BIN`

Entry point, Sega libraries

`06060000`

High Work Ram

`GAME.PRG`

Probably the equivalent of DRA.BIN

`060A5000`

High Work Ram

`RICHTER.PRG`/`MARIA.PRG`

Secondary player code overlay

`060DC000`

High Work Ram

`STAGE_XX.PRG`

Stage code overlay

`05C1D980`

VDP1 Ram

`RIC_W.CHR`/`MAR_W.CHR`

Secondary player sprite graphics

`05C2F820`

VDP1 Ram

`STAGE_XX.CHR`

Stage sprite graphics

## Scratches

### 0.BIN

Saturn Func

PSX Func

Scratch

Matched?

Note

f\_0000ae08

ratan2

[https://decomp.me/scratch/889Ky](https://decomp.me/scratch/889Ky)

### GAME.PRG

Saturn Func

PSX Func

Scratch

Matched?

Note

f\_0000921C

func\_800FD4C0

[https://decomp.me/scratch/1CORM](https://decomp.me/scratch/1CORM)

f\_000092C0

func\_800FD5BC

[https://decomp.me/scratch/DFpq8](https://decomp.me/scratch/DFpq8)

Probably matching

f\_00009328

func\_800FD664

[https://decomp.me/scratch/WEMRF](https://decomp.me/scratch/WEMRF)

f\_000152f4

Random

[https://decomp.me/scratch/F5nPH](https://decomp.me/scratch/F5nPH)

f\_000157b4

CheckCollision

[https://decomp.me/scratch/GZerS](https://decomp.me/scratch/GZerS)

f\_0606F798

LearnSpell

y

f\_0606F800

func\_800FDD44

y

f\_0606FC60

IsRelicActive

y

f\_060A80E0

func\_8011203C

y

### ALUCARD.PRG

Saturn Func

PSX Func

Scratch

Matched?

Note

f\_060A7DE8

BatFormFinished

y

f\_060AA23C

ControlBatForm

y

f\_060AC574

y

Part of EntityAlucard

### T\_BAT.PRG

Saturn Func

PSX Func

Scratch

Matched?

Note

data\_00000000

g\_ServantDesc

[https://decomp.me/scratch/Eex58](https://decomp.me/scratch/Eex58)

Y

func\_00000294

func\_801713C8

[https://decomp.me/scratch/FeLXE](https://decomp.me/scratch/FeLXE)

func\_000021b8

func\_80173E78

[https://decomp.me/scratch/kMCmY](https://decomp.me/scratch/kMCmY)

Y

func\_00002224

func\_80173F30

[https://decomp.me/scratch/ccc2s](https://decomp.me/scratch/ccc2s)

Should be equivalent

func\_060D11DC

func\_80173EB0

[https://decomp.me/scratch/z4bWL](https://decomp.me/scratch/z4bWL)

func\_060D125C

func\_80173F74

[https://decomp.me/scratch/nVmi2](https://decomp.me/scratch/nVmi2)

func\_0000225C

func\_80173F74

[https://decomp.me/scratch/ha1kO](https://decomp.me/scratch/ha1kO)

func\_000022AC

func\_80173FE8

[https://decomp.me/scratch/vOfP4](https://decomp.me/scratch/vOfP4)

Y

### STAGE\_02.PRG (Alchemy Lab)

Saturn Func

PSX Func

Scratch

Matched?

Note

func\_060EAFAC

EntityBloodyZombie

[https://decomp.me/scratch/ZvlTe](https://decomp.me/scratch/ZvlTe)

## Compiler patterns

### Function return values

If you have an issue like this with `jsr @r1` vs `jsr @r0`, your function prototype generally needs to return `void` to get `r1`, and non-void to get `r0`.

```
void DestroyEntity(Entity*);

  10:    mov.l   50 ,r1           
  12:    jsr     @r1
```

```
s32 DestroyEntity(Entity*);

r 10:    mov.l   50 ,r0         
r 12:    jsr     @r0

```

### Equivalent code that produces different asm

The following two functions produce different asm. [https://decomp.me/scratch/oNzR9](https://decomp.me/scratch/oNzR9)

```
bool func_06013320(void) {
    if (DAT_060644C0 == 2) {
        return 1;
    }
    return 0;
}

bool func_06013320(void) { return DAT_060644C0 == 2; }
```

### Ghidra output patterns:

Struct pointer dereference:

```
*(undefined *)(param_1 + 0x11) = 10;
```

```
param_1->unk11 = 10;
```

## Graphics Info

Tile graphics are loaded by func\_6008588. NOPing this out shows that the tilemap is present but the graphics aren't:

![image](https://private-user-images.githubusercontent.com/122322823/252204718-b18026f0-df5b-4986-b9cf-00d7e8528c07.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjAsIm5iZiI6MTc2NzQ5NTA2MCwicGF0aCI6Ii8xMjIzMjI4MjMvMjUyMjA0NzE4LWIxODAyNmYwLWRmNWItNDk4Ni1iOWNmLTAwZDdlODUyOGMwNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT06MDIyYzAxNGU0MGEyZGJmZTllYmM4MjljYjAwYzVlMDcwYTVlYWY1NjJiZWY0Y2YzZTkxZTY4YzA4ZWY4M2FhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.WvbjGHFYN0c9aKxScBjIgHtw7EFJI8sLdTuys8FRSOA)

WIP [https://decomp.me/scratch/TXaHJ](https://decomp.me/scratch/TXaHJ)

Part of the Richter sprite graphics are loaded by func\_600A490. I think there's two banks loaded to different RAM areas. NOPing this out removes one of the banks.

![image](https://private-user-images.githubusercontent.com/122322823/252204552-80f3aff0-0fb0-4f18-aa6c-2a16eb8b6e88.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjAsIm5iZiI6MTc2NzQ5NTA2MCwicGF0aCI6Ii8xMjIzMjI4MjMvMjUyMjA0NTUyLTgwZjNhZmYwLTBmYjAtNGYxOC1hYTZjLTJhMTZlYjhiNmU4OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xZDM0ZmY1ZjZiYmU0MjU4MmEzNTY3YzQxNDQ0NDFjYjdjMzdlZjMzMmQ4ZmNjODg5OGJiOTg3OTY0MWM3OTk5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.WjZ0i99F-R7hopN-uFWm26a-go7INWzgWtQ7JpZ_XZQ)

Tile maps and collision data seem to be loaded by func\_606C774. NOPing this out gives the following showing that the tile graphics are loaded but the map is messed up.

![image](https://private-user-images.githubusercontent.com/122322823/252204341-82706a10-dff2-48fe-afa5-b9ef3e3f29a7.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjAsIm5iZiI6MTc2NzQ5NTA2MCwicGF0aCI6Ii8xMjIzMjI4MjMvMjUyMjA0MzQxLTgyNzA2YTEwLWRmZjItNDhmZS1hZmE1LWI5ZWYzZTNmMjlhNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNzVlNTdlOTUzYTc0NzQzZWIwYzc3ZTZiOGFhOTMxOGE3NTMzNTBmYzdmODcyZTZiNTdiNmU3MTgxZWFjZjk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.KzcllpVZlcZ9OjU61FG7Wgic4OTdyBRDOlb06lt4KBw)

These functions all call func\_0600f96C which is responsible for writing to an area of Low WRAM around ~26a750.

This area gets read by instructions at 0x60088BC (func\_0600871C) or 0x60099fe (func\_060098F0) or 0x6009bee (func\_06009AE8). which transfers it to a buffer starting at high WRAM 0x0605C120.

NOPing out func\_060098F0 prevents part of the transfer to high WRAM and you get this:

![image](https://private-user-images.githubusercontent.com/122322823/252206388-f6b80a0d-d859-4e9e-9cb4-d650b5b5dd4c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjAsIm5iZiI6MTc2NzQ5NTA2MCwicGF0aCI6Ii8xMjIzMjI4MjMvMjUyMjA2Mzg4LWY2YjgwYTBkLWQ4NTktNGU5ZS05Y2I0LWQ2NTBiNWI1ZGQ0Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZDYwNmRlOTAyNmJkYzFjNDY4MjYzMzdlYjBlN2ZlOWQ3ZWQ3ZjUyOWUwMjljZmIyZGQ1YmM1MWE5Yjk4NzE4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3MdCpUDA2IZG1xREb7Lf_0ck1Wf0f0xcaED4qDATYUA)

NOPing out func\_06009AE8 gets this:

![image](https://private-user-images.githubusercontent.com/122322823/252206567-dde65428-b083-4adb-a3d0-99922c12a1fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjAsIm5iZiI6MTc2NzQ5NTA2MCwicGF0aCI6Ii8xMjIzMjI4MjMvMjUyMjA2NTY3LWRkZTY1NDI4LWIwODMtNGFkYi1hM2QwLTk5OTIyYzEyYTFmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNmI4Y2VjODc2NGE5ZWUxZDc1YjY0MWJkOTI5NzVkZjBkYjliNTFlYzNjY2ExZjRjMWY0OTI0ZmRlY2FiYjk3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.VsFvmYJ_SnW-49bHZITxNhn8b6hrvvciSGFLsGARYiA)

Then 0x0605C120 is processed and transferred to VDP2 Ram by func\_60098F0. The instruction that does the write is at 0x6009a04.