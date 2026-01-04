# SOTN Game Versions

The game was published multiple times on multiple platforms across the past decades.

## Version Table

| ID | Console | Build Date | Notes |
|----|---------|------------|-------|
| jp10 | PS1 | 1997-02-20 | |
| jp11 | PS1 | 1997-03-06 | Same psx.exe as jp10 |
| usproto | PS1 | 1997-06-17 | Same psx.exe as jp10 |
| **us** | PS1 | 1997-09-01 | **Decompilation target** |
| eu | PS1 | 1997-09-30 | |
| hk | PS1 | 1997-11-30 | Same psx.exe as jp10 |
| jp12 | PS1 | 1998-01-23 | Same psx.exe as jp10 |
| saturn | Saturn | 1998-04-27 | |
| hd | PS1 | 2006-10-22 | Build found in PSP game |
| xbla-109-jp | XB360 | 2007-06-22 | Found in XBLA (J) `\DATA\fonts\fonts.zip` |
| xbla-115-us | XB360 | 2007-03-07 | Found in XBLA (US) `\DATA\fonts\fonts.zip` |
| xbla-dvd-us | XB360 | 2007-03-07 | Konami Classics disk version. Same default.xex as xbla-115-us |
| pspko | PSP | 2007-09-07 | |
| pspus | PSP | 2007-09-10 | |
| pspjp | PSP | 2007-09-14 | |
| pspeu | PSP | 2007-11-21 | |

**Build date calculation**: Eldest timestamp from file list of a given release.

**Emulated versions**: Xbox Live is virtually identical to `us`. Castlevania Requiem, iOS, and Android emulate the `pspus` version.

## Japanese PS1 Revisions

Per [The Cutting Room Floor](https://tcrf.net/Castlevania:_Symphony_of_the_Night_(PlayStation)#Revisional_Differences), Japanese PS1 versions are identified by SLPM_860.23 date:

| ID | SLPM_860.23 Date |
|----|------------------|
| jp10 | 1997/02/19 |
| jp11 | 1997/03/06 |
| jp12 | 1998/01/19 |

---

## Version Details

### us
The most common version. **Currently in decompilation.**

### saturn
Ported by an external Japanese team. Very different folder structure from PS1, but similar memory structures.

Uses [Sega Saturn Development Tool Kit](https://archive.org/details/segasaturn-toolkit) SDK:
```
FS_SBL Version 2.14 1997-04-11
CDC Version 1.22 1997-02-27
BUP Version 1.25 1997-06-20
SYS Version 2.50 1997-06-10
```

### hd
Most intriguing version. Found in every Castlevania Dracula X Chronicles release at `PSP_GAME/USRDIR/res/ps/hdbin`. Appears to be an unreleased PS1 build. **Unused and not bootable.**

### xbla
Significant because it contains source code for **SEL, DRA, RIC, WARP** all in one executable (`default.xex`). Also contains original sound effect names.

**Tools**:
```bash
# Get executable info
xextool -l default.xex > info.txt

# Decrypt the xex
xextool -e d default.xex
```
