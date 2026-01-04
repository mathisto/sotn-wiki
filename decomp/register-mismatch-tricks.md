# Register Mismatch Decompilation Tricks

This page contains some examples of some unintuitive or tricky compiler tricks that may be SotN specific to get registers to match.

## GTE/LTE (PSP)

The developers of SotN tended to use `foo > bar` in if statements.

That tends to get compiled to look as `foo >= bar+1`

This can cause the "wrong" registers to be used. Take for example the asm:

```asm
slti    at,v1,0x29
bnez    at,3d0
nop
```

Directly, this translates to:

```c
if (foo >= 0x29) {
```

However, that will compile to:

```asm
slti    v1,v1,0x29
bnez    v1,3d0
nop
```

Which uses the register `v1` instead of `at`.

**The "correct" translation is `if (foo > 0x28)`**

---

## Modulo

This is a harder one to find in PSX vs PSP.

Take the following assembly in PSX and PSP:

**PSX:**
```asm
lui     v1,%hi(foo)
lw      v1,%lo(foo)(v1)
nop
bgez    v1,1c4 ~>
move    v0,v1
addiu   v0,v1,0x7f
sra     a0,v0,0x7
sll     v0,a0,0x7
subu    a0,v1,v0
```

**PSP:**
```asm
lui     v0,%hi(foo)
lw      v1,%lo(foo)(v0)
li      v0,0x80
andi    s2,v1,0x7f
bgez    v1,284
nop
beqz    s2,284
nop
addiu   s2,s2,-0x80
```

It sure looks like this is some sort of branching statement and you may try to write something like this:

```c
bar = foo & 0x7F;
if (bar < 0 && bar != 0) {
    bar -= 128;
}
```

However, that compiles to (PSP):

```asm
lui     v0,%hi(foo)
lw      v0,%lo(foo)(v0)
andi    s1,v0,0x7f
bgez    s1,284 ~>
nop
beqz    s1,284 ~>
nop
addiu   s1,s1,-0x80
```

Close, but not quite there. **The "tell" on this situation is that we are loading `0x80` into `v0` on PSP, but not doing anything with it.**

This may be a compiler bug (it may also be a sort of comment to help debug), but we can leverage it to know that this is actually a modulo. **The correct translation is:**

```c
index = foo % 0x80;
```

---

## MOVE(v1,v1) (PSP)

There is a weird instruction that gets executed sometimes where the source and destination for a MOVE is the same. This gets compiled out of the code on PSX, so you won't see it there, but it can cause a lot of register mismatches in PSP.

```asm
jal     Random
nop
move    v1,v0
andi    v1,v1,0x3
move    v1,v1  # This is the odd move command
seh     v0,v1
sh      v0,0xa(s0)
```

You may try to match that with something like this:

```c
foo = Random() & 3;
```

But that will lead to the asm being:

```asm
jal     Random
nop
move    v1,v0
andi    v1,v1,0x3
seh     v1,v1
sh      v1,0xa(s0)
```

and missing that odd move.

**MOVE is not actually a MIPS instruction.** It's a pseudo-instruction that the assembler uses as it's clearer to what is happening than the actual translation:

```asm
move   v1,v0
# Is actually
addu   v1, 0, v0
```

So what we are missing here is an addition. The compiler is smart enough to get rid of a `+0`, but if we take a non-zero value and subtract it off again, we will get back the missing move:

```c
foo = (Random() & 3) + 1 - 1;
```

**And that will match the assembly.** In a lot of cases, this also resolves a lot of a0/v0 mismatches as well.

> Likely, one of those values is some sort of `#DEFINE` and the other is an offset, but we may never actually know.

---

## Static function declaration (PSP)

Sometimes function calls can have register mismatches immediately before them that seem impossible to resolve. For example:

```asm
628:    li      v0,0x415 # expected v1 register
62c:    sh      v0,0x36(s0) # expected v1 register
630:    move    a0,s3
634:    move    a1,s0
638:    jal     func_psp_0925EBA0
```

In cases like this it can be worthwhile checking if the function being called would reside within the same file as the one being decompiled, and if so, **making the function being called `static`**:

```c
static void func_psp_0925EBA0(Primitive* a, Primitive* b) {}
```

This is hard to verify in decomp.me because functions produce additional assembly, but an empty statically declared function like this at the top of the scratch may resolve mismatches at the point where the function is called.

**Example:** [https://decomp.me/scratch/Wfz6v](https://decomp.me/scratch/Wfz6v)

---

## Use of $at register in `SP(x)` / `SPAD(x)` usage (PSP)

Certain calls to the scratchpad expect use of the `$at` register. This can be achieved by treating the scratchpad as an array reference. For example:

```asm
7b0:    sll     v1,s2,0x4
7b4:    lui     at,0x1     # expects $at
7b8:    ori     at,at,0x80 # expects $at
7bc:    addu    v0,v1,at
7c0:    sw      v0,0x34(sp)
```

**Expected code is:**

```c
foo = &((long*)(SP(0x80)))[some_var];
```

`long*` can be replaced with the type of `foo` you are expecting.

**Example:** [https://decomp.me/scratch/ZJDcJ](https://decomp.me/scratch/ZJDcJ)
