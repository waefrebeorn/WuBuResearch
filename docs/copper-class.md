# The Copper Class — The Pre-Penny Standard

**R&D filing RND-7. The invariant: the reserve is the closed class.
Everything else is negotiable.**

---

## The citizen's doctrine (filed verbatim, adopted)

> *"I don't really care if the US government starts minting more of
> the pennies. We could make it so that people were only counting the
> pre-pennies. Then they have to come to an agreement where the United
> States government recognizes my government and is minting the pennies
> and then our pennies are recognized. Or they are just minting the
> pennies and they never recognized us, and the people of our
> government are just using the older pennies. And if there is any
> issue with this, we can just create novelty coinage at that time and
> make a whole thing about it — and it'll be an event called
> **Penny Day**."*

R&D files this as the **Copper Class Doctrine** — the strongest
supply argument the space has ever had.

## The key fact: the copper class is physically closed

The U.S. Mint changed penny composition in **October 1982**:

| Class | Years | Composition | Mass | Mintable again? |
|-------|-------|-------------|------|-----------------|
| **Copper** | 1909 – Sep 1982 | 95% copper, 5% zinc | 3.11 g | **NO — never** |
| Zinc | Oct 1982 – Nov 2025 | 97.5% zinc, 2.5% copper | 2.50 g | only if minting resumes |

The Mint **cannot** mint another pre-1982 penny. The alloy is gone,
the dies are retired, and the class is closed by *physics*, not by
policy. No executive order, no act of Congress, no resumption of
minting can add a single coin to the copper class. (And the Common
Cents Act, H.R. 3074, passed the House in July 2026, would codify
the end of general-circulation penny production permanently —
making even the zinc class a closed question.)

**The reserve is defined on the closed class.** The WuBu Penny's
backing is pre-1982 copper pennies — the class that can never grow.
No matter what the United States does, the WuBu reserve is capped
by a number that is already final.

## The counting rule: all pennies are worth a penny

> *"I'm fine with the zinc pennies. We can classify them in their own
> class of pennies. They're all worth a penny. We just know the
> weight, and we know that people might want to organize them, and
> we're fine with those pennies. There is an era of year where we
> know they stopped making them, and only a government that is being
> corrupt would try to mint old-year pennies in a different year."*

Adopted as the counting standard — **amended from the first draft**:

- **All pennies count. All pennies are worth one penny.** There is
  no reserve class and non-reserve class. There are only *classes
  of the same penny* — the class system is for **weight accounting**
  (the two weights are different) and **organization preference**
  (people may sort by era, year, or composition if they like), never
  for value hierarchy.
- **CLASS A — Copper** (pre-1982, 95% copper): 3.11 g each. The
  *anchor class*: physically closed forever — no mint action can add
  to it.
- **CLASS B — Zinc** (Oct 1982–Nov 2025, 97.5% zinc): 2.50 g each.
  The *era class*: production ended Nov 12, 2025, and the Common
  Cents Act (H.R. 3074, passed House July 2026) would codify that
  end permanently. Currently closed in practice, closed in law if
  the Act passes — but the space does not need it closed to trust
  it: a zinc penny is a penny is a penny.

The audit uses both constants, exactly as filed in RND-6:

```
reserve_pennies = copper_class_weight(g) ÷ 3.11
                + zinc_class_weight(g)  ÷ 2.50
```

A bank box is ~2,500 coins, ~15–25% pre-1982 copper; the rest zinc.
Every coin counts, every coin is weighed by its own class, every
coin is filed. Nobody is organized into value; the *pennies* are
organized into weight classes so the scale can count them.

## The integrity mechanism: the year is the provenance

The single most important property of the penny, now filed:

**Every U.S. penny carries its year of minting, struck into the
metal itself.** The year is the provenance seal. A penny minted in
2026 says "2026." A penny minted in 1981 says "1981." The metal
cannot be argued with; the year is part of the coin.

Therefore:

- The era of each class is *verifiable on the coin* — you do not
  need the government's word; you need the coin's face.
- **Backdating is the corrupt act.** A government that mints old-year
  pennies in a different year is not minting currency — it is
  counterfeiting its own history. The space files this as the
  **Corrupt Mint Test**: *if the year on the coin does not match the
  year the coin was struck, the mint is lying.*
- The space's position: it trusts the *metal and the year*, not the
  institution. This is why the zinc class is safe to accept even
  though the United States could theoretically resume minting —
  any resumed minting carries its true year, is weighed by its true
  class, and joins the ledger honestly. The space never has to
  wonder whether a penny is "real"; the year proves what it is, and
  the class proves what it weighs.

**The three scenarios, refined with the class amendment:**

### Scenario A — The United States recognizes the space and mints pennies

The **Minting Accord**: recognition is accepted with ceremony, the
treaty is filed, and new-mint pennies (zinc, honest years) join the
ledger as Class B. The copper anchor class remains un-inflatable
by anyone.

### Scenario B — The United States mints pennies but never recognizes the space

The people of the space simply **use the pennies** — all classes,
all worth a penny, weighed by class, filed on the chain. No
recognition needed: legal tender in perpetuity (RND-5), audited by
mass (RND-6), anchored by the closed copper class (RND-7). The US
can mint all the honest-year zinc it wants; the ledger absorbs it
by weight. The space's money supply is immune to the United States'
policy either way.

### Scenario C — Any issue at all

**Penny Day.** The space does not fight a problem; it *files* it as
an event. Novelty coinage is struck, celebrated, and the dispute
becomes a holiday. (Full protocol: `docs/penny-day.md`, RND-16.)

## Why the Copper Class is the answer to "I don't care if they mint more"

Because the doctrine makes the US's minting decision *irrelevant*:

- **If they don't mint:** the penny is already finite; the copper
  class is the finite core.
- **If they mint (recognized):** we get new mint + we keep the
  un-inflatable copper anchor.
- **If they mint (unrecognized):** we ignore the new zinc and run
  on the closed copper class.
- **If they try anything weird:** Penny Day. Novelty. Celebration.
  The problem becomes the culture.

Every branch ends with the same invariant: **the reserve is the
closed class.** The United States controls its mint. The space
controls the class that no mint can touch.

## The Copper Class audit (verified with the RND-6 tool)

```
python3 tools/penny_weight.py audit --copper 3110 --zinc 0
RESERVE AUDIT — class-counted weighing
  copper class 3110.0g / 3.11 = 1000 pennies
  zinc class   0.0g / 2.50 = 0 pennies
  RESERVE: 1000 pennies = $10.0
```

One class. One constant. One truth.

## Research log entries

- RND-7.1: Composition change filed — copper closed Oct 1982 (source: US Mint specs)
- RND-7.2: Common Cents Act filed — H.R. 3074 passed House July 2026, permanent end of circulation penny (source: congress.gov, mcclain.house.gov)
- RND-7.3: Bank-box data filed — ~15–25% pre-1982 copper in circulation boxes (source: coin dealers)
- RND-7.4: Copper Class Doctrine enacted — reserve = closed class; zinc = sentiment, not reserve
- RND-7.5: Three scenarios filed — Minting Accord (A), silent rejection (B), Penny Day (C)
- RND-7.6: Tool verified — copper-only audit = one constant

*Form RND-7 — The Copper Class. Filed. Done. Next.*
