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

---

*The log is append-only. New findings go at the bottom, dated, filed.*
