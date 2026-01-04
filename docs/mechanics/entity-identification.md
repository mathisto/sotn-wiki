---
title: "Entity Identification"
---

# Entity Identification

When doing decomp, it can be tricky to identify what entity is associated to a particular function. This page will list methods for doing this.

## Known entity, unknown function, if Enemy

If you know an entity of interest, and want to find its function, here is a method that works if the entity is an enemy.

1) Open up a RAM viewer in an emulator. Look at address 80073490. This is PLAYER.unkB8.

2) Touch (and get hurt by) the enemy of interest. A pointer to that enemy gets stored into 80073490.

3) Look at the data stored at that pointer. That is the entity that hurt you; look at its PfnEntityUpdate function to see what its function is.