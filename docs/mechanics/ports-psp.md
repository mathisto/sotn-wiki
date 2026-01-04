---
title: "Ports/PSP"
---

# Ports/PSP

The PSP version of SotN is found as an unlockable in Dracula X Chronicles. The version of the game appears to be based on the original JP release as it's missing some bug fixes originally found in the PSX US version of the game.

Of note is that there appears to be a comprehensive implementation of the PSX SDK to bridge the original SotN code with the PSP SDK. Many functions for configuring hardware are empty stubs. Others that would have sent data to memory mapped hardware store values in RAM. This implementation can be found in `PSP_GAME/USRDIR/res/ps/PS.ELF`.

`PS.ELF` also includes address of the Load function for each overlay at offset 0x639BC:

  

type

name

unk

overlay address

1

"dra"

0

0x00000000

2

"sel"

0

0x09237868

2

"st0"

0

0x09246B10

2

"are"

0

0x092379E8

2

"cat"

0

0x0925E600

2

"cen"

0

0x09260988

2

"chi"

0

0x0924BCA8

2

"dai"

0

0x09251430

2

"dre"

0

0x09244A50

2

"lib"

0

0x09254120

2

"no0"

0

0x0925D048

2

"no1"

0

0x09255C38

2

"no2"

0

0x09256C90

2

"no3"

0

0x09238360

2

"no4"

0

0x09237FB0

2

"np3"

0

0x09237A90

2

"nz0"

0

0x09237AB0

2

"nz1"

0

0x09253460

2

"top"

0

0x09248480

2

"wrp"

0

0x092447C0

2

"rare"

0

0x09237840

2

"rcat"

0

0x0924C6D8

2

"rcen"

0

0x09244F30

2

"rchi"

0

0x0924A488

2

"rdai"

0

0x0924F318

2

"rlib"

0

0x09249828

2

"rno0"

0

0x0925D410

2

"rno1"

0

0x092497F8

2

"rno2"

0

0x09253588

2

"rno3"

0

0x09255FB0

2

"rno4"

0

0x09251F90

2

"rnz0"

0

0x09256B38

2

"rnz1"

0

0x09252CD8

2

"rtop"

0

0x09247898

2

"rwrp"

0

0x09244D08

2

"mar"

0

0x092465C8

2

"bo0"

0

0x09251368

2

"bo1"

0

0x09245870

2

"bo2"

0

0x09245D30

2

"bo3"

0

0x09246198

2

"bo4"

0

0x092478E8

2

"bo5"

0

0x092473A0

2

"bo6"

0

0x09244758

2

"bo7"

0

0x09245D08

2

"rbo0"

0

0x09237858

2

"rbo1"

0

0x09248780

2

"rbo2"

0

0x09245DF0

2

"rbo3"

0

0x09245800

2

"rbo4"

0

0x09245F70

2

"rbo5"

0

0x0925F690

2

"rbo6"

0

0x09244A00

2

"rbo7"

0

0x09245D40

2

"rbo8"

0

0x09245C58

3

"ric"

0

0x092C8D48

3

"arc\_f"

0

0x092A6280

3

"maria"

0

0x092C0280

4

"tt\_000"

0

0x092EC220

4

"tt\_001"

0

0x092EA620

4

"tt\_002"

0

0x092EF290

4

"tt\_003"

0

0x092EF908

4

"tt\_004"

0

0x092EF780

4

"tt\_005"

0

0x092EF290

4

"tt\_006"

0

0x092EF908

5

"w0\_000"

0

0x092F3498

5

"w0\_001"

0

0x092F48A0

5

"w0\_002"

0

0x092F3490

5

"w0\_003"

0

0x092F3498

5

"w0\_004"

0

0x092F34A8

5

"w0\_005"

0

0x092F3500

5

"w0\_006"

0

0x092F40F8

5

"w0\_007"

0

0x092F4020

5

"w0\_008"

0

0x092F4B80

5

"w0\_009"

0

0x092F4D98

5

"w0\_010"

0

0x092F59D0

5

"w0\_011"

0

0x092F5740

5

"w0\_012"

0

0x092F4650

5

"w0\_013"

0

0x092F4AB0

5

"w0\_014"

0

0x092F4418

5

"w0\_015"

0

0x092F4D88

5

"w0\_016"

0

0x092F4E68

5

"w0\_017"

0

0x092F3C30

5

"w0\_018"

0

0x092F3900

5

"w0\_019"

0

0x092F3818

5

"w0\_020"

0

0x092F4E18

5

"w0\_021"

0

0x092F4D08

5

"w0\_022"

0

0x092F3740

5

"w0\_023"

0

0x092F5798

5

"w0\_024"

0

0x092F59F8

5

"w0\_025"

0

0x092F5880

5

"w0\_026"

0

0x092F5A70

5

"w0\_027"

0

0x092F5140

5

"w0\_028"

0

0x092F5A10

5

"w0\_029"

0

0x092F5300

5

"w0\_030"

0

0x092F6378

5

"w0\_031"

0

0x092F3508

5

"w0\_032"

0

0x092F35B8

5

"w0\_033"

0

0x092F34E8

5

"w0\_034"

0

0x092F3C28

5

"w0\_035"

0

0x092F3498

5

"w0\_036"

0

0x092F3498

5

"w0\_037"

0

0x092F4670

5

"w0\_038"

0

0x092F39F0

5

"w0\_039"

0

0x092F3CC0

5

"w0\_040"

0

0x092F3ED0

5

"w0\_041"

0

0x092F3E18

5

"w0\_042"

0

0x092F4010

5

"w0\_043"

0

0x092F3F10

5

"w0\_044"

0

0x092F3EE8

5

"w0\_045"

0

0x092F4058

5

"w0\_046"

0

0x092F4738

5

"w0\_047"

0

0x092F4500

5

"w0\_048"

0

0x092F47C8

5

"w0\_049"

0

0x092F4E58

5

"w0\_050"

0

0x092F5358

5

"w0\_051"

0

0x092F47C0

5

"w0\_052"

0

0x092F58C0

5

"w0\_053"

0

0x092F4BC8

5

"w0\_054"

0

0x092F39E8

5

"w0\_055"

0

0x092F3AE0

5

"w0\_056"

0

0x092F4368

5

"w0\_057"

0

0x092F3498

5

"w0\_058"

0

0x092F43C0

6

"w1\_000"

0

0x092F7298

6

"w1\_001"

0

0x092F86A0

6

"w1\_002"

0

0x092F7290

6

"w1\_003"

0

0x092F7298

6

"w1\_004"

0

0x092F72A8

6

"w1\_005"

0

0x092F7300

6

"w1\_006"

0

0x092F7EF8

6

"w1\_007"

0

0x092F7E20

6

"w1\_008"

0

0x092F8980

6

"w1\_009"

0

0x092F8B98

6

"w1\_010"

0

0x092F97D0

6

"w1\_011"

0

0x092F9540

6

"w1\_012"

0

0x092F8450

6

"w1\_013"

0

0x092F88B0

6

"w1\_014"

0

0x092F8218

6

"w1\_015"

0

0x092F8B88

6

"w1\_016"

0

0x092F8C68

6

"w1\_017"

0

0x092F7A30

6

"w1\_018"

0

0x092F7700

6

"w1\_019"

0

0x092F7618

6

"w1\_020"

0

0x092F8C10

6

"w1\_021"

0

0x092F8B08

6

"w1\_022"

0

0x092F7540

6

"w1\_023"

0

0x092F9598

6

"w1\_024"

0

0x092F97F8

6

"w1\_025"

0

0x092F9680

6

"w1\_026"

0

0x092F9870

6

"w1\_027"

0

0x092F8F40

6

"w1\_028"

0

0x092F9810

6

"w1\_029"

0

0x092F9100

6

"w1\_030"

0

0x092FA178

6

"w1\_031"

0

0x092F7308

6

"w1\_032"

0

0x092F73B8

6

"w1\_033"

0

0x092F72E8

6

"w1\_034"

0

0x092F7A28

6

"w1\_035"

0

0x092F7298

6

"w1\_036"

0

0x092F7298

6

"w1\_037"

0

0x092F8470

6

"w1\_038"

0

0x092F77F0

6

"w1\_039"

0

0x092F7AC0

6

"w1\_040"

0

0x092F7CD0

6

"w1\_041"

0

0x092F7C18

6

"w1\_042"

0

0x092F7E10

6

"w1\_043"

0

0x092F7D10

6

"w1\_044"

0

0x092F7CE8

6

"w1\_045"

0

0x092F7E58

6

"w1\_046"

0

0x092F8538

6

"w1\_047"

0

0x092F8300

6

"w1\_048"

0

0x092F85C8

6

"w1\_049"

0

0x092F8C58

6

"w1\_050"

0

0x092F9158

6

"w1\_051"

0

0x092F85C0

6

"w1\_052"

0

0x092F96C0

6

"w1\_053"

0

0x092F89C8

6

"w1\_054"

0

0x092F77E8

6

"w1\_055"

0

0x092F78E0

6

"w1\_056"

0

0x092F8168

6

"w1\_057"

0

0x092F7298

6

"w1\_058"

0

0x092F81C0