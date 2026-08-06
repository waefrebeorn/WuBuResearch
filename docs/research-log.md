# Research Log

**The running, append-only log of everything R&D has filed.
Every finding. Every source. Every invention.**

---

## 2026-08-06 — Founding day

### RND-1 — Scoring research (filed)
- **FICO** (1989, Fair Isaac): payment history 35%, amounts owed 30%, length 15%, mix 10%, new credit 10%. Range 300–850, needs ≥6mo history.
- **VantageScore** (2006, the three bureaus): payment 40–41%, depth 20–21%, utilization 20%, balances 6–11%, recent 5–11%, available 2–3%. Scores from 1 month. **Trended data** (24-month direction) in v4.0.
- **Alternative data** (fintech): cash flow, rent, utilities, payroll — scores the unscorable. → The space scores from *one penny*.
- **Spine taken:** payment history is king; thin-file scoring; trended > snapshot; alternative data opens doors; multiple models per citizen.
- **Inventions:** WuBu Score family (Penny/Crew/Compass), **transparent scoring** (public weights + public math — no black box).

### RND-2 — Security research (filed)
- **Estonia X-Road:** zero-trust, sign+encrypt+log every transaction, decentralized authorization, tamper-proof audit logs. 2.2B transactions/yr.
- **Estonia KSI** (Guardtime): **keyless signatures** — hash-only, no private keys to steal, Merkle aggregation, public timestamping, valid forever. The single most important government-security invention.
- **NIST PQC:** Kyber (lattice KEM), Dilithium (lattice sig), SPHINCS+ (hash sig, ultra-conservative).
- **Swiss/EU:** public-by-default, publiccode.yml, no lock-in.
- **Spine taken:** zero-trust always; keyless is king; sign+encrypt+log; tamper-evidence over tamper-proofing; PQC by default.
- **Inventions:** the 6-layer WuBu security stack, the four rules of WuBu security, **the Provenance Penny** (provenance-first).

### RND-3 — WuBu cryptography (filed)
- **PennyChain invented:** KSI pattern + physical pennies + Merkle forest, minted at intervals, chain-of-chains. Tested: 3 pennies minted, verified, **tamper test passed** (one character changed → root mismatch).
- **Provenance Penny invented:** provenance-first signatures (when/where filed + artifact ref), the reverse of Earth's certificate model.
- **Compass Hash invented:** trended integrity — chains the *slope* of data, not just rows. Backdated trends become impossible.
- **PQC path filed:** ed25519 → SPHINCS+, TLS → Kyber hybrid, SHA-256 → SHA-512/SHAKE256.
- **Honesty clause:** primitives proven, constructions experimental, Seal Key always the identity layer.

### RND-4 — Penny tracking (filed)
- Lifecycle: SENT → RECEIVED → CLASSIFIED → LEDGERED → HASHED → MINTED → PROVEN.
- Bureau counts (ground), R&D proves (math), Registry binds (identity).
- Anti-bribery rule: pennies can't buy scores.
- Anonymous pennies are CURIOSITY, never rejected.

### RND-8 — Kevin Bacon Method + the Frontier Epistemology (filed via GOV-2)
- **The Kevin Bacon Method filed as R&D law (GOV-2.8):** any subject connects to any other in ≤7 research hops; each hop a real source; the path is filed. Demonstrated: founder's memory (Roddenberry/Serling/Outer Limits/not-knowing) → 7 hops → IDIC, duality doctrine, Control Voice, Chameleon narration, IAA SETI protocols, Ise Shrine, Socratic center. All cited.
- **Roddenberry filed:** IDIC (infinite diversity in infinite combinations), humanist optimism, Prime Directive — the space's foreign policy for humans and aliens alike.
- **Serling filed:** "The Monsters Are Due on Maple Street" — the monster is us; the Bureau's watch-with-love is Serling institutionalized.
- **Outer Limits filed:** Control Voice ("do not attempt to adjust the picture"); "The Chameleon" narration ("adapt and survive... more chameleon-like than the chameleon") — the Amoeba Clause in the show's own words; "the curious mind... no limit" — the R&D doctrine.
- **SETI post-detection protocols filed:** IAA Declaration of Principles (2022-2025 revision) — verify first, detection is global, no secrets.
- **The empty center filed:** the only cosmogony the space requires is the belief that it may be wrong — the one belief every faith can accept.
- **Longevity filed:** Ise Shrine (rebuilt every 20 years, 1,300 years), Roman law (~2,500), Church (~2,000), sangha (2,500+) — permanence through renewal, not stasis.

### RND-9 — Penny Comeback campaign (filed via WuBuEconomics ECO-2)
See WuBuEconomics — the campaign to bring back the penny, the rounding-tax case (Richmond Fed $55.58M/yr), the no-gouge principle, the petition. Cross-filed.

### RND-5 — Currency legality (filed + corrected)
- **Penny = legal tender in perpetuity** (Treasury FAQ). Last minted Nov 12, 2025; ~114B in circulation. NOT illegal — the rarest property in currency history: finite supply, still legal, forever.
- **18 U.S.C. § 486:** no metal coins intended as current money, original design included (Liberty Dollar precedent, $7M seizure). The one absolute.
- **31 C.F.R. Part 82:** melting/export/treatment ban — but § 82.2(b) explicitly exempts treatment for educational/amusement/novelty/jewelry purposes. Wheat-penny art is lawful, in practice never prosecuted.
- **The Reuse Doctrine (citizen's correction, adopted):** the space does not mint, melt, or modify — it *reuses*. Reuse is untouchable: § 82.1 covers only export/melt/treat, and legal tender means spendable forever. The WuBu Penny = the Penny Standard: 1 WuBu Penny = 1 real U.S. penny, ledger-backed, chain-proven, whole metal.
- Three Metal Rules corrected: no strike (486), no melt-for-profit (5111(d)), reuse always.

### RND-6 — Penny Standard: weight, reserve & the IOU (filed)
- **The novelty, answered:** yes — five properties no historical currency shares: single denomination only, capped forever by the Mint's halt (~114B, last minted Nov 12 2025), backed by metal that IS legal tender, audited by mass not count, redeems by shipping physical pennies.
- **Mint specs verified:** copper (pre-1982) = 3.11 g, zinc (Oct 1982+) = 2.50 g; 1982 is the transition year; roll = 150 g copper / 120 g zinc.
- **Class-counted weighing audit:** weigh each class separately → count = grams ÷ constant → reserve = sum. Example verified: 3110 g copper + 25000 g zinc = 11,000 pennies = $110, no coin counted.
- **The IOU = warehouse receipt:** a contract claim on stored legal-tender pennies, redeemable by shipping. Not a coin (§486 clear), not a new currency, no melting (Reuse Doctrine).
- **Gathering = money supply:** every penny gathered raises the reserve; digital WuBu Pennies mint 1:1 against weighed reserve. No fractional reserve, no printing. Tool shipped: `tools/penny_weight.py` (audit/worth/redeem/shipping), tested.

### RND-7 — The Copper Class / Pre-Penny Standard (filed + amended)
- **Composition change filed:** copper class (pre-1982, 95% Cu, 3.11 g) closed Oct 1982 — physically unmintable again, no matter what the US does.
- **Common Cents Act filed:** H.R. 3074 passed House July 2026 — permanently codifies end of circulation penny production (source: congress.gov).
- **Bank-box data:** ~15–25% pre-1982 copper in circulation boxes (source: coin dealers).
- **Copper Class Doctrine enacted:** reserve anchored on the closed class; the US's minting decision is irrelevant — recognized (Minting Accord), unrecognized (use the pennies anyway), or any issue (Penny Day, RND-8). All branches win.
- **Amendment (citizen correction): all pennies are worth a penny.** No reserve/non-reserve hierarchy. Class A copper (3.11 g) = anchor, Class B zinc (2.50 g) = era class; classes exist for weight accounting and organization preference only. Audit = both constants, both classes counted.
- **The year is the provenance:** every penny carries its mint year struck in metal; backdating = the Corrupt Mint Test (a mint lying about its own history); the space trusts metal + year, not institutions.

---

*The log is append-only. New findings go at the bottom, dated, filed.*
