---
title: "Internals"
---

# Internals

## The overlay system

The game is divided into separate modules called overlays. Overlays (`OVL` in short) are chunk of compiled code that are loaded into a specific address based on different situations in the game. This allows to fit more content in the game.

### Memory mapping (Alucard)

Address

End addr.

File name

Description

`80010000`

`8009FFFF`

`main.exe`

Hardware API, bootloader, shared memory

`800A0000`

`8013BFFF`

`DRA.BIN`

[Game engine](#game-engine)

`8013C000`

`8016FFFF`

`BIN/ARC_F.BIN`

Alucard spritesheet

`80170000`

`80179FFF`

`SERVANT/TT_*.BIN`

Familiar program

`8017A000`

`8017CFFF`

`BIN/WEAPON0.BIN`

Right-hand equip program

`8017D000`

`8017FFFF`

`BIN/WEAPON1.BIN`

Left-hand equip program

`80180000`

`801DFFFF`

`ST/*/*.BIN`

[Stages](#stages) program

`801E0000`

`801E8000`

`F_MAP.BIN`

Castle map graphics

`801F0000`

`801F7800`

Heap

`801F????`

`801FFFF0`

Stack

`80280000`

`80??????`

Used to load debug assets

### Memory mapping (Richter)

Address

End addr.

File name

Description

`80010000`

`8009FFFF`

`main.exe`

Hardware API, bootloader, shared memory

`800A0000`

`8013BFFF`

`DRA.BIN`

[Game engine](#game-engine)

`8013C000`

`8017FFFF`

`BIN/RIC.BIN`

Richter program

`80180000`

`801DFFFF`

`ST/*/*.BIN`

[Stages](#stages) program

`801E0000`

`801E8000`

`F_MAP.BIN`

Castle map graphics

`801F0000`

`801F7800`

Heap

`801F????`

`801FFFF0`

Stack

### main.exe

Loaded by the PlayStation 1 BIOS. On the game disk the name is `SLUS_000.67` and it is described by the boot configuration file `SYSTEM.CNF`. In the absence of a configuration file, this executable can be named as `PSX.EXE`. The name `main.exe` is after its counterpart found in the PSP version.

It contains all the hardware API (eg. gamepad, CD, memory card, GPU renderer) of the PlayStation 1 console from the PSY-Q SDK. It does not contain any game logic. The entry point `main` is just responsible to load `DRA.BIN` and `F_MAP.BIN` from the disk and execute the entry point of DRA.BIN immediately.

This executable is also responsible of statically allocate a shared portion of memory that all the overlays can access to. One typical example is the [`GameApi`](#game-api) structure. Overlays never communicate between one another with the exception of this portion of memory.

### Game engine

Named as `DRA.BIN`. It contains all the business logic such as the game loop, the [game API](#game-api), logic to draw maps, load stages, render the graphics, handles the menu, defines monsters, equipment and much more. There is a state-machine that decides what the game engine is supposed to do (eg. load a new stage, spawn Alucard entity and move him across the stage, pause the game into the menu, play FMV). It is the most critical file of the game.

### Stages

Contains all the unique logic to handle map specific events, cut-scenes, enemy AI, collisions and more. It also contains the rooms and entities layout. Each overlay can be considered as its own mini-game. The title screen `SEL.BIN` is an example of how a stage overlay can act very differently. It exposes a small portion of endpoints into the [game API](#game-api) including the room location list or the sprite definitions.

The following is a list of the many stage overlays found in the binary of the game:

ID

PSX

PSP

Description

00

NO0

STP00

Marble Gallery

01

NO1

STP01

Outer Wall

02

LIB

STP02

Long Library

03

CAT

STP03

Catacombs

04

NO2

STP04

Olrox's Quarters

05

CHI

STP05

Abandoned Mine

06

DAI

STP06

Royal Chapel

07

NP3

STP07

Castle Entrance

08

CEN

STP08

Castle Center

09

NO4

STP09

Underground Caverns

0A

ARE

STP10

Colosseum

0B

TOP

STP11

Castle Keep (Hallway Entrance)

0C

NZ0

STP12

Alchemy Laboratory

0D

NZ1

STP13

Clock Tower

0E

WRP

STP14

Warp Room

0F

NO1

STP15

10

NO0

STP16

11

NO1

STP17

12

DRE

STP18

Nightmare

13

NZ0

STP19

14

NZ1

STP20

15

LIB

STP21

16

BO7

STP22

Cerberos (Boss)

17

MAR

STP23

Maria cutscene (clock room)

18

BO6

STP24

Richter (Boss)

19

BO5

STP25

Hippogryph (Boss)

1A

BO4

STP26

Doppleganger10 (Boss)

1B

BO3

STP27

Scylla (Boss)

1C

BO2

STP28

Minotaurus / Werewolf (Boss)

1D

BO1

STP29

Granfaloon (Boss)

1E

BO0

STP30

Olrox (Boss)

1F

ST0

STP31

Final Stage: Bloodlines

20

RNO0

STP32

Black Marble Gallery

21

RNO1

STP33

Reverse Outer Wall

22

RLIB

STP34

Forbidden Library

23

RCAT

STP35

Floating Catacombs

24

RNO2

STP36

Death Wing's Lair

25

RCHI

STP37

Cave (Reverse Abandoned Mine)

26

RDAI

STP38

Anti-Chapel

27

RNO3

STP39

Reverse Castle Entrance

28

RCEN

STP40

Reverse Castle Center (Shaft Boss Fight)

29

RNO4

STP41

Reverse Caverns

2A

RARE

STP42

Reverse Colosseum

2B

RTOP

STP43

Reverse Castle Keep (Hallway Entrance)

2C

RNZ0

STP44

Necromancy Laboratory

2D

RNZ1

STP45

Reverse Clock Tower

2E

RWRP

STP46

Reverse Warp Room

2F

NO1

STP47

30

NO1

STP48

31

NO1

STP49

32

NO1

STP50

33

NO1

STP51

34

NO1

STP52

35

RNZ1

STP53

36

RBO8

STP54

Galamoth (Boss)

37

RBO7

STP55

Akmodan II (Boss)

38

RBO6

STP56

Dracula (Boss)

39

RBO5

STP57

Doppleganger40 (Boss)

3A

RBO4

STP58

The Creature (Boss)

3B

RBO3

STP59

Medusa (Boss)

3C

RBO2

STP60

Death (Boss)

3D

RBO1

STP61

Beezelbub (Boss)

3E

RBO0

STP62

Fake Trevor / Fake Grant / Fake Sypha (Boss)

3F

NO1

STP63

40

MAD

STP64

Debug Room

41

NO3

STP65

Castle Entrance (Intro / Death Cutscene)

42

DAI

STP66

43

LIB

STP67

44

NO1

STP68

45

SEL

STP69

Title Screen / Main Menu

46

TE1

STP70

Test Room 1

47

TE2

STP71

Test Room 2

48

TE3

STP72

Test Room 3

49

TE4

STP73

Test Room 4

4A

TE5

STP74

Test Room 5

4B

TOP

STP75

4C

TE2

STP76

4D

TE2

STP77

4E

TE2

STP78

4F

TE2

STP79

Please note, at the time of writing, not all stage overlays are extracted and available for decompilation. This was a deliberate decision made in an effort to keep the scope of the project manageable during the beginning phase. As the project progresses, more overlays will likely be extracted and made available for decompilation.

## Game API

Exposes endpoints from different overlays in a shared memory area, so they can communicate each other indirectly.

## File handling

The game has three ways to load the game files.

### LBA system

This is the main way the game loads files. To greatly improve loading times, files are accessed by directly specifying to the CD-ROM system the absolute position of the file to load in the disk. This saves time as the disk head would not need to fetch the file location and size from the main table searching by the name. The location is a 32-bit integer that represents the sector index of where the file is physically located on the disk. The size of a sector is physically 2352 bytes long, but only 2048 of them are used to store the actual game data (aside from the XA tracks and the STR videos).

There are mainly two tables in `DRA.BIN` that stores all the game data. One is at `800A3C40` which stores every [stage](#stages) offsets and size. The other table is at [`800ACC74`](https://docs.google.com/spreadsheets/d/1_8JTISfGOXx7UbrdKXnSUYaHAxbLdejoOVJ4svcEU4I/edit?usp=sharing) and it is used to load specific files in different part of the memory based on their type. The stage `ST/SEL/SEL.BIN` contains a duplicate table of `800A3C40`, probably to have some kind of stage select built in.

As the location of the files is hard-coded, their position has to be known before building the actual game. It is believed the PSY-Q SDK has tools to offer this specific functionality. In alternative the tool [sotn-disk](https://github.com/Xeeynamo/sotn-decomp/tree/master/tools/sotn-disk) can be used to patch those binaries after the image is being built.

### PSY-Q open

The classic way of opening files with the UNIX function `open`. This is only used by `main.exe` to bootstrap DRA.BIN and F\_MAP.BIN. It is known to be slower than using an LBA table as it has to move the head at the beginning of the disk, look for the Primary Volume Descriptor offset and walk through the directories to resolve the chosen sector offset and file length.

### Simulator

Used during the development. The file path prefix is `sim:` (eg. `sim:c:\bin\f_title1.bin`). The PlayStation 1 offers drivers for the file I/O. Most likely the developers registered the driver `sim` to allow the PlayStation to load overlays on the fly from a physical hard drive to quickly iterate between new builds. The `main.exe` initially attempts to load `DRA.BIN` and `DRA.BIO` (formal name of F\_MAP.BIN) from the simulator. If it succeeded it sets the flag at `800978AC` to a value different than `0`, effectively indicating the game needs to use the simulator instead of the LBA for all the following files.

## Graphics rendering

This is a write-up to break down how the game renders graphics on screen. In short the game has a [primitive list](#primitive-list) that gets consolidated into a [drawing scene](#drawing-scene) every frame. When graphics contains [sprites](#sprites) or textures the resources are loaded from the [VRAM](#vram).

### Primitive list

TODO

### Drawing scene

TODO

### Sprite banks

TODO: anim set, anim frame, clut index, tpage.

### VRAM

![image](https://private-user-images.githubusercontent.com/6128729/242634327-bde88973-86d7-4590-9952-08d092b561ce.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjgsIm5iZiI6MTc2NzQ5NTA2OCwicGF0aCI6Ii82MTI4NzI5LzI0MjYzNDMyNy1iZGU4ODk3My04NmQ3LTQ1OTAtOTk1Mi0wOGQwOTJiNTYxY2UucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTA4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTYzNWM1YTYxZWE1MjI3ZGM2NjBkOWU4YTY1OWQ2ZjhmZTI5MDNjZWFlYWQ4NWMwZWNiYTcxNGIwNmE1OWZlZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.vWLY6SpEcKUW4zJOl43VtkwYaSww-bI6XARNoAla18g)

This write-up focuses on how the Video RAM (VRAM) is managed by a stage. The VRAM can be divided into four quadrants, each measuring 512x256 pixels.

When working with graphics that have a 4 bits per pixel (4bpp) format, a Color Look-Up Table (CLUT) is utilized. In the following examples, a grey CLUT will be used as a reference.

To transfer graphics from the main memory to the VRAM, a DMA operation is performed using the PSY-Q SDK function `LoadImage(RECT*, u_long*)`. The first parameter `RECT` specifies the location in the VRAM where the graphics will be placed. The second parameter `u_long*` is a pointer to the main memory location from which the graphics will be loaded. It is important to note that the coordinates and size mentioned in the `RECT` parameter are based on a 16-bit image. For example, to load a 256x256 4bpp texture, the `RECT` values will be set as `w=64` and `h=256`.

#### Rendering targets

The upper-left quadrant of the VRAM serves as a double buffer and acts as the render target for creating the final picture. Utilizing a double buffer is crucial to prevent tearing artifacts in the displayed image. While one buffer is used to transfer its content to the video output, the other buffer can be populated to prepare for the next frame. The game employs two buffer descriptors, namely `GpuBuffer g_GpuBuffers[2]` and the variable `g_CurrentBuffer` to keep track of the currently active buffer for rendering the scene. When the frame is ready to be displayed on the screen, `g_CurrentBuffer = g_CurrentBuffer->next` is called to flip the buffers, ensuring that the rendering occurs on the appropriate buffer. During the rendering of stages, each buffer is represented as two 256x240 targets one next to the other. These buffers are stored in the RGBA5551 format, where each pixel is represented by a 16-bit value.

To achieve effects like the photo burning at the end of the prologue, the game creates a duplicate copy of one of the buffers and uses it as a texture. This technique is commonly used in PlayStation 1 games and subsequent game platforms.

#### Stage graphics

![image](https://private-user-images.githubusercontent.com/6128729/242641291-2f57d40a-49fa-45e4-a78f-c1d7d0f0369e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjgsIm5iZiI6MTc2NzQ5NTA2OCwicGF0aCI6Ii82MTI4NzI5LzI0MjY0MTI5MS0yZjU3ZDQwYS00OWZhLTQ1ZTQtYTc4Zi1jMWQ3ZDBmMDM2OWUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTA4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzBjNjVjMzc0ZjUzNDhiNzBlMzIxYThjOWM3YmYwZDgxZDllNjIyZjMzODBhYjc2NTAyNWI5ZjZmMjU3NzQ3NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.3ZKTb0Fk9S4uHESc1fCL-q3EtsDVqqQ51IwElj3quYk)

The second quadrant in the upper-right corner of the VRAM is dedicated to storing stage graphics. It specifically contains everything related to a given stage, including the tileset and decorative entities (e.g. the moving trees in parallax outside the castle or the clock tower in the prologue). Stage graphics are loaded from `ST/{stage}/F_{stage}.BIN` which is always a 256KB file consisting of 32 images of 128x128 pixels and a 4bpp format. Typically the graphics at the far left is used for the tile map and the one at the far right is for the entities.

The first few 256x256 tpages of the stage graphics are 256x240 of the actual tiles and the bottom 16x256 is utilised as a palette collection in the RGBA5551 format. All the stage graphics exclusively use the CLUT at that location to render the tile map. As a result the last row of the tileset is reserved for the palette, often resulting to either uncomprehensive graphics or left blank.

The tiles within the tileset are referenced by an index, where each tile occupies a space of 16x16 pixels. Tile `0` is always empty and it is never rendered. Tile `1` is located at `(16, 0)` while the tile `15` is is at `(240, 0)`. Following this pattern, tile `16` can be located at `(0, 16)`. It is worth noting that tile maps are crafted in a way where tiles from 240 to 255 are never used, as they contain the CLUT for the stage. Typically, after tile 239, the next tile would be tile 256, positioned at (256, 0).

#### DRA entities

![image](https://private-user-images.githubusercontent.com/6128729/242643094-ac8429b4-70d9-4935-8c1e-1ba7c82c93b8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjgsIm5iZiI6MTc2NzQ5NTA2OCwicGF0aCI6Ii82MTI4NzI5LzI0MjY0MzA5NC1hYzg0MjliNC03MGQ5LTQ5MzUtOGMxZS0xYmE3YzgyYzkzYjgucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTA4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YmZlMjlmNGNlNmU2MmMyYmMwYWY3MTY5ZmExMWUzNGJhNGEwMTExNDczMWNiMzNjZDJmYWZlZTY2MTM1YmFhZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.BAZaOZZneBINinDyZQpjgTdu0lSXgax-6uVeujutoW4)

The fourth quadrant at the bottom-right is dedicated to the game engine `DRA.BIN`. It stores the graphics that are shared across stages and can be reused without the need to load them every time. This is true even if the shared entities code (e.g. the candle or the item prize) is store inside each stage overlay and not in DRA. For Alucard, these graphics are loaded from BIN/F\_GAME.BIN, while for Richter, they are loaded from BIN/F\_GAME2.BIN. This section of VRAM contains a series of 32 images, each with a size of 128x128 pixels and a 4bpp format.

The file from which these graphics are loaded is 264KB in size. The last 8KB of the file is allocated for the CLUT, which is loaded at the very bottom of the first quadrant, just below the two [rendering targets](#rendering-targets).

#### Dynamic entities

![image](https://private-user-images.githubusercontent.com/6128729/242651575-09fecde4-2d33-4058-a8dc-388d7a16dafb.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNjgsIm5iZiI6MTc2NzQ5NTA2OCwicGF0aCI6Ii82MTI4NzI5LzI0MjY1MTU3NS0wOWZlY2RlNC0yZDMzLTQwNTgtYThkYy0zODhkN2ExNmRhZmIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTA4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjI0MTBjMmJlMmRjMWU5NTZlODdkYzBkZTM3ODc5M2M2YzIyNTMzNTdmOWU1MWY2NDlmNjM5MWZjZDI5OTA0MiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.c4o2M19DT357prQ5ZDarV3GjT8BUY2a6cZ0Hbb29N70)

This last section is still work-in-progress. It is currently unknown how the game dynamically loads this graphics and where it comes from. It seems to be dynamically loaded from memory based on the room where the player is into.

## Beta content

## ST0

TODO

## MAD

The debug room overlay `ST/MAD.BIN` was compiled earlier than the first retail release of the game. All the offsets that refers to DRA.BIN points to invalid portions of data or to the wrong API calls, effectively breaking the majority of its original functionalities. That is why the debug room does not contain any object. By compiling the debug room with make mad\_fix you can restore it by redirecting the old pointers to the retail version of the game.

## The factory system

Many entities in the game spawn other entities in a roundabout, indirect manner. For example, let's consider the function DoGravityJump, which is used when the player activates their gravity boots. It accelerates the player rapidly into the air, but it also creates a factory, using this syntax:

`CreateEntFactoryFromEntity(g_CurrentEntity, FACTORY(0, 2), 0);`

This will create a factory. The factory is a short-lived entity which exists solely for the purpose of spawning another entity. We pass it a basis entity (in this case g\_CurrentEntity) which will act as the parent of our new entity. By default, our new entity gets spawned into the same location as the parent.

The FACTORY() macro is important. It controls the behavior of the factory to determine what child is made, and any parameters related to that.

### Factory Blueprints

When a factory is created, it has the purpose of spawning a child. It builds that child (hence being called a factory), and does so based on a set of parameters. We call these parameters the "blueprint", the design for building the child. In this case, the gravity jump is creating a factory to use blueprint 2.

To see what blueprints are doing, we can look to `assets/dra/factory_blueprint.json` (note: Richter has his own set of blueprints, so any functions in RIC should look to `assets/ric` for those blueprints). We can then look at blueprint 2, as the blueprint with ID of 2. That is:

```
{
            "id": 2,
            "id_hex": "2",
            "ram_addr": "800AD1E0",
            "childId": 3,
            "unk1": 1,
            "unk2": {
                "bit7": true,
                "bit6": true,
                "bottom6": 1
            },
            "unk3": 0,
            "unk4": {
                "topHalf": 2,
                "bottomHalf": 0
            },
            "unk5": 0
        },
```

Everything from `childId` down is controlling how the factory behaves. Some factories will spawn multiple child entities, for example. A lot of these fields are not understood, and should be researched. Look to EntityEntFactory's first block of lines to see how the data is loaded into the fields of the factory.

The most important element of the blueprint is the `childId`, which tells us what child is made. In this case, the child is entity #3.

### Child entities

When looking at these child entities, they are numbered and are pulled from a few different tables. Factories in the main game and overlays will pull from `g_DraEntityTbl` (and in Richter's code, `g_RicEntityTbl`). In this case, we will look at the #3 entity (counting from 0 of course) in the DRA entity table, and we find `EntityGravityBootBeam`. Lines right up! This factory will create the blue and white beam from Alucard's feet when gravity jumping.

Weapons are different. You will usually see weapon calls like

`g_api.CreateEntFactoryFromEntity(self, ((g_HandId + 1) << 0xE) + FACTORY(0x100, 88), 0);`

The use of `g_HandId` is crucial for knowing this is a weapon call. You can look to `func_8011A4D0` to understand how entity update functions are assigned to new entities. Once we identify this as a weapon call, we can look to the blueprints. We have blueprint 88, which says it has child 9 (again, in `assets/dra/factory_blueprint.json`). But this is not the 9th entity in `g_DraEntityTbl`! This is the 9th element in the Weapon struct in `include/weapon.h`. We can count these down and see `func_ptr_80170024`. This factory call will create an entity whose update function is `func_ptr_80170024`.

This process of identifying what a factory does can be a little confusing. Anywhere in the code which uses a `CreateEntFactoryFromEntity` call should ideally have a comment saying what entity is being made from the chosen blueprint.

It would also be nice if we had a macro for something like `WPN_FACTORY()` which would bake in the `g_HandId` logic, which is somewhat bulky.