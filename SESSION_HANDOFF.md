# SOTN Wiki Scraping - Session Handoff

**Date**: 2026-01-03
**Status**: 47/100+ pages scraped

## Continuation Prompt

```
Continue SOTN wiki scraping project in .dev/wiki/

CONTEXT:
- 47 markdown pages already scraped and saved
- Infrastructure ready: .dev/wiki/ structure, SCRAPING_PLAN.md, OpenMemory entries, SQLite artifact
- Using 5 free delegation models in parallel: /grok, /big-pickle, /gpt, /gemini, /zai
- Strategy: 5 scrapers at a time, one per model to avoid rate limits

COMPLETED:
- All GitHub Wiki decomp pages (18 files in decomp/)
- Core game mechanics (RNG, glitches, familiars, stages)
- Speedrunning overview + techniques
- 20 castle locations (both Normal and Reverse Castle)

REMAINING HIGH-PRIORITY:
1. Reverse Castle locations: Reverse Outer Wall, Reverse Clock Tower, Reverse Entrance, Cave, Reverse Colosseum
2. Saturn-exclusive: Underground Garden, Cursed Prison, Hell Garden, Soul Prison
3. Characters: Richter, Maria, Death, Shaft, Dracula (Fandom)
4. Bosses: Individual boss pages with strategies

REMAINING MEDIUM-PRIORITY:
1. sotn.fun pages as they get populated (many are stubs)
2. Enemy bestiary pages
3. Item/equipment pages

HOW TO CONTINUE:
1. Check .dev/wiki/SCRAPING_PLAN.md for full inventory
2. Fire 5 parallel scrapers using Task tool with /grok, /big-pickle, /gpt, /gemini, /zai
3. Save results to appropriate .dev/wiki/ paths
4. Some Fandom pages hit Cloudflare - try alternative URLs or skip

NOTES:
- Fandom occasionally blocks webfetch (Cloudflare) - ~20% failure rate
- sotn.fun wiki is sparse - many pages are stubs
- GitHub Wiki pages are comprehensive and reliable
```

## Files Structure

```
.dev/wiki/
├── decomp/           # 18 technical decomp docs
├── game/
│   ├── characters/   # 1 file (alucard.md)
│   ├── locations/    # 20 castle area files
│   └── mechanics/    # 6 files (rng, glitches, etc.)
├── speedrunning/     # 2 files
├── README.md
├── SCRAPING_PLAN.md  # Full page inventory with checkboxes
└── SESSION_HANDOFF.md # This file
```

## Reference Resources

| Resource | URL | Status |
|----------|-----|--------|
| GitHub Wiki | https://github.com/Xeeynamo/sotn-decomp/wiki/ | ✅ Mostly scraped |
| Progress Tracker | https://sotn.xee.dev/ | Bookmarked (JS-only) |
| sotn.fun Wiki | https://www.sotn.fun/wiki/ | Partially scraped |
| Castlevania Fandom | https://castlevania.fandom.com/ | Partially scraped |

## Delegation Commands

```bash
/grok <task>        # Free Grok model
/big-pickle <task>  # Free Big Pickle model  
/gpt <task>         # GPT-4o-mini
/gemini <task>      # Gemini 2.5 Flash
/zai <task>         # GLM 4.5 Flash
```

All 5 can run in parallel without rate limiting each other.
