---
title: "Asset Tool"
---

# Asset Tool

A utility bundled in [sotn-decomp/tools](https://github.com/Xeeynamo/sotn-decomp/tree/master/tools/sotn-assets) that exports raw data into a human-readable format and imports it back into the source code.

## Runbook

# Build from the root of the repository

go build -C tools/sotn-assets -o ../../bin/sotn-assets .

# Or build from inside the directory
cd tools/sotn-assets
go build -o ../../bin/sotn-assets .

# Run the tool directly from source without compiling
go run . --help

# Run unit tests
go test

# Format code
go fmt ./...

# End-to-end execution example
bin/sotn-assets extract config/assets.us.yaml
bin/sotn-assets build config/assets.us.yaml

You can use [JetBrains Goland EAP](https://www.jetbrains.com/go/nextversion/) (highly recommended) or VS Code to add your contribution.

NOTE: If you installed Go using `make update-dependencies`, you might encounter `warning: GOPATH set to GOROOT (/home/<your_username>/go) has no effect`. To fix it, run `rm -rf ~/go` and reinstall Go using the [official instructions](https://go.dev/doc/install).

## 🔍 Asset Extraction

sotn-assets extract <config.yaml\>

This command reads each overlay defined in the YAML config and extracts the corresponding binary data to the `assets/` directory in a human-readable format. Each asset type may output multiple files if necessary. The goal is to enable data mining and modding through an editable format.

Example YAML entry:

\- target: disks/us/DRA.BIN
  assets:
  - \[0x2217C, cmpgfx, text\_item\_up, 128, 128, 4\]
  - \[0x227B0, ...

In this example:

1.  The tool opens `disks/us/DRA.BIN`
2.  Seeks to offset `0x2217C`
3.  Loads data up to `0x227B0`
4.  Interprets the loaded data as `cmpgfx` (compressed graphics)
5.  Exports it to a PNG file named `text_item_up.png`

The remaining parameters (`128`, `128`, `4`) are specific to the cmpgfx type: width, height, and bit depth.

Asset entry format:

\- \[offset, type, name, args...\]

Arguments are always positional. Depending on the asset type they can be optional or not. An argument that starts with `--` (e.g. `--skip-build`) is always optional and position-independent.

`name` is often optional. If not specified, `D_{vram+offset}` will be used as a name instead.

## 🔧 Asset Build

sotn-assets build <config.yaml\>

This command reads previously extracted files from the `assets/` directory and converts them back into data consumable by the C compiler (usually as byte arrays).

Uses the same YAML config as used in extraction. Do not edit the asset configuration between an extraction and a build, as the build step is tied to extraction rules. Ensure the tool version is consistent between extraction and build to avoid incompatibilities.

When building, each asset type may:

-   Emit symbols for C code
-   Export headers to be manually referenced
-   Emit .c files with one or more symbols

Tip: Extract once, build as many times as needed when assets are modified.

Caution: Re-running extraction will overwrite existing extracted assets.

## 🗒️ Asset Types

To implement a new asset type, your Asset Handler must implement the following interface:

-   `Name() string`: Returns the YAML type name.
-   `Extract(...)`: Converts binary data to readable files in assets/.
-   `Build(...)`: Converts readable files back into binary/code form.
-   `Info(...)`: Extracts metadata from overlays. Rarely used.

The binary asset has the easiest and smallest handler to understand, useful to use as a base for a new asset handler.

Almost all asset types allow modding, unless stated otherwise.

### 🪧 binary

`<offset> binary [name] [extension] [--skip-build]`

Extract the binary data 1:1 to `assets/<ovl_path>/<name>.bin`. The `bin` extension can be overridden with `[extension]`.

Build the asset in `src/<ovl_path>/gen/<name>.h` as an array of bytes. When `--skip-build` is specified, this step is skipped. Useful when the asset could be included with `.incbin` without having to rely to include a big header file in a C file.

### 🪧 blueprintsdef

`<offset> blueprintsdef NAME SUBWEAPON_ENUM BLUEPRINT_ENUM`

Parse and extract data into a `assets/<ovl_path>/<name>.yaml` file that describes how each blueprint entry is consumed. Both `SUBWEAPON_ENUM` and `BLUEPRINT_ENUM` are required to document IDs that otherwise would be shown as raw numbers.

Build the YAML in `src/<ovl_path>/gen/<name>.h` as an array of `FactoryBlueprint`. The order of the blueprints from the YAML file is not strict, but all the blueprints from `BLUEPRINT_ENUM` must be present. Adding or removing a blueprint needs to also be reflected on the enum, or viceversa.

### 🪧 cmpgfx (modding not working)

`<offset> cmpgfx NAME WIDTH HEIGHT BITS_PER_PIXEL [palette_offset]`

Extracts the two files `assets/<ovl_path>/<name>.cmp` and `assets/<ovl_path>/<name>.png`. The PNG file will have the specified `WIDTH` and `HEIGHT`, while the number of colors will be `16` for `BITS_PER_PIXEL=4`, or `256` for `BITS_PER_PIXEL=8`. Optionally, a `palette_offset` can be specified to use a known palette from the same overlay the compressed graphics is extracted from. When not specified, a default gray-scale palette is used instead.

Building will transpose `assets/<ovl_path>/<name>.cmp` to `src/<ovl_path>/gen/<name>.h`. The previously extracted PNG file is ignored. This impacts modding. The reason is because we do not yet have a matching compression algorithm that can convert a PNG back to a CMP 1:1.

### 🪧 cutscene

`<offset> cutscene [name]`

Parse and extract to `assets/<ovl_path>/<name>.yaml` a cutscene script. The parsed script is a list of opcodes the game interprets to drive a cutscene.

Builds back `assets/<ovl_path>/<name>.yaml` to `src/<ovl_path>/gen/<name>.h` as an array of bytes. All the opcodes and their parameters are parsed back. If an opcode is invalid, the build will fail returning an error.

### 🪧 gfxbanks

`<offset> gfx_banks [name]`

Parse and extract to `assets/<ovl_path>/<name>.json` multiple bank of graphics entires for the stage overlay to upload from memory to the Video RAM.

A graphics entry describes where the graphics should be uploaded to in the VRAM. Based on the graphics location, the entity using the graphics need to use the corresponding tpage and uv coordinates.

The game can use one bank at a time. The same graphics entry can be used by multiple banks. To save space in the game, `indices` is used to maintain an ordered list of banks. An index of `-1` means NULL, and the game will not load any graphics.

Builds to `src/<ovl_path>/gen/<name>.h` chunks of code using `OVL_EXPORT(gfxBanks)[]` as a public symbol. It internally leverages `GFX_ENTRY`.

### 🪧 headergfx

`<offset> headergfx [name] [palette_offset]`

Extracts the file `assets/<ovl_path>/<name>.png`. The PNG file will get width and height from the first two bytes of the data, and the palette size will always be of 16 colors. Optionally, a `palette_offset` can be specified to use a known palette from the same overlay the compressed graphics is extracted from. When not specified, a default gray-scale palette is used instead.

Building will convert `assets/<ovl_path>/<name>.png` to `src/<ovl_path>/gen/<name>.h` as a byte array, including the two bytes containing width and height. The size of the image cannot exceed 255x255.

### 🪧 layers

`<offset> layers [name]`

Parse and extract to `assets/<ovl_path>/<name>.json` an array of background and foreground layers, used to know how to render a room and where to render the main player in the castle.

A room references to a specific bg/fg pair with `layerId`. A `bg` is optional, and some rooms omit it. On the other hand, `fg` is required and the game will crash without it. A `fg` contains the necessary tiles not only to display the room, but for the player to know how it collides with the room itself.

Builds to `src/<ovl_path>/gen/<name>.h` chunks of code using `OVL_EXPORT(rooms_layers)[]` as a public symbol. It internally leverages `LayerDef`.

### 🪧 layout

`<offset> layout [name]`

Parse and extract to `assets/<ovl_path>/<name>.json` an array of entity lists. A room references to a specific entity list with `entityLayoutId`.

Every list of entities have two dummy entities to delimit the start and the end of a list. A `x: -2, y: -2` described the start of an entity list, and `x: -1, y: -1` is the end. These two entities are ignored by the game engine, but they are necessary for the game functionality. If these two entities are absent or mis-placed, building the asset will throw an explicit error.

Each ID is retrieved by the `enum EntityIDs` found in `src/st/<overlay_name>/<overlay_name>.h`. Whenever an ID is not recognised, an hexadecimal string will be used as a place-holder.

Builds to `src/<ovl_path>/gen/<name>.h` chunks of code using `OVL_EXPORT(rooms_layers)[]` as a public symbol. It internally leverages `LayerDef`.

### 🪧 paldef

`<offset> paldef [name]`

Parse and extract to `assets/<ovl_path>/<name>.json` an array of palette entries.

Builds to `src/<ovl_path>/gen/<name>.h` chunks of code using `OVL_EXPORT(cluts)[]` as a public symbol.

### 🪧 palette

TODO

### 🪧 rawgfx

`<offset> rawgfx NAME WIDTH HEIGHT BITS_PER_PIXEL [palette_offset]`

Extracts the file `assets/<ovl_path>/<name>.png`. The PNG file will have the specified `WIDTH` and `HEIGHT`, while the number of colors will be `16` for `BITS_PER_PIXEL=4`, or `256` for `BITS_PER_PIXEL=8`. Optionally, a `palette_offset` can be specified to use a known palette from the same overlay the compressed graphics is extracted from. When not specified, a default gray-scale palette is used instead.

Building will convert `assets/<ovl_path>/<name>.png` to `src/<ovl_path>/gen/<name>.h` as a byte array.

### 🪧 rooms

TODO

### 🪧 sfxconfig

TODO

### 🪧 skip

A special asset type that performs a dummy operation. It does not produce any file. Its sole purpose is to skip a certain region of data.

Takes no parameters.

### 🪧 spritebanks

TODO

### 🪧 spriteset

TODO

### 🪧 spritesheet

TODO

### 🪧 subweaponsdef

TODO

### 🪧 xamusicconfig

TODO

## ℹ️ Additional Considerations

-   The tool is multi-threaded and automatically scales to your CPU core count.
-   Output is generally silent, with warnings and errors written to stderr.
-   Exit code 0 means success. Any non-zero exit code indicates an error.
-   Asset processing is safely isolated—errors during one asset’s extraction or build will not interrupt others.