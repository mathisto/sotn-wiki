---
title: "Importing Data"
---

## Basic Tutorial

We will add some data from NZ0 as an example. Let's take a look at the data folder:

```
asm/us/st/nz0/data/
```

All the data here needs to be imported eventually. Let's see how many symbols there are:

```
cat asm/us/st/nz0/data/0.data.s | grep glabel
glabel D_80180000
glabel g_SpriteBanks
glabel D_8018008C
glabel g_Cluts
```

Let's look at `D_80180000`:

```
glabel D_80180000
/* 0 80180000 04951B80 */ .word Update
/* 4 80180004 08991B80 */ .word HitDetection
/* 8 80180008 98BA1B80 */ .word UpdateRoomPosition
/* C 8018000C 20B91B80 */ .word InitRoomEntities
/* 10 80180010 2C271880 */ .word g_Rooms
/* 14 80180014 2C001880 */ .word g_SpriteBanks
/* 18 80180018 60011880 */ .word g_Cluts
/* 1C 8018001C EC081880 */ .word g_pStObjLayoutHorizontal
/* 20 80180020 94031880 */ .word g_TileLayers
/* 24 80180024 88081880 */ .word g_EntityGfxs
/* 28 80180028 00981B80 */ .word UpdateStageEntities
.size D_80180000, . - D_80180000

glabel g_SpriteBanks
/* 2C 8018002C 00000000 */ .word 0x00000000
/* 30 80180030 8C6E1A80 */ .word D_801A6E8C
/* 34 80180034 CC6F1A80 */ .word D_801A6FCC
/* 38 80180038 04731A80 */ .word D_801A7304
/* 3C 8018003C E4791A80 */ .word D_801A79E4
/* 40 80180040 48941A80 */ .word D_801A9448
```

WRP is the most complete overlay, so let's compare:

```
Overlay g_StageOverlay = {
    /* 0x00 */ Update,
    /* 0x04 */ HitDetection,
    /* 0x08 */ UpdateRoomPosition,
    /* 0x0C */ InitRoomEntities,
    /* 0x10 */ g_Rooms,
    /* 0x14 */ g_SpriteBanks,
    /* 0x18 */ g_Cluts,
    /* 0x1C */ NULL,
    /* 0x20 */ g_TileLayers,
    /* 0x24 */ OVL_EXPORT(g_EntityGfxs),
    /* 0x28 */ UpdateStageEntities,
    /* 0x2C */ 0x00000000,
    /* 0x30 */ 0x00000000,
    /* 0x34 */ 0x00000000,
    /* 0x38 */ 0x00000000,
    /* 0x3C */ 0x00000000,
};
```

We can infer that `D_80180000` is g\_StageOverlay for NZ0 because we see the same sequence of function pointers and data pointers. e.g. the first entry is Update, then HitDetection and so forth. Let's import it. Right now in the `config/splat.us.stnz0.yaml` we have:

```
    subsegments:
      - [0x0, data]
      - [0x164, layers, rooms]
```

Let's add a split so we can do one piece at a time. We see that the next data starts at 0x2C:

```
/* 28 80180028 00981B80 */ .word UpdateStageEntities
.size D_80180000, . - D_80180000

glabel g_SpriteBanks
/* 2C 8018002C 00000000 */ .word 0x00000000
```

However, we know that Overlay is size 0x40 from inspecting the struct. It's typical for runs of data to be segmented where they shouldn't be. Let's segment that out by adding another split:

```
      - [0x0, data]
      - [0x40, data]
      - [0x164, layers, rooms]
```

Now do a full rebuild. You need to clean to make it extract again correctly:

```
make clean && make extract -j && make build -j && make check
```

NZ0 still matches, so we can continue:

```
build/us/NZ0.BIN: OK
```

Let's create a new file, d\_0.c.

```
#include "nz0.h"

void Update(void);
void HitDetection(void);
void UpdateRoomPosition(void);
void InitRoomEntities(s32 objLayoutId);
extern RoomHeader g_Rooms[];
extern s16** g_SpriteBanks[];
extern void* g_Cluts[];
extern RoomDef g_TileLayers[];
extern void* g_EntityGfxs[];
void UpdateStageEntities(void);

extern u8** D_801A6E8C;
extern s32* D_801A6FCC;
extern s32* D_801A7304;

Overlay g_StageOverlay = {
    /* 0x00 */ Update,
    /* 0x04 */ HitDetection,
    /* 0x08 */ UpdateRoomPosition,
    /* 0x0C */ InitRoomEntities,
    /* 0x10 */ g_Rooms,
    /* 0x14 */ 0x8018002C,
    /* 0x18 */ g_Cluts,
    /* 0x1C */ g_pStObjLayoutHorizontal,
    /* 0x20 */ g_TileLayers,
    /* 0x24 */ g_EntityGfxs,
    /* 0x28 */ UpdateStageEntities,
    /* 0x2C */ NULL,
    /* 0x30 */ &D_801A6E8C,
    /* 0x34 */ &D_801A6FCC,
    /* 0x38 */ &D_801A7304,
    /* 0x3C */ 0x801A79E4,
};
```

We cheated on two of the symbols, 0x8018002C, and 0x801A79E4 due to issues I was having getting a match. Importing data is an iterative process where it gets more polished over time.

And indicate to splat to use the C file instead of the asm:

```
    subsegments:
      - [0x0, .data, d_0]
      - [0x40, data]
```

Do a full rebuild:

```
make clean && make extract -j && make build -j && make check
```

And we get a match

```
build/us/NZ0.BIN: OK
```

See the full PR here: [https://github.com/Xeeynamo/sotn-decomp/pull/1324/files](https://github.com/Xeeynamo/sotn-decomp/pull/1324/files)

## Diagnosing Errors

Let's see what happens if the data is too long:

```
Overlay g_StageOverlay = {
    /* 0x00 */ Update,
    /* 0x04 */ HitDetection,
    /* 0x08 */ UpdateRoomPosition,
    /* 0x0C */ InitRoomEntities,
    /* 0x10 */ g_Rooms,
    /* 0x14 */ 0x8018002C,
    /* 0x18 */ g_Cluts,
    /* 0x1C */ g_pStObjLayoutHorizontal,
    /* 0x20 */ g_TileLayers,
    /* 0x24 */ g_EntityGfxs,
    /* 0x28 */ UpdateStageEntities,
    /* 0x2C */ NULL,
    /* 0x30 */ &D_801A6E8C,
    /* 0x34 */ &D_801A6FCC,
    /* 0x38 */ &D_801A7304,
    /* 0x3C */ 0x801A79E4,
};

u32 too_long = 0;
```

After building, we see:

```
build/us/NZ0.BIN: FAILED
```

I use a script to help with these issues. This one is currently hardcoded for NZ0. [https://gist.github.com/sozud/3d3ea081de6906b6f99b9b336e4de507](https://gist.github.com/sozud/3d3ea081de6906b6f99b9b336e4de507)

Let's see the output:

```
python3 ./first_diff.py 
build/us/NZ0.BIN build/us/stnz0.map expected/NZ0.BIN expected/build/us/stnz0.map
Modified ROM has different size...
It should be 0x4B780 but it is 0x4B784
First difference at ROM addr 0x18, 0x80180018 is at 0x18 bytes inside 'g_StageOverlay' (VRAM: 0x80180000, VROM: 0x000000, SIZE: 0x40, build/us/src/st/nz0/d_0.c.o)
Bytes: 64:01:18:80 vs 60:01:18:80
Instruction difference at ROM addr 0x18, 0x80180018 is at 0x18 bytes inside 'g_StageOverlay' (VRAM: 0x80180000, VROM: 0x000000, SIZE: 0x40, build/us/src/st/nz0/d_0.c.o)
Bytes: 64:01:18:80 vs 60:01:18:80
Instruction difference at ROM addr 0x40, Symbol 'too_long' (VRAM: 0x80180040, VROM: 0x000040, SIZE: 0x4, build/us/src/st/nz0/d_0.c.o)
Bytes: 00:00:00:00 vs 48:94:1A:80
Instruction difference at ROM addr 0x44, Symbol 'D_80180040' (VRAM: 0x80180044, VROM: 0x000044, SIZE: 0x4C, build/us/asm/us/st/nz0/data/40.data.s.o)
Bytes: 4C:94:1A:80 vs 40:A3:1A:80
Instruction difference at ROM addr 0x90, Symbol 'D_8018008C' (VRAM: 0x80180090, VROM: 0x000090, SIZE: 0xD4, build/us/asm/us/st/nz0/data/40.data.s.o)
Bytes: 05:00:00:00 vs 00:20:00:00
Instruction difference at ROM addr 0x164, Symbol 'g_Cluts' (VRAM: 0x80180164, VROM: 0x000164, SIZE: 0x4, build/us/asm/us/st/nz0/data/40.data.s.o)
Bytes: 90:00:18:80 vs 00:00:00:00

Over 1000 differing words, must be a shifted ROM.
Map appears to have shifted just before D_8018008C (build/us/asm/us/st/nz0/data/40.data.s.o) -- in D_80180040?
```

From `Modified ROM has different size... It should be 0x4B780 but it is 0x4B784`, we know the ROM is too long by 4 bytes.

From `Map appears to have shifted just before D_8018008C (build/us/asm/us/st/nz0/data/40.data.s.o) -- in D_80180040?`, it gives the location.

We can verify this with vbindiff.

```
vbindiff ./build/us/NZ0.BIN ./expected/build/us/NZ0.BIN
```

![image](https://private-user-images.githubusercontent.com/122322823/339964844-ba984c48-61cb-40ba-ad2c-42ce4ce6de1d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzODIsIm5iZiI6MTc2NzQ5NTA4MiwicGF0aCI6Ii8xMjIzMjI4MjMvMzM5OTY0ODQ0LWJhOTg0YzQ4LTYxY2ItNDBiYS1hZDJjLTQyY2U0Y2U2ZGUxZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwNFQwMjUxMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMjZiMWFmMzgxNGFkYzM1ZDk4MGY2OTc1YjM4YTQyMTQzYzkzOGUwMzdmZjg3NTQ1Mjg5NjgzMDUwZDE5ZDgzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.iTQH5zXqoOHBG9_o8rD5im1uhdX2maGus6VBoQQV4d4)

vbindiff has a hard to read color scheme, but I highlighted the area of 0s that is incorrect.