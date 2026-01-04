---
title: "Maria PSP for PSX - How to Install"
---

# Maria PSP for PSX - How to Install

This mod replaces Richter with Maria from the Symphony of the Night copy found in Castlevania: Dracula X Chronicles. This means you have to type "RICHTER" when starting a new game, and existing saves with Richter will load Maria instead.

## Preface

This tutorial assumes you do not already have the Docker CLI installed. Docker Desktop is recommended as it is available on all operating systems, and supports both x86/x64 and ARM. If you already have Docker installed, you can skip Docker Desktop and simply open a terminal in the folder containing your ISOs, then run:

```bash
docker run -v .:/disks xeeynamo/sotn-mariapsp-forpsx
```

## Requirements

- Disk image of [Castlevania: Symphony of the Night (US, PSX)](http://redump.org/disc/3379/)
- Disk image of [Castlevania: Dracula X Chronicles (EU, PSP)](http://redump.org/disc/4528/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

!!! warning
    You **must** use the European version of Castlevania Dracula X Chronicles or it will NOT work! The American version is not supported.

!!! info
    You can supply a modified disk image of Castlevania: Symphony of the Night for PlayStation 1. But we do not support it nor can we guarantee it will work.

## Disclaimer

!!! warning
    Do not redistribute any files without permission, and make sure to follow the terms of the included license file. Unless otherwise stated, this page is the official source for the most up-to-date version of the mod.

!!! info
    This mod is the result of years of research by the [all the contributors](https://github.com/Xeeynamo/sotn-decomp/graphs/contributors) to the sotn-decomp project. Both the mod and the decompilation are free and open source. Please give proper credit by mentioning the project when discussing or sharing the mod. Any enhancements or direct derivative works must also remain open source.

## Step 1: Prepare the Game Files

1. Rename your PlayStation 1 copy of Castlevania: Symphony of the Night as `sotn.us.bin`
   - Windows tends to hide file extensions by default; in that case renaming it to `sotn.us` will just work
2. Rename your PlayStation Portable copy of Castlevania: Dracula X Chronicles as `sotn.pspeu.iso`
   - If Windows hides the extension name from your file, `sotn.pspeu` will just work

## Step 2: Start Docker Desktop

Once you start Docker Desktop on your Windows or macOS, you should see the main Docker Desktop interface.

## Step 3: Locate the Maria PSP for PSX Mod

On the search bar at the top center, type `xeeynamo/sotn-mariapsp-forpsx` and click the *Run* button. It will take a while to download, so be patient.

## Step 4: Prepare the Mod

Under *Optional Settings*, in the *Volume* section:

1. Click the three blue dots next to *Host path*
2. Select your computer folder where you have your two Castlevania games
3. On *Container Path* write `/disks`
4. Press the *Run* button

Your computer will install the Maria PSP for PSX mod.

## Step 5: Install the Mod

This step will take a few minutes, depending on your computer. You know it finished when the play button becomes blue.

## Step 6: Play the Mod

In the same folder where you have your two Castlevania games, there will be a new folder called `mariapsp-forpsx`. Inside that folder, you will find `sotn-patched.us.bin`. This is the patched game image to use with your emulator or console. Enjoy!
