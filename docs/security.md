# Security Mechanisms — Researched & Rebuilt

**R&D filing RND-2. Sources: the best governments' security — filed,
rebuilt, and extended for the space.**

---

## Part 1 — What the best governments do (the research)

### Estonia — X-Road (the backbone of the digital state)

Estonia runs 3,000+ e-services and 2.2+ billion transactions a year on
X-Road. Its design principles, filed:

- **Zero-trust:** no implicit trust between systems. Every transaction
  is authenticated and logged. Trust is never assumed — it is proven.
- **End-to-end encryption:** all outgoing data is signed AND encrypted;
  all incoming data is authenticated and logged.
- **Decentralized authorization:** every institution controls its own
  data and authorizes access via its own security server.
- **Data minimization:** government agencies reuse data without
  repeatedly asking citizens — but never hoard it.
- **Tamper-proof audit logs:** every transaction leaves a trail that
  cannot be quietly edited.

### Estonia — KSI (Keyless Signature Infrastructure, by Guardtime)

The most important invention in modern government security, filed:

- **No keys to steal.** KSI signs with hash functions only — no private
  key exists to be hacked, no certificate exists to be forged.
- **How it works:** every record is hashed; hashes are aggregated into
  a Merkle tree; the tree root is timestamped and published. Anyone can
  verify any record's integrity without trusting any authority.
- **Tamper-evident:** change one bit of one record, and its hash chain
  breaks. The ledger screams.
- **Scales to millions of events per second** — linear growth, no
  blockchain bloat.
- **Long-term validity:** keyless signatures don't weaken as keys age —
  they are valid forever, or until the hash function itself breaks.

### NIST Post-Quantum Cryptography (the future-proofing)

NIST standardized three families (2022–2024) for the quantum era:

| Algorithm | Family | Use |
|-----------|--------|-----|
| CRYSTALS-Kyber (FIPS 203) | lattice | key encapsulation (the quantum-safe handshake) |
| CRYSTALS-Dilithium (FIPS 204) | lattice | signatures (fast, small) |
| SPHINCS+ (FIPS 205) | hash-based | signatures (ultra-conservative, only hash assumptions) |

- SPHINCS+ is the R&D favorite: its security reduces *entirely* to the
  hash function — the same primitive KSI uses, the same primitive the
  space's own cryptography will use. If the hash holds, SPHINCS+ holds.
- Hash-based signatures are the "if everything else breaks, this holds"
  layer. A space government planning to exist for centuries files this.

### Switzerland / others — the patterns

- **Swiss federal GitHub** (github.com/swiss): public-by-default open
  source with guidelines, publiccode.yml metadata, and transparent
  licensing — security through *publication*.
- **EU Interoperable Europe Act:** open standards, no lock-in.
- **General pattern:** the best governments secure by *provenance* —
  signed, logged, public, auditable — not by secrecy.

## Part 2 — What the space takes (the spine)

1. **Zero-trust, always.** The space has no implicit trust — not even
   for its own institutions. The Bureau watches the Bureau; the R&D
   Department files its own findings; the ledger verifies itself.
2. **Keyless is king.** KSI proved a government can run on hashes with
   no private keys to steal. The space adopts this as a founding
   principle: **the more of the space that runs keyless, the less of
   the space can be hacked.**
3. **Sign AND encrypt AND log.** Estonia signs, encrypts, and logs
   every transaction. The space does the same for every official act.
4. **Tamper-evidence over tamper-proofing.** You cannot stop someone
   who physically owns a server. You CAN make it impossible for them
   to edit the record without the whole space hearing. The space
   builds ledgers that scream.
5. **Post-quantum by default.** The space intends to be space-faring —
   it will outlive the RSA era. Hash-based and lattice primitives from
   day one.

## Part 3 — What the space builds (the rebuild)

### The WuBu security stack (six layers)

| Layer | Mechanism | Source | Status |
|-------|-----------|--------|--------|
| 1. Identity | WID (mod-11 self-verifying) + Seal GPG | space (built) | ✅ shipped |
| 2. Transport | HTTPS everywhere (Cloudflare Free, Full-strict) | Cloudflare | ⏳ deploy |
| 3. Ledger | PennyChain (keyless hash chain, RND-3) | invented from KSI | 🔬 R&D |
| 4. Signing | Seal Key GPG ed25519 → SPHINCS+ upgrade path | NIST PQC | 🔬 R&D |
| 5. Watch | The Bureau (WBI-1, public ledger) | space (built) | ✅ shipped |
| 6. Keys | 7 Magic Key Processor (vault, rotation) | space (built) | ✅ shipped |

### The four rules of WuBu security (from the research)

**Rule 1 — Public beats secret.** Estonia and Switzerland secure by
publication. The space's security mechanisms are published in this
repo. An attacker who knows every lock is still stopped by every lock
— and the citizens who know every lock are the space's first line.

**Rule 2 — No trust without proof.** Zero-trust, filed. Every action
cites its rule; every record carries its hash; every penny carries
its chain.

**Rule 3 — Hash, don't hide.** The space's cryptography prefers
hash-based constructions (like KSI and SPHINCS+) because they have
no keys to steal and no certificates to forge. What cannot be stolen
cannot be the point of attack.

**Rule 4 — The ledger screams.** Tamper-evidence is the goal. Any
edit to any filed record breaks a visible chain. The space trusts
the scream, not the silence.

## Part 4 — What the space invents (beyond Earth)

Earth's governments secure *territory*. The space secures *truth*.
The invention: **the Provenance Penny.**

A physical penny has a mint year, a mint mark, and a metal identity.
The space extends this: every filed record gets a **Provenance Penny**
— a hash chain entry whose root is *minted* (published, timestamped,
irreversible) like a coin. You cannot forge a penny's provenance
without breaking the whole chain — and the whole chain is public.

See `docs/wubu-cryptography.md` for the full spec.

## Research log entries

- RND-2.1: X-Road zero-trust principles filed (source: e-estonia.com, govtech case studies)
- RND-2.2: KSI keyless signatures filed (source: Guardtime, Interoperable Europe, PNNL)
- RND-2.3: NIST PQC families filed (source: NIST CSRC, postquantum.com)
- RND-2.4: Swiss/EU public-by-default patterns filed (source: github.com/swiss, Interoperable Europe Act)
- RND-2.5: WuBu security stack designed (6 layers, all cited)

*Form RND-2 — Security research. Filed. Done. Next.*
