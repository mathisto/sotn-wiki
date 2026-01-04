---
title: "Sound Effects Documentation"
---

Sound effects are loaded via the CdFile struct:

```
typedef struct {
    s32 loc;        // lba offset, might be a s32
    CdCallbacks cb; // sets g_CdCallback
    s32 size;       // file size
    u8 vabId;       // index for g_VabAddrs, between 0 and 5?
    u8 unkD;        // index for D_800ACD10, between 0 and 6?
    u8 nextCdFileType;
    u8 unkF;
} CdFile;
```

The vabId indicates which VAB to overwrite with the new sound effects. By default the VH and VB files are defined as:

```
CdFile g_LbaStageVh = {0x0000, 19, 0x00000, 3, 3, 0xFF, 14};
CdFile g_LbaStageVb = {0x0000, 17, 0x00000, 3, 3, 0xFF, 0};
```

So they use vabId 3. The locations and sizes get overwritten when loading:

```
        if (g_LoadFile == CdFile_StageSfx) {
            g_LbaStageVh.loc = g_StagesLba[g_LoadOvlIdx].vhOff;
            g_LbaStageVh.size = g_StagesLba[g_LoadOvlIdx].vhLen;
            g_LbaStageVb.size = g_StagesLba[g_LoadOvlIdx].vbLen;
        }
```

And the vabId to load into gets set later:

```
        g_VabId = cdFile->vabId;
```

Which gets used later to load the VH and VB into vabId 3.

```
        res = SsVabOpenHeadSticky(g_Cd.addr, g_VabId, g_VabAddrs[g_VabId]);
...
    D_80137FA8 = SsVabTransBodyPartly(g_Cd.overlayCopySrc, len, g_VabId);
```

This means that every sound effect with vabId 3 refers to different sounds depending on the stage overlay that is loaded. For example:

```
        {
            "id": 265,
            "id_hex": "109",
            "ram_addr": "800BFC93",
            "vabid": 3,
            "prog": 2,
            "note": 65,
            "volume": 120,
            "unk4": 0,
            "tone": 0,
            "unk6": 50
        },
```

See `assets/dra/sfx.json`

## Sound Effect Scripts

SOTN has a system that allows combining notes in a sequence to produce new sound effects. For example let's look at a "cursor" sound effect. If we play sound effect 0x67B, that maps to entry 123 of the g\_SfxData array, which as a vabId of 9. 9 is special and indicates to use a script.

```
void func_8013572C(s16 arg0, u16 volume, s16 distance) {
...
    if (g_SfxData[arg0].vabid == 9) {
```

The script is parsed in `func_80135D8C`:

```
                    vab = temp_t2[0];
                    if (vab == -1) {
                        g_UnkChannelSetting2[i] = 0;
                        continue;
                    }
                    *temp_t3 = temp_t2 + 2;
                    prog = temp_t2[1];
                    *temp_t3 = temp_t2 + 3;
                    note = temp_t2[2];
                    *temp_t3 = temp_t2 + 4;
                    tone = temp_t2[3];
                    *temp_t3 = temp_t2 + 5;
```

The array of sound effects is D\_8013B628 and is accessed by the `prog` value + 1.

```
    progId = g_SfxData[arg0].prog + 1;
    D_8013B628[channel_group] = D_800C1ECC[progId];
```

The cursor sound effect is entry 2 in that array, which is D\_800C0CE8:

```
   // vab| prog| note| tone| vol | delay
u8 D_800C0CE8[] = {
     0x00, 0x05, 0x56, 0x0A, 0x20, 0x01, 
     0x00, 0x05, 0x4A, 0x0A, 0x68, 0x04, 
     0x00, 0x05, 0x4A, 0x0A, 0x0E, 0x03, 0xFF,
};
```

The system will play 3 sounds with a delay after each one:

```
vab 0 prog 05 tone 0A note 56
vab 0 prog 05 tone 0A note 4A
vab 0 prog 05 tone 0A note 4A
```

The 0xFF indicates the end of the sound effect script.