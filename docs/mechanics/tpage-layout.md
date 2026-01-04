---
title: "TPAGE Layout"
---

# TPAGE layout

The game stores data in GPU VRAM organized in texture pages, or tpages. They are laid out in the VRAM as follows:

[![](/wiki_wiki/images/1/1e/Annotated_tpages.png)](/wiki/File:Annotated_tpages.png)

This may be helpful for debugging and tracking of textures.

Note that the game's two framebuffers are held in tpages 0 through 7.

Since the game is 256x240 (widthxheight), the height of 240 leaves 16 extra rows of pixels available. These are used for the color lookup tables (also known as CLUTs, or palettes). These are visible in the screenshot along the lower edge of tpages 0 through 7. They actually also bleed into tpages 8 through B as well.