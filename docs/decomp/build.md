---
title: "Build"
---

## Introduction

These instructions assume you are running **Ubuntu 24.04 LTS**, which is what we are testing against in our CI.

:warning: If any of the commands fail (i.e. give error messages), **STOP** and check the [Troubleshooting](#Troubleshooting) section. :warning:

If you don't see an answer, join the Discord and ask for help - do not blindly continue running commands!

## Set-up

```bash
# update apt's package index
sudo apt-get update

# install go
sudo snap install --classic go

# install git
sudo apt-get install -y git

# clone the repo
git clone https://github.com/Xeeynamo/sotn-decomp.git

# change directory into the folder containing the cloned repo
cd sotn-decomp

# update submodules used by the repo
git submodule update --init --recursive

# install system packages
# If you encounter an error with installing the packages, check the
# tools/requirements-debian.txt file for the line "./tools/dosemu-deb/*.deb"
# and remove it if it exists, then try this step again.
sudo apt-get install -y $(cat tools/requirements-debian.txt)
sudo apt-get install -y rustup
rustup default stable
# if building the Saturn version, this command is required as well
sudo dpkg -i tools/dosemu-deb/*.deb

# download compilers + other required tools
make update-dependencies
rustup update
```

### ISO Setup

- Dump your unmodified US copy of the game as BIN/CUE
- Place the `.bin` and `.cue` files inside `sotn-decomp/disks/`
  - **NOTE** Name the `.cue` file `sotn.us.cue`. 

Once done, continue with extraction, building and verifying the code matches the original binary:

```bash
# dump files from the iso
make extract_disk && echo "iso dump OK"

# extract code and data from the dumped files
make extract -j && echo "extract OK"

# compile the code
make build -j && echo "build OK"

# confirm that the compiled code matches the original binary
make check
```

## Building

1. Run `make extract` to extract the game assets and the assembly code yet to decompile.
1. Run `make all` to compile the binaries in the `build/` directory.
1. Run `make disk` to create a new CUE/BIN pair based on the new compiled binaries.

In case there are any changes in the `config/` folder, you might need to run `make clean` to reset the extraction.

Some non-matching functions are present in the source preprocessed by the macro `NON_MATCHING`. You can still compile the game binaries by running `CPP_FLAGS=-DNON_MATCHING make`. In theory they might be functionally equivalent in-game, but this is not guaranteed. Few of them could match by tuning or changing the compiler.

## Troubleshooting

### I am on Windows and I do not know how to install WSL

Open an PowerShell admin command prompt and run the following:

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
Enable-WindowsOptionalFeature -Online -FeatureName "Microsoft-Windows-Subsystem-Linux" -NoRestart
wsl --install
wsl --set-default-version 2
wsl --install Ubuntu-24.04
```

### I get `/bin/bash line 1: go: command not found` when I run `make extract_disk`
Install the Go binary - there are multiple ways to do this but [using PPA or Snap](https://go.dev/wiki/Ubuntu#using-ppa) are likely easiest depending on your platform.

### I get `/bin/bash line 1: splat: command not found` when I run `make extract_disk`

Run the following command to see whether `splat` is installed:
```bash
python3 -m pip freeze | grep splat || echo "splat is not installed"
```
If it shows something like `splat64==0.24.6` then `splat` *is* installed but the binary is not on your `$PATH`.

Run 
```bash
export $PATH=$PATH:$HOME/.local/bin
```
.. and then run `make extract_disk` again.

**NOTE:** If it says that splat is not installed, you need to run `make update-dependencies`.

### I am on Windows and I get a `cannot execute binary file: Exec format error`

You are most likely using WSL1. Open a command prompt and run the following:

```
wsl --set-default-version 2
wsl -l -v
wsl --set-version "Ubuntu-24.04" 2
```

### I am on a Arch-based Linux distribution

You need to install the AUR packages [`cross-mipsel-linux-gnu-binutils`](https://aur.archlinux.org/packages/cross-mipsel-linux-gnu-binutils) and [`cross-mipsel-linux-gnu-gcc`](https://aur.archlinux.org/packages/cross-mipsel-linux-gnu-gcc) by cloning their repository and by running `makepkg -si`.

### I need to dump my PS1 or Saturn game disc

To dump the PSX or Saturn versions of the game, install `cdrdao` and `toc2cue`.

The argument to `--device` may be different on your system. The BIN, TOC, and CUE should be named in the format `sotn.$VERSION.$EXT`.
```bash
sudo apt install -y cdrdao toc2cue
pushd disks
cdrdao read-cd --read-raw --datafile sotn.us.bin --device /dev/sr0 --driver generic-mmc-raw sotn.us.toc
toc2cue sotn.us.toc sotn.us.cue
popd
```

This will produce a single file BIN with corresponding CUE and TOC files. The TOC file is not used and can be deleted.

### I get `SyntaxError: f-string` during the build when a Python script executes

Make sure you have installed a version of Python that is at least v3.12.x

Note this may not be installed out of the box with your current distro version and you may need to install it manually.