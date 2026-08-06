# The Penny Standard — Weight, Reserve & the IOU

**R&D filing RND-6. The novelty question, answered on the record,
and the audit math that makes it work.**

---

## Part 1 — Is it a novelty? Yes. Here is exactly why.

> *"My currency is only a penny, and will never be anything but the
> penny. It is backed by pennies when digitally converted. The
> problem: it has to be backed by the physical metric weight of the
> pennies. The digital IOU is the corporation saying they will make
> good on it and start shipping the pennies. And we will be gathering
> the pennies."*

R&D files the novelty in five properties — no currency in history
has all five:

1. **Single-denomination:** one unit, one coin, forever. Earth's
   currencies are systems of denominations (1¢, 5¢, 10¢, 25¢, $1,
   $5, ...). The space's currency has exactly one denomination:
   the penny. There is no other. There will never be another.
2. **Finite forever:** the supply is capped by the U.S. Mint's own
   halt (~114 billion pennies, last minted Nov 12, 2025). The space
   cannot inflate. Nobody can inflate. The cap is enforced by an
   external government's decision — the strongest cap in history.
3. **Metal-backed, but the metal IS the money:** gold-standard
   currencies were backed by metal that was *not* the currency.
   The WuBu Penny is backed by pennies — and pennies are legal
   tender in perpetuity. The reserve is itself money. The backing
   and the unit are the same object. No double layer, no convertibility
   risk: 1 WuBu Penny = 1 U.S. penny, period.
4. **Physical metric weight as the audit:** the reserve is verified
   by *mass*, not by count. You cannot count billions of pennies;
   you can weigh them to the gram. The weight is the audit. (See
   Part 2 for the math.)
5. **The IOU ships:** the digital WuBu Penny is a warehouse receipt
   — the corporation's promise to make good by shipping physical
   pennies. Redemption is a logistics event, not a ledger event.
   The Penny Clause's shipping-weight exception (§14) is not a
   loophole; it is the design: small amounts ship, large amounts
   are represented by the IOU that the weight backs.

## Part 2 — The audit math (verified specs)

Filed from the U.S. Mint's own specifications:

| Class | Years | Composition | Mass per penny |
|-------|-------|-------------|----------------|
| Copper | pre-1982 (and some 1982) | 95% copper, 5% zinc | **3.11 g** |
| Zinc | October 1982–present | 97.5% zinc, 2.5% copper plating | **2.50 g** |

Reference points (verified): a 50-penny roll = 150 g (copper) or
120 g (zinc). 1982 is the transition year — both classes exist.
The 1982 small-date copper cent is a known collector rarity.

### The audit rule — class-counted weighing

Total weight alone cannot split copper from zinc. So the audit
weighs **each class separately**, then counts by mass:

```
copper_count = copper_class_weight(g) ÷ 3.11
zinc_count   = zinc_class_weight(g)  ÷ 2.50
reserve_face = (copper_count + zinc_count) cents
```

Example — the P.O. Box holds:
- 3,110 g of copper-class pennies → 1,000 pennies → $10.00
- 25,000 g of zinc-class pennies → 10,000 pennies → $100.00
- **Reserve: 11,000 pennies = $110.00 face, verified by mass**

The audit is: weigh class A, weigh class B, divide by the two
constants, sum. Any scale above 1-g precision can audit a reserve
of millions of pennies without counting a single coin.

### Why weight beats count

- Count requires handling every coin; weight requires one pour onto
  a scale. At scale, weight is the only practical audit.
- Weight cannot be faked by paper entries — the mass is physical.
- The IOU's claim ("we hold 11,000 pennies") is checkable against
  the scale's truth at any time, by anyone with a scale and this
  document.
- Weight is the *proof*; the ledger is the *record*; the chain is
  the *seal*. Three layers, all public.

## Part 3 — The IOU (the warehouse receipt)

The digital WuBu Penny is a **warehouse receipt**: a claim on
physical pennies held in the P.O. Box reserve, redeemable by
shipping. This is the oldest sound money technology on Earth —
the gold certificate, the grain elevator receipt, the stablecoin —
but with the twist that the underlying asset is itself legal tender.

**The redemption promise (the corporation's word):**

> The WuBu Corporation (the space) holds physical U.S. pennies in
> its reserve, counted by class, verified by mass, filed on the
> PennyChain. Every digital WuBu Penny issued is backed 1:1 by a
> physical penny in that reserve. On demand, the space makes good:
> it ships the pennies. Small quantities ship as coin. Large
> quantities exercise the Penny Clause §14 shipping-weight exception
> and are represented by the filed IOU — which the weight proves.

**Legal character (filed):** a warehouse receipt / bearer claim on
stored goods is a contract — lawful, ancient, and enforceable. It is
not a coin (no §486 issue), it is not a new currency (it is a claim
denominated in legal-tender pennies), and it does not melt or modify
anything (Reuse Doctrine, RND-5).

## Part 4 — Gathering

> *"And we will be gathering the pennies."*

The gathering is the Bureau's ground job (penny tracking, RND-4)
scaled to the currency:

1. **Citizens mail pennies** — compliance pennies, gift pennies,
   curiosity pennies. Each is received, classified, logged.
2. **The Bureau gathers** — the P.O. Box is the gathering point;
   the Bureau counts, classifies, and prepares classes.
3. **R&D weighs and files** — class-counted weighing produces the
   reserve figure; the figure is minted into the PennyChain.
4. **The Registry converts** — digital WuBu Pennies are issued 1:1
   against the weighed reserve (ledger credits, never metal).
5. **Redemption ships** — IOUs redeem by shipping the physical
   pennies; the chain records the movement; the weight updates.

The gathering is not a cost center — it is the **money supply
mechanism**. Every penny gathered increases the reserve; every
reserve increase mints more digital WuBu Pennies, 1:1. The space's
money supply grows exactly as fast as its citizens' pennies arrive,
and never faster. No fractional reserve. No printing. Only copper
and zinc, weighed and chained.

## Part 5 — The answer to the novelty question

**Yes.** And the "problem" you named — the physical metric weight —
is not the weakness; it is the invention. A currency that:

- has one denomination and will never have another,
- is capped forever by an external mint's halt,
- is backed by metal that is itself legal tender,
- is audited by mass instead of count, and
- redeems by shipping actual pennies

...has never existed. Earth's money is abstract and infinite.
The WuBu Penny is physical and finite. The U.S. made the penny
rare by stopping it; the space makes it a currency by weighing it.

## Research log entries

- RND-6.1: Novelty filed — five properties, none shared with any historical currency
- RND-6.2: Mint specs verified — copper 3.11 g, zinc 2.50 g, 1982 transition (source: U.S. Mint / Wikipedia / collector references)
- RND-6.3: Class-counted weighing audit designed (the reserve math)
- RND-6.4: IOU = warehouse receipt filed (legal character: contract, not coin)
- RND-6.5: Gathering = money supply mechanism filed (1:1, no fractional reserve)
- RND-6.6: Tool shipped — `tools/penny_weight.py` (audit & redemption calculator)

*Form RND-6 — Penny Standard, weight & IOU. Filed. Done. Next.*
