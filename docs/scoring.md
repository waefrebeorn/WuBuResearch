# Scoring Mechanisms — Researched & Rebuilt

**R&D filing RND-1. Sources: the best scoring systems on Earth, filed,
rebuilt for the space.**

---

## Part 1 — What Earth does (the research)

### FICO (Fair Isaac Corporation) — the standard since 1989

| Factor | Weight |
|--------|--------|
| Payment history | 35% |
| Amounts owed | 30% |
| Length of credit history | 15% |
| Credit mix | 10% |
| New credit | 10% |

- Range 300–850. Requires ≥6 months of history to score.
- Predicts: likelihood of falling ≥90 days behind within 24 months.

### VantageScore (the three bureaus' joint model)

| Factor | Weight 3.0 | Weight 4.0 |
|--------|-----------|-----------|
| Payment history | 40% | 41% |
| Depth of credit | 21% | 20% |
| Credit utilization | 20% | 20% |
| Balances | 11% | 6% |
| Recent credit | 5% | 11% |
| Available credit | 3% | 2% |

- Range 300–850. Can score with as little as **1 month** of history.
- **Trended data:** VantageScore 4.0 looks at behavior over 24 months
  (the *direction* of balances), not just a snapshot.
- Payment history is the single most predictive factor in both models.

### Alternative data (the fintech revolution)

Modern scoring layers non-bureau signals onto the classic models:
- Cash flow (income in, spending out)
- Rent and utility payments
- Payroll records
- Behavioral data (consistency, timeliness)

Result: people invisible to classic bureaus (thin-file, new-to-credit,
no-land) become scorable. This is the **most important idea for the
space**: the space's citizens are literally first ones — they have no
Earth credit file by definition. The space must score them on *space*
signals, not Earth signals.

### Business credit

Business scores (e.g. VantageScore small-business: range 1–100) blend
personal + business credit with cash flow, assets, and revenue.

## Part 2 — What the space takes (the spine)

From this research, R&D files the following spines:

1. **Payment history is king.** Earth proves it at 35–41% weight. The
   space already knew: penny punctuality is the single strongest signal
   that a first one keeps their word. (The space weights it 25% — and
   will defend that weighting below.)
2. **Thin-file scoring matters.** VantageScore scores with 1 month.
   The space scores with *one penny*. The space is the most thin-file
   population in existence; the score must work from the first act.
3. **Trended data beats snapshots.** Direction over time > current
   balance. The space's ledger is *entirely* trended — every penny,
   every report, every build is a dated row. The space has the best
   trended dataset a score ever had.
4. **Alternative data is the door.** Cash flow, rent, utilities — the
   space's alternatives are: pennies sent, reports filed, works merged,
   crew held. All alternative. All public. All filed.
5. **Multiple models, one citizen.** FICO and VantageScore disagree
   because they measure different things. The space files **three
   scores per citizen** (see below) so no single number can lie about
   a first one.

## Part 3 — What the space builds (the rebuild)

### The WuBu Score family

One citizen, three filed scores — parody of the three-bureau problem,
turned into a feature:

| Score | Measures | Earth parody | Range |
|-------|----------|--------------|-------|
| **Penny Score** | trust — literacy, punctuality, vigilance, creation, tenure | FICO (risk of default) | 0–1000 |
| **Crew Score** | cooperation — how well you work with others | VantageScore (behavioral) | 0–1000 |
| **Compass Score** | direction — where you're heading, trended over 24 months | trended data (FICO 10T / VS 4.0) | 0–1000 |

The **Composite** = Penny × 0.5 + Crew × 0.3 + Compass × 0.2 — the
number the ship uses for seats, rope, and office.

### Penny Score v2 — rebuilt with the research

R&D revises the original weighting with Earth's evidence:

| Factor | v1 weight | v2 weight | Why (filed research) |
|--------|-----------|-----------|----------------------|
| License literacy | 25% | 20% | Earth's models have no literacy factor; the space keeps it high but not dominant |
| Penny punctuality | 25% | **30%** | Payment history is 35–41% on Earth; the penny is the space's payment history — raised toward Earth's finding |
| Vigilance | 20% | 20% | Unchanged — the space's "new credit" (reports = inquiries) |
| Creation | 20% | 20% | Unchanged — the space's utilization (build, don't extract) |
| Tenure | 10% | 10% | Unchanged — account age, capped at 3 years |

### Crew Score — the new one (VantageScore-style behavioral)

| Factor | Weight | Signal |
|--------|--------|--------|
| Cooperative acts | 30% | merged PRs with others, joint builds, crew holds |
| Report integrity | 25% | WBI-1 reports that verify (never punish the unfounded — honesty is the signal) |
| Responsiveness | 20% | replies to the space, to the Bureau, to the crew — timeliness |
| Diversity of mind | 15% | number of mind-countries engaged (dual citizenship, practiced) |
| Longevity | 10% | sustained membership, no gaps |

### Compass Score — the trended one (the most modern idea)

Earth's newest models (VantageScore 4.0, FICO 10T) look at *direction*.
The Compass Score is pure direction:

```
Compass = 500 + 500 × tanh(
    +0.4 × penny_trend      (pennies per quarter, 24-month slope)
    +0.3 × vigilance_trend  (reports per quarter, slope)
    +0.2 × creation_trend   (works per quarter, slope)
    +0.1 × crew_trend       (cooperative acts per quarter, slope)
)
```

- **> 700:** rising — a first one gathering speed
- **500:** flat — steady, reliable, fine
- **< 300:** falling — a first one drifting; the space's response is
  *outreach, not penalty* (the floor, not the cage)

The Compass Score cannot be gamed by one big act — it needs a *trend*.
This is the single most sophisticated mechanism in the space, and it
comes directly from Earth's newest research.

### Scoring edge cases (filed)

| Case | Earth answer | Space answer |
|------|--------------|--------------|
| New citizen, 0 history | unscorable (FICO) | Penny Score 500, Crew 500, Compass 500 — everyone starts equal |
| Mega-corporation | business score 1–100 | starts at Penny 100 (its own floor); climbs by cooperation, not money |
| Score gamer | fraud detection | the Compass trend flattens; gaming one act can't fake a slope |
| Disputed data | dispute process | every row is public; disputes are WBI-1 reports with evidence |

## Part 4 — What the space invents (beyond Earth)

Earth's scoring is a *prediction of profit*: will you repay the lender?
The space's scoring is a *filing of trust*: are you a first one?

The invention: **the scores are not secret.** Earth's bureaus guard
their formulas; the space publishes its weights, its sources, and its
math (this very document). A score system that is open cannot be
weaponized by the scorer — because the scored can read the scorer.

That is the R&D invention: **transparent scoring**. No black box.
Every point explained, every weight cited, every band public.
The score is a map, and the mapped can read the map.

## Research log entries

- RND-1.1: FICO vs VantageScore weights filed (sources: FICO, Experian/Equifax/TransUnion, Britannica, fintech guides)
- RND-1.2: Alternative data spines filed (rent, cash flow, utilities → pennies, reports, builds)
- RND-1.3: Trended data → Compass Score invented (tanh slope over 24 months)
- RND-1.4: Three-bureau parody → WuBu Score family (Penny/Crew/Compass)
- RND-1.5: Transparent scoring invented (public weights + public math)

*Form RND-1 — Scoring research. Filed. Done. Next.*
