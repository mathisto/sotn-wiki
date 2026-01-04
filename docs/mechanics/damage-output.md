---
title: "Damage Output"
---

# Damage Output

Castlevania: Symphony of the Night has a fairly straightforward formula for calculating attack power for Alucard. From GameFAQs:

"The ATT stats listed on the pause menu detail how much damage Alucard will do with a simple swing of whatever weapon Alucard has equipped. It is calculated as follows. All weapons (including the Dark and Medusa shields, but \_not\_ including the Sword Familiar, Badelaire, and Muramasa) have a maximum attack stat. \[...\] Given this, your ATT rating will be:

ATT = STR + \[Max ATT - (STR / 2)\] (if STR < Max ATT)

ATT = STR + Max ATT (if STR >= Max ATT)"

So, if Alucard has a strength of 36 and is equipped with a Terminus Est (Max Attack of 32), his attack should be 68.

Now, to apply attack to damage to the enemy, there is an additional formula that is also straightforward. From GameFAQs:

"Damage done = (AM \* ATT) - Target's DEF

AM is the attack multiplier. This is usually 1, except in the following cases:

Attacker is poisoned: AM = 0.5

Target is strong vs. attack: AM = 0.5

Target is strong vs. attack, attacker poisoned: AM = 0.25

Target is weak vs. attack: AM = 2

Target is weak vs. attack, attacker poisoned: AM = 1"

Going back to the previous example, if Alucard with 35 strength hits Akmodan II (0 def, strong against poison) with non-critical damage using a Terminus Est (which has poison properties), the amount of damage dealt to Akmodan II will be 34.

Critical damage, on the other hand, is not straightforward. The game uses the so-called Evil RNG (a random number that changes every frame) to determine which formula it will use to generate critical damage. More specifically, all 4 base stats (INT, STR, LCK, CON) get a random number added to them from 0 to 63. Whichever stat wins determines the critical damage formula:

If RNG lands on INT for critical damage, CRITICAL = ATT + (SquareRoot of room count)

If RNG lands on STR for critical damage, CRITICAL = ATT\*2

If RNG lands on LCK for critical damage, it asks the game for a new random number between 0 and LCK -1, then CRITICAL = ATT + (new random number) + 1

If RNG lands on CON for critical damage, CRITICAL = ATT + defense/2

So if Alucard with 35 strength gets a critical hit on Akmodan II with a Terminus Est and the Evil RNG lands on STR for critical damage, Alucard will hit for 68 damage.

How the game determines whether a hit is critical or not is equally complicated.

Each weapon has its own critical rate stat. When a weapon is used to attack, the critical rate of the weapon gets added to another number determined by the following formula:

SquareRoot((LCK\*2) + (random number from 0 to 15)) - 5

Whatever the result of your weapon crit rate plus the above formula, it then is tested against a random number from 0 to 255. If your number is higher than the random number, it's a critical hit.

Let's say Alucard has LCK of 17, and is attacking with a Terminus Est, which has a critical rate stat of 1. The random number between 0 and 15 ends up being 15. Here's how the formula now looks:

SquareRoot((17\*2) + 15) - 5 = 2 + 1 (from Terminus Est's crit rate stat) = 3

In this case, the RNG has to roll a number lower than 3 (0, 1 or 2) in order to land a critical hit, about a 1% chance.