# SOTN RNG Mechanics

Symphony of the Night uses [Pseudo-Random Number Generators](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) when randomness is needed. There are **two PRNGs** (dubbed **Nice** and **Evil**), each responsible for different events.

In decompiled code:
- `Random()` → Nice RNG
- `rand()` → Evil RNG

## Initialization

Both RNGs initialize to **0** on startup.

**Exception**: On Saturn, the Evil RNG initializes to **1**.

## Nice RNG

Deterministic, only advances when called by specific game events.

**Controls:**
- Dracula's teleport locations (Prologue)
- Flea Man jump patterns
- Book rotations in the Library

### Implementation

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

## Evil RNG

Advances **once every frame**, even when idle—hence "Evil."

**Controls:**
- Item drop occurrence on enemy death
- Drop rarity (common/uncommon/rare)
- Meal Ticket food item selection

### Implementation

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

## Mixed Events

Some events call **both** RNGs, such as Medusa Head spawn behavior.

## RNG Constants Summary

| RNG | Multiplier | Increment | Output Shift |
|-----|------------|-----------|--------------|
| Nice | `0x01010101` | `1` | `>> 0x18` (24 bits) |
| Evil | `0x41c64e6d` | `0x3039` | `>> 0x10` & `0x7FFF` |

---

*Source: [sotn.fun/wiki/RNG](https://www.sotn.fun/wiki/RNG) (CC BY-SA 4.0)*
