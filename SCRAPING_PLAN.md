# SOTN Ultimate Wiki - Master Scraping Plan

Comprehensive plan for scraping and crystallizing SOTN knowledge from multiple sources.

## Overview

| Source | Base URL | Page Count | Priority | Method |
|--------|----------|------------|----------|--------|
| GitHub Wiki | github.com/Xeeynamo/sotn-decomp/wiki | 24 | HIGH | Direct webfetch |
| sotn.fun | sotn.fun/wiki | 22 | HIGH | Direct webfetch |
| Castlevania Fandom | castlevania.fandom.com | ~150+ | MEDIUM | Selective scraping |

## Phase 1: GitHub Wiki (Technical - Decomp Focus)

**Priority: CRITICAL** - Core technical documentation

### Build & Setup
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Build | /wiki/Build | Pending | decomp/build.md |
| FAQ | /wiki/FAQ | Pending | decomp/faq.md |

### Decompilation Guides  
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Decompilation | /wiki/Decompilation | Pending | decomp/decompilation.md |
| Decompilation (PSP) | /wiki/Decompilation-(PSP-edition) | Pending | decomp/decompilation-psp.md |
| Saturn Decompilation | /wiki/Saturn-decompilation | Pending | decomp/saturn.md |
| Saturn RE Workflow | /wiki/Saturn-RE-workflow | Pending | decomp/saturn-workflow.md |
| HD Version Matching | /wiki/HD-Version-Matching | Pending | decomp/hd-matching.md |

### Architecture & Internals
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Multiplatform Architecture | /wiki/Multiplatform-Architecture | Pending | decomp/architecture.md |
| Internals | /wiki/Internals | Pending | decomp/internals.md |
| PSP Overlay Header | /wiki/PSP-overlay-header | Pending | decomp/psp-overlay.md |
| Jump Tables | /wiki/Jump-tables | Pending | decomp/jump-tables.md |
| Deduplication | /wiki/Deduplication | Pending | decomp/deduplication.md |

### Tools & Reference
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Asset Tool | /wiki/Asset-Tool | Pending | decomp/asset-tool.md |
| Debug Module | /wiki/Debug-Module | Pending | decomp/debug-module.md |
| Psy-Q Reimplementations | /wiki/Psy-Q-Reimplementations | Pending | decomp/psyq.md |
| Register Mismatch Tricks | /wiki/Register-Mismatch-Tricks | Pending | decomp/register-tricks.md |

### Game Data
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Game Versions | /wiki/Game-versions | Pending | game/versions.md |
| Glossary | /wiki/Glossary | Pending | decomp/glossary.md |
| Sound Effects | /wiki/Sound-Effects-documentation | Pending | game/sound-effects.md |
| Stage Graphics | /wiki/Stage-graphics | Pending | decomp/stage-graphics.md |
| Importing Data | /wiki/Importing-Data | Pending | decomp/importing-data.md |

### Contribution
| Page | URL | Status | Output |
|------|-----|--------|--------|
| PR Guidelines | /wiki/PR-Guidelines | Pending | decomp/pr-guidelines.md |
| Maria PSP for PSX | /wiki/Maria-PSP-for-PSX | Pending | decomp/maria-psp.md |

---

## Phase 2: sotn.fun Wiki (Game Mechanics)

**Priority: HIGH** - In-depth game mechanics, speedrunning

| Page | URL | Status | Output |
|------|-----|--------|--------|
| Alucard | /wiki/Alucard | Pending | game/characters/alucard.md |
| Alucard Blindfolded | /wiki/Alucard_Blindfolded | Pending | game/characters/alucard-blindfolded.md |
| Richter | /wiki/Richter | Pending | game/characters/richter.md |
| Game Versions | /wiki/Game_Versions | Pending | game/versions-detail.md |
| Damage Output | /wiki/Damage-output | Pending | game/mechanics/damage.md |
| RNG | /wiki/RNG | Pending | game/mechanics/rng.md |
| Entity Identification | /wiki/Entity_Identification | Pending | game/mechanics/entities.md |
| Overlay | /wiki/Overlay | Pending | game/mechanics/overlay.md |
| Room IDs | /wiki/Room_IDs | Pending | game/mechanics/room-ids.md |
| TPAGE Layout | /wiki/TPAGE_layout | Pending | game/mechanics/tpage.md |
| Familiar | /wiki/Familiar | Pending | game/mechanics/familiars.md |
| Stage | /wiki/Stage | Pending | game/locations/stages.md |
| Sound Effects | /wiki/Sound_Effects | Pending | game/sound-effects-detail.md |
| Speedrunning | /wiki/Speedrunning | Pending | speedrunning/overview.md |
| Techniques | /wiki/Techniques | Pending | speedrunning/techniques.md |
| Death Skip | /wiki/Death_Skip | Pending | speedrunning/death-skip.md |
| Glitches | /wiki/Glitches | Pending | speedrunning/glitches.md |
| Jewel Sword | /wiki/Jewel_Sword | Pending | game/items/jewel-sword.md |
| GameShark | /wiki/GameShark | Pending | game/cheats.md |
| Ports/PSP | /wiki/Ports/PSP | Pending | game/ports-psp.md |
| Ports/Xbox 360 | /wiki/Ports/Xbox_360 | Pending | game/ports-xbox.md |

---

## Phase 3: Castlevania Fandom (Lore & Reference)

**Priority: MEDIUM** - Comprehensive lore, characters, locations

### Characters (Priority targets)
| Page | URL | Status | Output |
|------|-----|--------|--------|
| Alucard | /wiki/Alucard | Pending | lore/characters/alucard.md |
| Richter Belmont | /wiki/Richter_Belmont | Pending | lore/characters/richter.md |
| Maria Renard | /wiki/Maria_Renard | Pending | lore/characters/maria.md |
| Dracula | /wiki/Dracula | Pending | lore/characters/dracula.md |
| Death | /wiki/Death | Pending | lore/characters/death.md |
| Shaft | /wiki/Shaft | Pending | lore/characters/shaft.md |
| Succubus | /wiki/Succubus | Pending | lore/characters/succubus.md |
| Librarian | /wiki/Librarian | Pending | lore/characters/librarian.md |

### Locations (34 pages - see extracted list)
Normal Castle locations, Reverse Castle locations, Saturn-exclusive areas.
Output: lore/locations/{area-name}.md

### Enemies
Full bestiary - scrape from Category:Symphony_of_the_Night_Enemies
Output: game/enemies/{enemy-name}.md

### Items & Equipment
- Weapons, Armor, Accessories, Relics, Consumables
Output: game/items/{category}/{item-name}.md

---

## Execution Strategy

### Delegation Pattern

Each scraping task will be delegated to background agents:

```
background_task(
  agent="librarian",
  prompt="Fetch and convert [URL] to clean markdown. 
         Extract: title, main content, tables, lists.
         Remove: navigation, ads, footer.
         Output: Clean markdown suitable for local wiki.
         Return: The complete markdown content."
)
```

### Batch Processing

**Batch 1** (24 tasks): GitHub Wiki - all pages
**Batch 2** (22 tasks): sotn.fun Wiki - all pages  
**Batch 3** (50+ tasks): Fandom characters & key locations
**Batch 4** (100+ tasks): Fandom enemies, items (lower priority)

### Quality Control

After each batch:
1. Review markdown for formatting issues
2. Extract key facts to OpenMemory
3. Cross-reference with existing knowledge
4. Update SQLite artifact with status

---

## Automation Notes

### Scraping Script (Future)

Could create a Python script to automate:
```python
# .dev/scripts/scrape_wiki.py
import requests
from bs4 import BeautifulSoup
import markdownify

def scrape_page(url, output_path):
    # Fetch, clean, convert to markdown, save
    pass
```

### Continuous Updates

- GitHub Wiki: Re-scrape monthly (active development)
- sotn.fun: Re-scrape quarterly
- Fandom: Re-scrape annually (stable content)

---

## Status Tracking

- [ ] Phase 1: GitHub Wiki (0/24 complete)
- [ ] Phase 2: sotn.fun Wiki (0/22 complete)
- [ ] Phase 3a: Fandom Characters (0/~20 complete)
- [ ] Phase 3b: Fandom Locations (0/34 complete)
- [ ] Phase 3c: Fandom Enemies (0/~100 complete)
- [ ] Phase 3d: Fandom Items (0/~200 complete)

---
Last Updated: 2026-01-03
