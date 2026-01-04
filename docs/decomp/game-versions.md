---
title: "Game Versions"
---

The game was published multiple times into multiple platforms across the past decades. The following table lists the main versions and revisions released so far:

| ID           | Console | Build date | Notes
|--------------|---------|------------|-------
| jp10         | PS1     | 1997-02-20 |
| jp11         | PS1     | 1997-03-06 | same psx.exe as jp10
| usproto      | PS1     | 1997-06-17 | same psx.exe as jp10
| us           | PS1     | 1997-09-01 |
| eu           | PS1     | 1997-09-30 |
| hk           | PS1     | 1997-11-30 | same psx.exe as jp10
| jp12         | PS1     | 1998-01-23 | same psx.exe as jp10
| saturn       | Saturn  | 1998-04-27 |
| hd           | PS1     | 2006-10-22 | build found in the PSP game
| xbla-109-jp  | XB360   | 2007-06-22 | build found in the XBLA (J) game in \DATA\fonts\fonts.zip
| xbla-115-us  | XB360   | 2007-03-07 | build found in the XBLA (US) game in \DATA\fonts\fonts.zip
| xbla-dvd-us  | XB360   | 2007-03-07 | Konami Classics disk version. Same default.xex as in xbla-115-us
| pspko        | PSP     | 2007-09-07 |
| pspus        | PSP     | 2007-09-10 |
| pspjp        | PSP     | 2007-09-14 |
| pspeu        | PSP     | 2007-11-21 |

The build date is calculated by taking the eldest timestamp from the list of files of a given release. The Xbox Live version is virtually identical to the `us` variant, while the ports in Castlevania Requiem, the iOS and Android are emulating the `pspus` version.

According to [The Cutting Room Floor](https://tcrf.net/Castlevania:_Symphony_of_the_Night_(PlayStation)#Revisional_Differences) the three PS1 Japanese version releases can be identified by the modified date of the SLPM_860.23 file of the disk. On the other end this wiki uses the file in the disk with the latest modified date to calculate the Build Dae.

| ID           | SLPM_860.23 Date |
|--------------|------------------|
| jp10         | 1997/02/19       |
| jp11         | 1997/03/06       |
| jp12         | 1998/01/19       |

## us

The most common version of the game. This is the version which is currently in decompilation.

## saturn

Ported by an external Japanese team. The folder structure is very different from the PS1 version. From a first look in a game memory dump, the structures are very similar to the PS1 counterpart.

It is confirmed to use the [Sega Saturn Development Tool Kit](https://archive.org/details/segasaturn-toolkit) as SDK by looking at the following string dump:

```
00017214 FS_SBL Version 2.14 1997-04-11
00029c44 CDC Version 1.22 1997-02-27
0002c364 BUP Version 1.25 1997-06-20
0002ca5C SYS Version 2.50 1997-06-10
```

## hd

This is so far the most intriguing version of the game. Found in every release of the Castlevania Dracula X Chronicles in the `PSP_GAME/USRDIR/res/ps/hdbin` folder, the game looks like a strange PS1 build that was never seen before. It is unused and so far it is not bootable.

## xbla

The xbla versions are significant because they contain source code for SEL, DRA, RIC, WARP all in one big executable: default.xex.

This big executable also contains a list of original sound effect names.

You can get some info on the executable with xextool:

```
xextool -l default.xex > info.txt
```

You can decrypt the xex with:

```
xextool -e d default.xex
```