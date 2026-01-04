# Psy-Q SDK Reimplementations Comparison

A comparison of open-source Psy-Q SDK reimplementations for PlayStation decompilation projects.

## Rendering

| Feature | PsyCross | libValkyrie |
|---------|----------|-------------|
| **Backend** | SDL + OpenGL (hardcoded) | Multiple: D3D9, D3D11, D3D12, OpenGL, OpenGL ES, Vulkan, XED3D |
| **PXGP Support** | Yes | No |

**Sources:**
- PsyCross: [PsyX_render.cpp](https://github.com/OpenDriver2/PsyCross/blob/bffa65e67e8dcad1a70560f88088e5d2e3030cca/src/render/PsyX_render.cpp#L361)
- libValkyrie: [Core/Render](https://github.com/Gh0stBlade/libValkyrie/tree/main/Core/Render)
- PsyCross GTE: [PsyX_GTE.cpp](https://github.com/OpenDriver2/PsyCross/blob/bffa65e67e8dcad1a70560f88088e5d2e3030cca/src/gte/PsyX_GTE.cpp#L282)

## Sound

| Feature | PsyCross | libValkyrie |
|---------|----------|-------------|
| **libsnd** | No | No |
| **XA Support** | No | No |
| **libspu** | High-level reimplementation (SDL/OpenAL, no emulator backing) | Better reimplementation with emulator backing |

**Sources:**
- PsyCross: [PsyX_SPUAL.cpp](https://github.com/OpenDriver2/PsyCross/blob/bffa65e67e8dcad1a70560f88088e5d2e3030cca/src/audio/PsyX_SPUAL.cpp#L599)
- libValkyrie: [EMULATOR_SPU.C](https://github.com/Gh0stBlade/libValkyrie/blob/main/Core/Audio/EMULATOR_SPU.C)

## Portability

| Library | Platforms |
|---------|-----------|
| **PsyCross** | SDL + OpenAL (cross-platform but hardcoded dependencies) |
| **libValkyrie** | Android, Durango, Emscripten, Linux, Win32, Win64, Windows Store |

**Sources:**
- PsyCross: [CMakeLists.txt](https://github.com/OpenDriver2/PsyCross/blob/bffa65e67e8dcad1a70560f88088e5d2e3030cca/CMakeLists.txt#L17)
- libValkyrie: [Platform](https://github.com/Gh0stBlade/libValkyrie/tree/main/Platform)

## Summary

| Aspect | PsyCross | libValkyrie |
|--------|----------|-------------|
| **Rendering Flexibility** | Limited (SDL+OpenGL only) | Extensive (7 backends) |
| **GTE/PXGP** | Full support | Partial (no PXGP) |
| **Sound Quality** | Basic high-level | Better (emulator-backed) |
| **Platform Support** | SDL-dependent | Native multi-platform |
