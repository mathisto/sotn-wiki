# SOTN Decomp Build Guide

## Prerequisites

- **OS**: Ubuntu 24.04 LTS (recommended, tested in CI)
- **Go**: Install via snap
- **Git**: For cloning the repository
- **Python**: Version 3.12.x or newer
- **Rust**: Via rustup
- **System packages**: Listed in `tools/requirements-debian.txt`

### Windows Users
Must use WSL2 with Ubuntu 24.04. Install via PowerShell (admin):
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
Enable-WindowsOptionalFeature -Online -FeatureName "Microsoft-Windows-Subsystem-Linux" -NoRestart
wsl --install
wsl --set-default-version 2
wsl --install Ubuntu-24.04
```

### Arch Linux Users
Install AUR packages:
- `cross-mipsel-linux-gnu-binutils`
- `cross-mipsel-linux-gnu-gcc`

---

## Build Steps

### 1. Initial Setup
```bash
# Update apt package index
sudo apt-get update

# Install Go
sudo snap install --classic go

# Install Git
sudo apt-get install -y git

# Clone the repo
git clone https://github.com/Xeeynamo/sotn-decomp.git
cd sotn-decomp

# Update submodules
git submodule update --init --recursive

# Install system packages
sudo apt-get install -y $(cat tools/requirements-debian.txt)
sudo apt-get install -y rustup
rustup default stable

# For Saturn version only:
sudo dpkg -i tools/dosemu-deb/*.deb

# Download compilers and tools
make update-dependencies
rustup update
```

### 2. ISO Setup
1. Dump your unmodified US copy as BIN/CUE
2. Place files in `sotn-decomp/disks/`
3. Name the CUE file `sotn.us.cue`

```bash
# Dump files from ISO
make extract_disk && echo "iso dump OK"

# Extract code and data
make extract -j && echo "extract OK"

# Compile
make build -j && echo "build OK"

# Verify match
make check
```

### 3. Regular Building
```bash
make extract      # Extract game assets and assembly
make all          # Compile binaries to build/
make disk         # Create new CUE/BIN from compiled binaries
```

**Note**: After changes in `config/`, run `make clean` first.

For non-matching functions:
```bash
CPP_FLAGS=-DNON_MATCHING make
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **`go: command not found`** | Install Go via [PPA or Snap](https://go.dev/wiki/Ubuntu#using-ppa) |
| **`splat: command not found`** | Run `export PATH=$PATH:$HOME/.local/bin` then retry. If splat not installed, run `make update-dependencies` |
| **`cannot execute binary file: Exec format error`** (Windows) | You're on WSL1. Run: `wsl --set-version "Ubuntu-24.04" 2` |
| **`SyntaxError: f-string`** | Install Python 3.12.x or newer |
| **Dumping PS1/Saturn disc** | See below |

### Dumping Game Discs
```bash
sudo apt install -y cdrdao toc2cue
cd disks
cdrdao read-cd --read-raw --datafile sotn.us.bin --device /dev/sr0 --driver generic-mmc-raw sotn.us.toc
toc2cue sotn.us.toc sotn.us.cue
```

---

⚠️ **If any command fails, STOP and check troubleshooting or ask on [Discord](https://sotn-discord.xee.dev/).**
