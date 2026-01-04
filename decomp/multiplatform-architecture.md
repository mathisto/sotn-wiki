# Multiplatform Architectural Considerations

## Building

First extract and build the US version:

```bash
make clean && make extract -j && make build -j && make check
```

Build `Sound`:

```bash
cmake -B build/pc -G Ninja -DWANT_LIBSND_LLE=1 -DCMAKE_BUILD_TYPE=Debug && cmake --build build/pc
```

Run `sotn` and make sure that it starts:

```bash
./build/pc/sotn --disk castlevania.us.bin
```

> `castlevania.us.bin` should be Track 1 of your dumped bin/cue.

---

## Adding a Stage

First tell CMake the stage exists. Add a section like this to `CMakeLists.txt` with all the files relevant to the stage:

```cmake
set(SOURCE_FILES_STAGE_WRP
    src/pc/stages/stage_wrp.c
    src/st/wrp/d_1b8.c
    ...
    src/st/wrp/bss.c
)
```

And add it to the core files:

```cmake
set(SOURCE_FILES_CORE
    ${SOURCE_FILES_STAGE_WRP}  # <- new
)
```

Then rebuild.

---

## Stubbing

Stubbing is a technique used when missing code or data that isn't essential yet, or to make incremental progress.

If a function calls another function that's not decompiled yet (has an `INCLUDE_ASM`), put an empty version in `src/pc/stubs.c`:

```c
void func_801083BC(void) { NOT_IMPLEMENTED; }
```

Same with missing data:

```c
s32 D_800978B4;
```

Best practice is to import actual data, unless it's BSS (all zeros anyway).

---

## Typical Bugs (Platform Differences)

### Incorrect Pointer Types

On PS1, `u8*` and `s32` are equivalent and work fine. On 64-bit platforms these are **not** the same and will crash.

### Uninitialized Pointers

On PS1, dereferencing a null pointer may still work since there's no memory protection. Example bug:
- [`src/boss/mar/AFC4.c:38`](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/boss/mar/AFC4.c#L38)

### Scratchpad Usage

The scratchpad is special on-chip memory on PS1. This doesn't exist on other platforms, so you need to declare storage for the types. Example:
- [`src/dra/4A538.c:1831`](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/dra/4A538.c#L1831)

### Struct Alignment

Pointers are not the same length on 32-bit vs 64-bit platforms. Any struct with pointers will have alignment problems. Example fix:
- [`include/primitive.h:16`](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/include/primitive.h#L16)

---

## Summary

| Issue | PS1 Behavior | PC/64-bit Behavior |
|-------|--------------|-------------------|
| `u8*` vs `s32` | Equivalent | Different sizes, crashes |
| Null pointer deref | May work (no protection) | Segfault |
| Scratchpad memory | Hardware feature | Must be emulated/declared |
| Pointer in struct | 4 bytes | 8 bytes (alignment issues) |
