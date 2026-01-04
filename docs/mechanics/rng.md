---
title: "RNG"
---

# RNG

Symphony of the Night uses [Pseudo-Random Number Generators](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) when randomness is needed in the game. There are two PRNGs that are currently known about (dubbed Nice and Evil), and each is responsible for handling the randomness of different events in the game.

In the decompiled code, `Random()` is the function for the Nice RNG, and `rand()` is the function for Evil RNG.

Both RNGs are set to an initial value of 0 on startup (NOTE: On Saturn the initial value for the Evil RNG is actually 1 instead of 0). For the most part, the Evil RNG is advanced once every frame, even if the player isn't doing anything (hence why it has been dubbed Evil). Different functions within the game's code will also make specific calls to the Nice and Evil RNG, and so different events will trigger one or the other. A comprehensive list of what events call which RNG is not known, but a few events have been figured out. The Nice RNG is responsible for determining the location of Dracula's teleports in the Prologue, determining Flea Man jumps, determining the rotations of the Books in the Library, etc. The Evil RNG is responsible for determining whether or not an item drop occurs after an enemy dies and whether or not an item drop will be rare, uncommon, or common. The Evil RNG is also responsible for determining which Food item will drop from a Meal Ticket.

Some events in the game are the result of calls to both, as in the case of Medusa Head spawn behavior.

Both RNGs operate in a similar manner, but use different numbers as their multiplier, increment, and shift, as detailed in the code sections at the bottom of the page.

## Python implementation of the Nice RNG used in SOTN

```python
class NiceRng():
    def __init__(self, initial_seed: int = 0):
        self.seed = initial_seed
    
    def current(self) -> int:
        return self.seed >> 0x18
    
    def next(self) -> int:
        self.seed = 0xFFFFFFFF & ((self.seed * 0x01010101) + 1)
        return self.current()
```

## Python implementation of the Evil RNG used in SOTN

```python
class EvilRng():
    def __init__(self, initial_seed: int = 0):
        self.seed = initial_seed
    
    def current(self) -> int:
        return 0x7FFF & (self.seed >> 0x10)
    
    def next(self) -> int:
        self.seed = 0xFFFFFFFF & ((self.seed * 0x41c64e6d) + 0x3039)
        return self.current()
```