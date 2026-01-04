---
title: "Stage graphics"
---

## Intro

Stage graphics are found in `ST/{stage}/F_{stage}.BIN` and they are generally 256KB long. They contain the tileset used to render the maps and the sprite-sheet for the objects unique to that specific stage. The graphics is stored in 4-bit, which means each pixel can store up to 16 different color combinations. To accommodate more colors, the game can map multiple palettes to the same graphics while keeping the limit of 16 colors per palette. The CLUT (or palette list) is found in the same file, where each color follows the format RGBA5551 (5 bits per channel, 1 bit for opacity).

## Modding

When extracting the game's code and assets via `make -j extract`, the graphics will be found in `assets/st/`. There will be 8 PNG images per stage in a grey-scale palette, while the CLUT is extracted as a separate PNG image. Changing the colors in the tileset is good for a preview and it will not affect the real colors as they are stored in a separate file. It is important to keep the color count and the image size as it is.

Invoking the command `make -j build` will re-pack the graphics from the PNG files into `build/us/F_{stage}.BIN`, while `make disk` will create a new disk image in `build/` with the modified assets.

NOTE: whenever you run `make extract` the content in `assets/` will be replaced!

## Manual decode

Another way to decode the stage graphics is to manually invoke the tool. The advantage of this is that you can specify a palette to better preview how the tileset will look like. Picking different palettes will not change the output.

`python3 tools/gfxstage.py d disks/us/ST/NO3/F_NO3.BIN assets/st/no3 --pal 6`

## Manual encode

In a similar fashion, to encode the graphics and CLUT back into the `F_{stage}.BIN` file, you can run the following command:

`python3 tools/gfxstage.py e assets/st/no3 build/us/F_NO3.BIN`