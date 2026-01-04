---
title: "Saturn Reverse Engineering Workflow"
---

## Setup

```
Copy NITM cue/bin into disks and name it sotn.saturn.cue / sotn.saturn.bin
apt-get install -y $(cat tools/requirements-debian.txt)
pip3 install -r tools/requirements-python.txt 

sudo apt-get install -y -o APT::Immediate-Configure=false \
    dos2unix software-properties-common && \
    sudo add-apt-repository -y ppa:dosemu2/ppa && \
    sudo apt-get update && \
    sudo apt-get install -y dosemu2; 

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

make -j build_saturn_toolchain_native
make extract_saturn
make saturn
```

## Ghidra Usage

# Import the file

File -> Import File Accept the defaults Yes to Analyze Press Analyze on the window that comes up

Our example will be stage\_02\_li.o

Press G to bring up the goto window. Enter `060dca54`

Right now there's no function defined.

Click on the first instruction and press f to make a function

Go to File -> Parse C Source

Set the Architecture to SuperH SH-2

Remove all the "Source files to parse by pressing X"

Add header files like sattypes.h. Press Parse to Program, Continue, Use Open Archives. You should see the new types in the Data Type Manager

Now right click on param\_1 and edit function signature

Change param\_1 to Entity\*

The decompiler output should be improved

## Identifying Overlays

### If you already know the address

If you already know where the overlay is loaded, the process is easier. For example let's do a stage overlay. We know that stages are loaded at `0x060DC000`. This is a an address in High Work Ram. To get the address within High Work Ram, subtract `0x06000000`. So we want to look at `0x000DC000` in Mednafen's debugger.

Press Alt-D to bring up the debugger.

Select High Work Ram by pressing `>` twice.

Press `G` and enter `000DC000`

We need to search for these bytes in the files on the CD: `06 0E E9 C4 06 0E E9 38`. Eight bytes is usually enough to eliminate false positives.

I've written a tool to help with this, in [https://github.com/sozud/saturn-splitter/tree/main/byte-search](https://github.com/sozud/saturn-splitter/tree/main/byte-search)

It can be used as follows:

```
cargo build --release
./target/release/byte-search /disks/saturn/ 06,0E,E9,C4,06,0E,E9,38
Byte sequence found at address 0x00000000 in file: "/disks/saturn/STAGE_02.PRG"
Search complete.
```

We've now identified that STAGE\_02.PRG is the Alchemy Lab.

### If you don't know the address

Let's say we don't know where the Bat overlay is loaded. We acquire the familiar and turn it on so that it's loaded. We need to look at the start of the file to see the bytes. We can get the first 8 bytes like this:

```
xxd -l 8 -p ./T_BAT.PRG
060cfb00060cfc48
```

Enable the debugger and go to High Work Ram as in the previous example. Press S to search. Input the string and press enter.

The debugger finds it at `0xCF000`, which is the correct location.

Note that some overlays may use compression or be stored in other memory areas.

## Finding functions

The splitter tool can help with finding function entrypoints. We can use it like this:

```
./target/release/rust-dis --find-funcs ./T_BAT.PRG 
00000060-00000274
00000294-000002E0
000002E8-000003DA
00000410-000005CE
000005F4-0000069C
000006B4-00000AC8
00000B00-00000BF8
00000C48-0000145C
00001490-0000190C
00001938-00001940
00001944-0000194C
00001950-00001958
0000195C-00001964
00001968-00001A28
00001A4C-00001A54
00001A58-00001A60
00001A64-00002004
00002010-00002018
0000201C-00002024
00002028-00002030
00002034-0000203C
00002040-00002064
00002070-000021A8
000021B8-000021DA
000021DC-00002218
00002224-00002252
0000225C-000022A4
000022AC-000022D4
000022DC-000023E4
0000241C-0000263E
00002640-000026BC
000026D0-00002772
00002784-000027F6
00002808-0000284E
```

So the tool has identified a number of functions in T\_BAT.PRG. These are addresses within the file, so you would need to add 0x060CF000 to get the addresses in High Work Ram for this particular case, since that is where T\_BAT.PRG is loaded. We can use Ghidra to decompile these functions and see if any of them look similar to functions in the PSX codebase. In Ghidra, press G to go to a particular address, then press D to decompile it. Make sure you are on the function entrypoint or the decompilation will be strange.

The addresses at first will be addresses within the file. We can change this by going to Window > Memory Map > House Button and set the base address. In this case we want 0x060CF000.

## Finding functions with the debugger

We can use breakpoints to find functions as well. For example let's say we want to find the Entity function for Bloody Zombie. We need to eliminate as many entities as possible so that there aren't false positives, so we kill the skeleton and break the candles.

Press Alt-D to go to the main debugger screen.

Sort the extracted asm by size, since we know it's probably going to be one of the larger functions in STAGE\_02

```
ls -lS ./asm/saturn/stage_02/
d60ECC50.s
d60D1858.s
f60E7508.s
f60E0F70.s
...
```

Ignore the `d` files since those are data. Go to the function address by pressing G and entering the address, then pressing enter.

Press space to toggle a breakpoint. If the game stops, we hit a breakpoint. Untoggle the breakpoint by pressing space. Then press R to start the game. Press Alt-D to exit the debugger, then kill the enemy. Re-enter the debugger and toggle the breakpoint again. If you don't hit a breakpoint, there's a strong possibility you found the right function. Load it up in Ghidra and inspect it for similarities with the PSX code.

We can also get extra assurance by NOPing out the function. We'll use the following sequence, which is just equivalent to `void func() {}`.

```
glabel null_func
/* 0x2FE6 */ mov.l r14, @-r15
/* 0x6EF3 */ mov r15, r14
/* 0x6EF6 */ mov.l @r15+, r14
/* 0x000B */ rts
/* 0x0009 */ nop
```

Go to High Work Ram, press G to go to 0xEAFAC. Then press insert and enter `2fe66ef36ef6000b0009`.

Now, none the Bloody Zombies spawn, confirming we have the right function.