---
title: "Multiplatform Architectural Considerations"
---

# Multiplatform Architectural Considerations

# Building

First extract and build the US version:

```
make clean && make extract -j && make build -j && make check
```

Build `Sound`

```
cmake -B build/pc -G Ninja -DWANT_LIBSND_LLE=1 -DCMAKE_BUILD_TYPE=Debug && cmake --build build/pc
```

Run `sotn` and make sure that it starts.

```
./build/pc/sotn --disk castlevania.us.bin
```

castlevania.us.bin should be Track 1 of your dumped bin/cue.

# Adding a stage

First you need to tell Cmake it exists. Add a section like this to `CMakeLists.txt` with all the files relevant to the stage

```
set(SOURCE_FILES_STAGE_WRP
    src/pc/stages/stage_wrp.c
    src/st/wrp/d_1b8.c
...
    src/st/wrp/bss.c
)
```

And add it to the core files

```
set(SOURCE_FILES_CORE
    ${SOURCE_FILES_STAGE_WRP} <- new
)
```

Try rebuilding.

## Stubbing

Stubbing is a technique we use when we are missing code or data that we don't think is essential just yet, or to make incremental progress.

If a function calls another function, but it's not decompiled yet (there's an INCLUDE\_ASM), we can simply put an empty version of it in `src/pc/stubs.c`

For example:

```
void func_801083BC(void) { NOT_IMPLEMENTED; }
```

We can do the same with missing data:

```
s32 D_800978B4;
```

It's best to import the actual data, unless it's bss, where you don't need to since it's all 0s anyway.

## Typical Bugs

### Incorrect Pointer Types

On PS1 `u8*` and `s32` are equivalent and it works fine. On 64-bit platforms these are not the same and will result in a crash.

### Uninitialized Pointers

On PS1, you can deference a null pointer and it may still work since there's no memory protection. Here's an example of this sort of bug [https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/boss/mar/AFC4.c#L38](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/boss/mar/AFC4.c#L38)

### Scratchpad Usage

The scratchpad is a special on-chip memory area on PS1. This doesn't exist on other platforms so you need to declare storage for the types. Here's an example [https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/dra/4A538.c#L1831](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/src/dra/4A538.c#L1831)

### Struct alignment

Pointers are not the same length on 32-bit and 64-bit platforms. Any struct with pointers in it is going to have alignment problems. Here's an example of this sort of fix: [https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/include/primitive.h#L16](https://github.com/Xeeynamo/sotn-decomp/blob/d9f9d9c79c393c17207e9660de7698065da0416c/include/primitive.h#L16)