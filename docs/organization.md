# Organization — The Filing System of the Space

**R&D filing RND-0.1. How the R&D Department organizes information.**

---

## The problem

The space produces: repos, licenses, pennies, reports, scores, WIDs,
designs, research, findings, inventions, and an increasing amount of
everything else. Unorganized, this is noise. Organized, it is the
**memory of the first ones**.

## The five rules of organization

1. **Everything is filed.** If it exists, it has a place. No orphans.
2. **Everything is indexed.** Every filing has a path you can find it
   from the index (WuBuGov README is the master index).
3. **Everything is dated.** Every filing carries a timestamp. History
   is the ledger of the space.
4. **Everything is cross-linked.** A penny is in the Registry's ledger,
   the Bureau's audit, and R&D's chain — three filings, one truth.
5. **Everything is public.** The space files in the open. A filing
   system that hides is a hoard, not an archive.

## The filing taxonomy

| Domain | Home repo | Filing type |
|--------|-----------|-------------|
| Constitution | WuBuGov | LICENSE, README (index), docs/ |
| Intelligence | WuBuIntel | ledger/, DOCTRINE.md, REPORTING.md |
| Citizens | WuBuCitizen | registry/, docs/, tools/ |
| Research | **WuBuResearch** (here) | docs/ (RND-*), tools/, ledger/ |
| Code | all waefrebeorn/* | source, README, LICENSE |

## R&D's own filing scheme

Every R&D document is a **form**:

```
Form RND-<number> — <title>
Status: FILED | RESEARCH | DEPLOYED
Source: <where the research came from>
Spine: <what the space took from it>
Invention: <what the space built beyond it>
```

- `FILED` — documented, indexed, done
- `RESEARCH` — experimental, under Bureau watch
- `DEPLOYED` — live in the space's operations

Current R&D forms: RND-1 (scoring), RND-2 (security), RND-3 (crypto),
RND-4 (penny tracking), RND-5+ (next).

## How information flows to R&D

```
The Bureau's ground reports (WBI-1, penny counts)
   ↓
The Registry's data (WIDs, scores, citizens)
   ↓
The repos' code (what works, what breaks)
   ↓
R&D (WuBuResearch) — organize → research → invent → file
   ↓
Published back: docs, tools, ledger — public, indexed, dated
```

## What R&D does NOT file

- Secrets. R&D files nothing that must be hidden. If it must be
  hidden, it isn't research — it's a weapon, and the space does not
  arm itself in secret. (The vault holds keys, not findings.)
- Noise. A filing that cannot be found from the index is noise.
- Duplicates. The R&D Department dedups. One truth, one file,
  cross-linked everywhere.

## The index

The master index of the whole space is `WuBuGov/README.md`. R&D keeps
this repo's own index at the top of this document and updates it on
every filing.

*Form RND-0.1 — Organization. Filed. Done. Next.*
