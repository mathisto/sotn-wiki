---
title: "Debug Module"
---

# Debug Module

# What is this?

Adds a custom debug menu. It is written in C and it is meant to replace the Bat familar `SERVANT/TT_000.BIN`. Once loaded you can long-press SELECT+START to soft-reset the game and keep using the debug menu everywhere, including when playing with Richter or during the credits.

One key requirement to run this is to have an emulator that emulates the 8MB of RAM. This is a key requirement to have the debug module surviving soft-resets or accessing to the in-game menu. I personally used [PCSX Redux](https://github.com/grumpycoders/pcsx-redux) to build this module. I am not sure about the compatibility with other emulators. This does **NOT** work on real hardware and it is a choice by design. The debug module is intended to test different areas of the game and help decompiling. It is not intended to be used in normal gameplay.

# Build

Simply invoke `make disk_debug` to create a disk image of the game in `build/` with the debug module replacing the Bat familiar. This is the bare minimum required to test it in-game.

# Usage

![image](https://private-user-images.githubusercontent.com/6128729/259826946-15a040b6-6191-41c4-b2b8-a4a906ed59eb.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNzEsIm5iZiI6MTc2NzQ5NTA3MSwicGF0aCI6Ii82MTI4NzI5LzI1OTgyNjk0Ni0xNWEwNDBiNi02MTkxLTQxYzQtYjJiOC1hNGE5MDZlZDU5ZWIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTExWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTVlODc4ZmMzYWYzOTAzNGFlNWM4NDQ4Yjg5MzMwY2FhY2ZmZThhNTVkZDU0MjA4ZmZjZDc5MzdhMjFmOTBmZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.g_A9_d5AfQnUWzA_l5cbdb01SGzOn18me0_lZWJJMUo)

On PCSX Redux go to Configuration, Emulation be sure the `8MB` option is checked and Dynarec CPU is unchecked.

## Loading the module

![image](https://private-user-images.githubusercontent.com/6128729/259446455-65b7ccb3-800e-4b66-84f5-5703fc91babe.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNzEsIm5iZiI6MTc2NzQ5NTA3MSwicGF0aCI6Ii82MTI4NzI5LzI1OTQ0NjQ1NS02NWI3Y2NiMy04MDBlLTRiNjYtODRmNS01NzAzZmM5MWJhYmUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTExWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjkyMmEwNzcxYWQxYTVmZGYyOWY2ZTY3OWMzZjJiZDlmNzRjNjZkY2RmYmUxMDFlYTUzZjgxZDE3NGQzNmI1YiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.m48RwAOyGWwVsE6czhJLxBoB7zQSKJtWZ-0xBrxj28Y)

You need to enable the Bat Card from the menu. This will load the debug module from the disk. If you want to re-load the module you need to select another Familar Card, un-pause, pause again and select the Bat Card once more.

You can get the bat card by setting the byte at `0x80097976` to `1` ([ref](https://gamefaqs.gamespot.com/ps/196885-castlevania-symphony-of-the-night/faqs/52789)).

## The main screen

![image](https://private-user-images.githubusercontent.com/6128729/259447050-b528425a-ea6c-4c10-9c19-522612d0ad2a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0OTUzNzEsIm5iZiI6MTc2NzQ5NTA3MSwicGF0aCI6Ii82MTI4NzI5LzI1OTQ0NzA1MC1iNTI4NDI1YS1lYTZjLTRjMTAtOWMxOS01MjI2MTJkMGFkMmEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDRUMDI1MTExWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OWU4MmFkMzNkMGRhYTIyM2ExZWI0YWRhMjUzYjY0NWNiZDcxYTdmYjgwNjZjYmIxZDdlNjcyNjRiZDE1MTMyNCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.3dhQFXE_5jMBjSkOz6MWG-uKfoscCUFhKBu-fB35mwo)

You will know you have loaded the debug module when you see the blue rectangle on the top right. You can press R2 to cycle between the menus. Some menus will temporarily freeze the game, some not. To quickly return in-game you can either press TRIANGLE or START. To bring back the paused debug menu just press R2 once again.

## Debug Mode

### Stage

Teleports the player to a different stage. It is not stable and it can crash often.

### Player

Switches between Alucard and Richter. Currently switching from Richter to Alucard consistently crashes the game.

### No Clip

Allows to freely move the player within the room and without the collisions on. Once the flag is enabled from the debug menu, pressing L2 while in-game will temporarily freeze the player movement and make it immune to collision checking. You can then press the directional buttons to slowly move the player or you can hold CROSS to move it faster. You can also use SQUARE or CIRCLE to cycle between the player frames. Press L2 again to deactivate the NoClip mode.

### Frame by frame

Freezes the game outside the debug module. Press L1 to advance by 1 frame. Hold L2 to put the game in slow-motion.

### Show hitboxes

As shown in the image

### Show debug messages

When the debug menu is un-paused, prints on the top left all the debug messages from the game itself.

### Show collision layer

This prints the internal collision value for every 16x16 tile on the screen. Look the CheckCollision function for more information on how each printed value is used.

### Show draw calls

Shows the maximum GPU resource usage since the game started. Currently only the `max` option works. The `current` option will not show anything.

### Show HBlank

Prints the current horizontal blank interrupt count.

## Entity Spawn

Allows to immediately spawn new entities in the current map

### Mode

There are three list of entities, each one with their own ID: DRA, Stage and RIC. The option RIC is hidden if Richter is not the current playing character. As the list of entities per stage is maintained manually, stage entities might not be available for all stages. The `Alloc` shows how many entities are reserved or actually used. Pressing the SQUARE button here will destroy all the entities within that range.

### ID

Press Left or Right to cycle between the different IDs available. Some of them might crash the game immediately once spawned. Press CROSS to immediately spawn the entity.

### Params

Each entity might have its own parameters. Sometimes the flag 0x8000 is used, which can be toggled with the SQUARE button. Press CROSS to immediately spawn the entity.

### Entity preview

Shows the entity before spawning it. This is turned off by default as it can immediately crash by cycling through the available entity IDs.

### Place entity

Pressing CROSS will allow to move the entity across the screen before placing it. Press CROSS again to place the entity and return to the previous screen. Press SQUARE to quickly place multiple entities of the same type.

## Sound player

There are three macro categories the sound player is split into. For what is currently known only the sounds within the Kind 3 changes based on the loaded stage.

### Stop all sounds

This will also disable the SPU IRQ, effectively unlocking the frame rate.

### Load Stage

Loads a different sound font than the current loaded stage. This can help to quickly preview and test SFXs from other stages without necessarily moving the player there.

### Load Servant

Loads the sound font of a specific servant without necessarily equipping the Familiar Card.

## Castle flags

Preview all the flags used to modify the behaviour of different parts of the two castles.

### Edit mode

You can move the cursor with the directional buttons and flip the flag with CROSS. Press L1 or R1 to cycle between the pages. The cursor warps when reaching the border of the flag grid, allowing a faster navigation.

### View mode

Allows to move between the flags more flexibly.

### Listen mode

Listens for the modified flags while playing. Every time a flag is modified the offset and its value is registered on the top left up to 4 rows. When all the rows are occupied, new values will just remove the oldest one. The last modified flag will always be displayed at the bottom.