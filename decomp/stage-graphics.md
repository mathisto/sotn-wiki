# Stage Graphics System

## Overview

Stage graphics in Castlevania: Symphony of the Night are located at `ST/{stage}/F_{stage}.BIN` and are typically **256KB** in size. These files contain:

- **Tileset** - Used to render stage maps
- **Sprite-sheets** - Graphics for stage-specific objects/entities

## Technical Format

### Pixel Data
- **4-bit indexed color** (each pixel stores an index 0-15)
- Allows 16 colors per palette
- Multiple palettes can map to the same graphics data

### Color Lookup Table (CLUT)
- Stored in the same file as graphics
- Uses **RGBA5551** format:
  - 5 bits per RGB channel
  - 1 bit for opacity/alpha

## Modding Workflow

### Extraction

Run the extraction command:
```bash
make -j extract
```

Output location: `assets/st/{stage}/`

Each stage produces:
- **8 PNG images** - Grayscale tileset sheets
- **1 CLUT PNG** - Palette data stored separately

> **Note**: Changing tileset colors only affects preview - actual colors come from CLUT file.

### Build & Pack

Repack modified assets:
```bash
make -j build
```

Creates: `build/us/F_{stage}.BIN`

Create disk image with changes:
```bash
make disk
```

Output: New disk image in `build/`

> **Warning**: Running `make extract` will overwrite `assets/` content!

## Manual Tools

### Decode (Extract)

```bash
python3 tools/gfxstage.py d disks/us/ST/NO3/F_NO3.BIN assets/st/no3 --pal 6
```

Arguments:
- `d` - Decode mode
- `disks/us/ST/{stage}/F_{stage}.BIN` - Input binary
- `assets/st/{stage}` - Output directory
- `--pal N` - Palette index for preview (doesn't change output)

### Encode (Pack)

```bash
python3 tools/gfxstage.py e assets/st/no3 build/us/F_NO3.BIN
```

Arguments:
- `e` - Encode mode
- `assets/st/{stage}` - Input PNG directory
- `build/us/F_{stage}.BIN` - Output binary

## Important Constraints

When modifying stage graphics:
- **Keep original image dimensions**
- **Maintain 16-color limit per palette**
- Use grayscale values 0-15 to represent palette indices
