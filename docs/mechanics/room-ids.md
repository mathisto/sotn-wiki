---
title: "Room IDs"
---

# Room IDs

Here is a diagram showing the ID numbers for each room in each zone of the game. This was originally created by Forat Negre on Discord :)

To find the ID for a room, set an emulator breakpoint on InitRoomEntities (for the appropriate overlay). Then, walk into the room of interest, and see what the `$a0` register is set to. This will be the ID of the room you're entering.

[![caption](/wiki/File:Map_rooms.png "caption")](https://www.sotn.fun/wiki/File:Map_rooms.png)