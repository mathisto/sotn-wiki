# Alucard

Alucard is the player character for Symphony of the Night.

## Afterimage Effect

Alucard, Richter, and select entities have an "afterimage" effect that draws duplicate graphics behind them during movement - one of the game's most iconic visual elements.

### How It Works

- **6 duplicate images** split into 3 entity groups (2 images each)
- Each frame, a new duplicate captures the current animation frame and position
- Oldest image cleared when max (6) is reached
- RAM index animates blue color and opacity fade via 3 timing/transparency tables
- Effect stops at index 10, or instantly on attack/hard landing

### Flicker Effect

Only 3 of 6 afterimages visible per frame:
- Frame N: images 1, 3, 5 visible
- Frame N+1: images 2, 4, 6 visible

This creates a 60fps flicker that makes the trailing effect visually compelling.

---

**Note:** The sotn.fun wiki Alucard page focuses on technical mechanics. For comprehensive stats/abilities, see Castlevania Fandom or GameFAQs.
