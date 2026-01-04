---
title: "GameShark"
---

# GameShark

Hundreds of Game Shark "codes" exist for SotN. These codes typically change game code found in [DRA](/wiki/Overlay "Overlay"), RIC, or occasionally stage or boss overlays.

A selection of these codes are presented below with the original ROM values compared to the modified values, what the decompiled code or data looks like before and after the change, and what the effect on the game is.

Several of these came from [sotn.dev](https://sotn.dev/debug.html). There are many additional sources for these as well.

## Debug Print Messages

GameShark code

800E3D5C 45BF
800E3D5E 0C00
800E3D60 FFFF
800E3D62 2404

Original

Modified

bne $v1, $v0, .L800E3D94
nop

jal 0x800116fc
addiu $a0, $zero, -1

if (g\_GameState == Game\_Play && g\_DebugEnabled) {
  if (g\_DebugHitboxViewMode != 0) {
    DrawEntitiesHitbox(g\_DebugHitboxViewMode);
  }
}

FntFlush(-1);
if (g\_DebugEnabled) {
  if (g\_DebugHitboxViewMode != 0) {
    DrawEntitiesHitbox(g\_DebugHitboxViewMode);
  }
}

  

## Hitbox Viewer

GameShark code

800BD1C0 0001
801362B0 0001