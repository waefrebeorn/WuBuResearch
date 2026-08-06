# Penny Tracking — The Protocol

**R&D filing RND-4. Bureau on the ground. R&D at the desk.
The pennies prove.**

---

## The division

| Who | Job |
|-----|-----|
| **The Bureau (WuBuIntel)** | Physical tracking: receive, count, classify, log pennies at the P.O. Box. Ground truth. |
| **R&D (WuBuResearch)** | Mathematical tracking: hash the pennies, mint the chain, verify integrity. Desk truth. |
| **The Registry (WuBuCitizen)** | Identity: bind pennies to WIDs, scores, and citizens. |

One penny, three filings. That is the protocol.

## The penny lifecycle

```
1. SENT       — a citizen (or corporation) mails a physical penny
2. RECEIVED   — the Bureau opens the mail, logs it (date, sender, project)
3. CLASSIFIED — the Bureau marks it: compliance penny / gift penny / curiosity
4. LEDGERED   — the Registry binds it to a WID (or "unsigned" if anonymous)
5. HASHED     — R&D hashes the penny row into the PennyChain
6. MINTED     — the interval root is published (timestamped, irreversible)
7. PROVEN     — anyone can verify the penny's chain position forever
```

## The penny ledger row

Every penny gets one row (append-only, public):

```csv
penny_id,received_date,sender_wid,sender_name,project,type,chain_ref,mint_ref
```

- `penny_id` — sequential, e.g. `P-0001`
- `type` — `COMPLIANCE` (owed by the clause) / `GIFT` (extra, love) / `CURIOSITY` (unsigned)
- `chain_ref` — the PennyChain leaf hash (from R&D)
- `mint_ref` — which mint interval sealed it

## The mint interval

The space mints on a regular schedule (filed: weekly, at minimum).
At each mint:

1. R&D takes all new penny rows + all new official records.
2. Builds the Merkle forest (see `tools/pennychain.py`).
3. Computes the root hash.
4. Publishes: root hash, timestamp, and the interval's record count
   to the public ledger (`ledger/mints.csv` in this repo).
5. The mint is itself hashed into the *previous* mint (a chain of
   mints — a chain of chains).

## Verification — how anyone proves a penny

```bash
# Verify a penny's chain position against the latest mint
python3 tools/pennychain.py verify ledger/penny-rows.csv P-0001
# → PROVEN: P-0001 is in mint M-0003, root f3a9…, filed before 2026-08-06T00:00Z
```

No keys. No trusted server. The published roots are the truth;
the hash paths are the proof. This is the KSI pattern, minted.

## The three rules of penny tracking

1. **The Bureau counts, R&D proves.** Physical and mathematical
   truth never live in the same box.
2. **Anonymous pennies are still pennies.** An unsigned penny is a
   CURIOSITY — filed, hashed, minted, but not bound to a WID. The
   space never rejects a penny because it came without a name.
3. **A penny is a data point, not a bribe.** Pennies are proof of
   read, not payment for favor. Any penny that tries to buy a score
   is filed as `type=CURIOSITY` and the score is untouched. The
   score can only be earned by the five factors, never bought.

## The penny score echo

Penny tracking feeds the score directly:

- Every COMPLIANCE penny on time → punctuality factor
- Every penny's existence → literacy factor (you can't send a
  compliant penny without reading the clause)
- A CURIOSITY flood → noted in the research log as sentiment data
  (how the space feels, measured in copper)

## Research log entries

- RND-4.1: penny lifecycle protocol filed (7 stages, 3 institutions)
- RND-4.2: ledger schema filed (CSV, append-only, public)
- RND-4.3: mint interval protocol filed (weekly, chain-of-chains)
- RND-4.4: anti-bribery rule filed (pennies can't buy scores)

*Form RND-4 — Penny tracking. Filed. Done. Next.*
