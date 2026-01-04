# SOTN Wiki

> The comprehensive companion wiki for [Castlevania: Symphony of the Night](https://en.wikipedia.org/wiki/Castlevania:_Symphony_of_the_Night) and the [sotn-decomp](https://github.com/Xeeynamo/sotn-decomp) project.

**[View the Wiki](https://mathisto.github.io/sotn-wiki)**

---

## What's Inside

This wiki consolidates game knowledge, technical documentation, and speedrunning resources for Symphony of the Night across all platforms (PS1, Saturn, PSP, and modern ports).

### Castlevania Guide

| Section | Description | Pages |
|---------|-------------|-------|
| [Stages](https://mathisto.github.io/sotn-wiki/stages/) | All 50 castle locations — Normal and Reverse | 50 |
| [Enemies](https://mathisto.github.io/sotn-wiki/enemies/) | Complete bestiary with stats, drops, and behavior | 100+ |
| [Bosses](https://mathisto.github.io/sotn-wiki/bosses/) | Boss strategies, patterns, and lore | 17 |
| [Items](https://mathisto.github.io/sotn-wiki/items/) | Weapons, armor, accessories, relics, consumables | 60+ |
| [Characters](https://mathisto.github.io/sotn-wiki/characters/) | Playable characters and NPCs | — |
| [Mechanics](https://mathisto.github.io/sotn-wiki/mechanics/) | Game systems, RNG, damage formulas | — |

### Technical Reference

| Section | Description |
|---------|-------------|
| [Decompilation](https://mathisto.github.io/sotn-wiki/decomp/) | Guides for PS1, PSP, and Saturn decompilation |
| [Architecture](https://mathisto.github.io/sotn-wiki/decomp/multiplatform-architecture/) | How the game's overlay system works |
| [Build Guide](https://mathisto.github.io/sotn-wiki/decomp/build/) | Setting up the decomp build environment |
| [Asset Tools](https://mathisto.github.io/sotn-wiki/decomp/asset-tool/) | Working with game assets |

### Speedrunning

| Section | Description |
|---------|-------------|
| [Overview](https://mathisto.github.io/sotn-wiki/speedrunning/overview/) | Category rules and current records |
| [Techniques](https://mathisto.github.io/sotn-wiki/speedrunning/techniques/) | Movement tech, glitches, and skips |

---

## About This Project

This wiki exists to support the **[sotn-decomp](https://github.com/Xeeynamo/sotn-decomp)** project — a matching decompilation effort to reverse-engineer Symphony of the Night's source code for PS1, PSP, and Saturn.

Content is aggregated and synthesized from:

- **[sotn-decomp Wiki](https://github.com/Xeeynamo/sotn-decomp/wiki)** — Technical documentation
- **[sotn.fun](https://www.sotn.fun/wiki/)** — Game mechanics and speedrunning
- **[Castlevania Fandom](https://castlevania.fandom.com/)** — Lore and comprehensive game data
- **sotn-decomp source code** — Direct analysis of decompiled functions

---

## Contributing

Contributions are welcome! This wiki is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

### Local Development

```bash
# Clone the repo
git clone https://github.com/mathisto/sotn-wiki.git
cd sotn-wiki

# Install dependencies
pip install mkdocs-material

# Start local server
mkdocs serve
```

### Adding Content

- **Enemies**: Add markdown files to `docs/enemies/`
- **Stages**: Add to `docs/stages/normal/` or `docs/stages/reverse/`
- **Items**: Add to `docs/items/`

Templates are available in `docs/_templates/` for consistent formatting.

---

## Status

| Content | Progress |
|---------|----------|
| Stage pages | 50/50 |
| Enemy stubs | 100+/~150 |
| Boss pages | 17/17 |
| Item stubs | 60+/~200 |
| Decomp docs | Syncing from upstream |

See [PROGRESS.md](https://mathisto.github.io/sotn-wiki/PROGRESS/) for detailed tracking.

---

## License

Content is provided for educational and preservation purposes. Symphony of the Night is © Konami.

---

<p align="center">
  <i>"What is a man? A miserable little pile of secrets!"</i>
</p>
