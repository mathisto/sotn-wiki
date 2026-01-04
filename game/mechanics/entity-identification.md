# Entity Identification

When doing decomp, it can be tricky to identify what entity is associated to a particular function. This page lists methods for doing this.

## Known Entity, Unknown Function (Enemy Method)

If you know an entity of interest and want to find its function, this method works if the entity is an **enemy**:

### Steps

1. **Open a RAM viewer** in an emulator
2. **Look at address `0x80073490`** — this is `PLAYER.unkB8`
3. **Touch (and get hurt by)** the enemy of interest
   - A pointer to that enemy gets stored into `0x80073490`
4. **Examine the data** stored at that pointer
   - This is the entity that hurt you
   - Look at its `PfnEntityUpdate` function to see what its function is

### Key Memory Address

| Address | Field | Purpose |
|---------|-------|---------|
| `0x80073490` | `PLAYER.unkB8` | Stores pointer to last enemy that hurt player |

---

*Source: [sotn.fun wiki](https://www.sotn.fun/wiki/Entity_Identification)*
