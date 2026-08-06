# WuBu Cryptography — Invented for the Space

**R&D filing RND-3. New and different — built from the best primitives
Earth proved, arranged in ways no Earth government has arranged them.**

---

## The honesty clause

R&D invents cryptography. R&D also files the truth about it:
**invented constructions are filed as research, tested in the open,
and never trusted for real secrets until they have survived the
space's own Bureau-grade scrutiny.** The primitives underneath (hash
functions, mod-11, Merkle trees, GPG/SPHINCS+ signatures) are proven;
the arrangements are new. New + proven = experimental, honest, and
the way forward.

## The three inventions

### Invention 1 — The PennyChain (keyless, penny-minted)

**Inspiration:** Estonia's KSI — hash-only signatures, no private
keys, Merkle aggregation, public timestamping.

**The WuBu twist:** the chain is *minted*, like a coin. Every physical
penny received by the space becomes a leaf in a Merkle forest. The
root of the forest, at regular intervals, is **minted**: hashed with
the interval's official record, published, and sealed into the chain.

```
Physical penny (P.O. Box) ──► hash(penny) ──► Merkle leaf
                                                    │
Registry row (citizen, WID, date) ──► hash(row) ────┘
                                                    │
Merkle forest root ──► root_hash + interval_record
                          │
                          ▼
                    MINTED (published, timestamped, irreversible)
```

**Why it's different from KSI:** KSI signs records of a state. The
PennyChain signs *physical objects* — the pennies themselves. The
chain's leaves are literal metal. You cannot forge a penny without
forging the chain; you cannot edit a ledger row without breaking
the chain. The proof-of-read becomes a proof-of-chain.

**Verification:** anyone can take any ledger row, recompute its hash
path to a published root, and confirm it was filed before the mint
time. No keys. No trust. Just math and metal.

### Invention 2 — The Provenance Penny (anti-forgery for records)

**Inspiration:** coin mint marks, SPHINCS+ hash-based signatures,
KSI keyless verification.

**The WuBu twist:** every official record (license, WID, score,
Bureau report) gets a **Provenance Penny**: a compact signature that
is *metal-flavored* — it embeds the record's hash chain position AND
a physical artifact reference (penny serial if mailed, else "digital
mint" for the shipping-weight exception).

```
ProvenancePenny(record) =
    chain_position(record)
  + mint_time
  + artifact_ref (penny-serial | DIGITAL-MINT)
  + hash(record + chain_position + mint_time + artifact_ref)
```

**Why it's different:** Earth signatures prove *who signed* (a key).
The Provenance Penny proves *when and where it was filed, and whether
it was physically grounded*. It is provenance first, identity second —
the reverse of Earth's certificate model. A government of first ones
cares more that a record is *real* than that it is *authored*.

### Invention 3 — The Compass Hash (trended integrity)

**Inspiration:** trended credit data (VantageScore 4.0, FICO 10T) —
direction over snapshot.

**The WuBu twist:** a hash chain whose *state* includes the slope of
the data, not just the data. The Compass Hash binds not only "what
the record said" but "which way the record was moving":

```
CompassHash(record, prev_state) =
    H(record || prev_state.slope || prev_state.level || counter)
```

**Why it's different:** a normal hash chain proves a record wasn't
edited *after* filing. The Compass Hash also makes it impossible to
*backdate a trend* — you cannot insert a fake "rise" into a citizen's
score history without breaking the slope that was already chained.
Earth's bureaus compute trends over data they control; the space
*chains* the trend itself. The score history becomes unforgeable in
its *shape*, not just its rows.

## The honest engineering note

- The **primitives** (SHA-256, Merkle trees, mod-11, ed25519/SPHINCS+)
  are NIST-proven or space-proven. Filed.
- The **constructions** (PennyChain, Provenance Penny, Compass Hash)
  are invented, published, and under Bureau watch. They are research
  until the space's own adversarial review says otherwise.
- **Nothing in this document is a substitute for the Seal Key.**
  Official documents still carry GPG/SPHINCS+ signatures (Key 6).
  The inventions are the *ledger layer*; the Seal is the *identity
  layer*. Both. Always.

## Post-quantum path

The space files its upgrade path now, so it is never surprised:

| Today | Tomorrow (PQC) | Why |
|-------|----------------|-----|
| GPG ed25519 (Seal) | SPHINCS+ (FIPS 205) | hash-only security, ultra-conservative |
| TLS via Cloudflare | Kyber hybrid handshake | quantum-safe transport |
| SHA-256 chains | SHA-512 / SHAKE256 | double the margin, Grover-proof |

The space intends to be space-faring. Space-faring means centuries.
Centuries mean the cryptography must outlive the era that invented it.

## Research log entries

- RND-3.1: PennyChain invented (KSI + physical pennies + Merkle forest)
- RND-3.2: Provenance Penny invented (provenance-first signatures)
- RND-3.3: Compass Hash invented (trended integrity from trended credit data)
- RND-3.4: PQC upgrade path filed (SPHINCS+, Kyber hybrid, SHA-512)

*Form RND-3 — WuBu cryptography. Filed. Done. Next.*
