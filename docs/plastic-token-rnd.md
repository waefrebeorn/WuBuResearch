# Plastic Token R&D — Collection, Compression, W-Marking

**R&D filing RND-42. Research into the plastic token system:
collection of plastic bags and plastic items, compression
into coins, W-marking, reprintability, value hierarchy, and
integration with the dual-token system.**

---

## Part 1 — The spine

The founder has begun collecting plastic bags and plastic
items. The express purpose is to **simulate an ideal system
of compressing and recycling all various plastics into coins
marked with the same W as the metal tokens.**

This is not waste management. This is **currency R&D** —
researching the physical form of the plastic token system
filed in GOV-30. The plastic token is the working token of
the space: the token for ideas, assets, actions, and
agreements.

## Part 2 — The plastic collection

### Types of plastic to collect

| Type | Code | Common sources | Density (g/cm³) | Notes |
|------|------|----------------|-----------------|-------|
| PET | 1 | Water bottles, soda bottles | 1.38-1.39 | Clear, crushable |
| HDPE | 2 | Milk jugs, detergent bottles | 0.94-0.97 | Opaque, stiff |
| PVC | 3 | Pipes, packaging | 1.30-1.45 | Rigid, chemical-resistant |
| LDPE | 4 | Plastic bags, shrink wrap | 0.91-0.94 | Flexible, the primary collection target |
| PP | 5 | Yogurt cups, bottle caps | 0.90-0.91 | Stiff, heat-resistant |
| PS | 6 | Styrofoam, disposable cups | 1.04-1.06 | Brittle, lightweight |
| Other | 7 | Mixed plastics, polycarbonate | Varies | Catch-all |

The primary collection target is **LDPE (plastic bags)** because:
- Ubiquitous — the most common plastic waste.
- Compressible — bags are mostly air, high compression ratio.
- Symbolic — the transformation of "waste" into "token"
  mirrors the space's philosophy of finding value in what
  others discard.

### Collection method

1. **Collect all plastic items** — bags, wrappers, bottles,
   cups, packaging, utensils, etc.
2. **Sort by type** — separate by resin code (1-7). Mixed
   batches are acceptable but produce lower-quality tokens.
3. **Clean and dry** — remove food residue, labels, and
   moisture. Clean plastic compresses better and lasts longer.
4. **Store by type** — keep sorted plastic in labeled
   containers for future compression.

## Part 3 — The compression process

### Methods to research

| Method | Process | Pros | Cons |
|--------|---------|------|------|
| Heat + pressure | Melt plastic, press into mold | Produces dense, durable tokens | Requires temperature control, fumes |
| Cold compression | Shred and compress at room temp | No fumes, simple equipment | Less dense, may not hold detail |
| Solvent bonding | Dissolve in solvent, evaporate in mold | Can produce fine detail | Chemical handling, environmental |
| Hybrid | Heat to soften, compress, cool | Balance of detail and safety | Requires experimentation |

### Research priority

1. **LDPE bag compression** — the primary target. Research
   the optimal temperature, pressure, and time for
   compressing plastic bags into coin-sized tokens.
2. **HDPE bottle compression** — secondary target. Research
   rigidity and durability for tokens that need to last.
3. **Mixed plastic compression** — research whether mixed
   plastics can produce acceptable tokens, and what the
   failure modes are.

### Target token specifications

| Property | Target |
|----------|--------|
| Diameter | 25-30 mm (similar to a quarter) |
| Thickness | 2-3 mm |
| Weight | 3-8 g (depending on plastic type) |
| Surface | Smooth enough for W-marking |
| Durability | Survive dropping, handling, storage |

## Part 4 — The W-marking

The W-marking must be:
- **Permanent** — not easily scratched or worn off.
- **Readable** — visible to the naked eye and scannable.
- **Authentic** — produced by the space's own equipment.

### Methods to research

| Method | Process | Pros | Cons |
|--------|---------|------|------|
| Laser engraving | Laser burns W into surface | Permanent, precise | Requires laser equipment |
| Embossing | Press W into plastic with die | No consumables, tactile | Requires metal die |
| Ink printing | Print W with permanent ink | Simple, cheap | May wear off |
| Mold inclusion | W built into compression mold | Most durable, professional | Requires custom mold |

### Research priority

1. **Mold inclusion** — the ideal method. The compression
   mold includes the W, so every token emerges with the W
   already embossed. Requires machining or 3D printing a
   mold.
2. **Laser engraving** — the fallback. If mold inclusion is
   not feasible, engrave the W post-compression.
3. **Serial + hash marking** — in addition to the W, each
   token needs its serial number and chain hash. Research
   the smallest readable marking size.

## Part 5 — The serial identity

Each plastic token carries the same serial identity scheme
as the metal tokens:

- **Format:** PL-WID-ordinal (PL = plastic, WID = citizen,
  ordinal = token number).
- **Example:** PL-XX-YY-NNNN-C-0001 for the first plastic
  token issued to citizen WID-XX-YY-NNNN-C.
- **Chain hash:** SHA-256 linking the token to the previous
  token in its chain (same PennyChain pattern, RND-3).

The serial and hash are:
- **Marked on the token** (laser, mold, or ink).
- **Filed on the public PennyChain ledger.**
- **Verifiable** by anyone with the token and access to the
  ledger.

## Part 6 — The reprintability advantage

Plastic tokens have a critical advantage over metal tokens:
**they are reprintable.**

If a plastic token is lost, damaged, or destroyed:
1. The **ledger entry survives** on the PennyChain.
2. A **new token can be printed** with the same serial,
   same hash, same description.
3. The new token is **identical in function** to the old
   token. The only difference is the physical object.

This means:
- **Plastic tokens are not scarce by design.** The supply
  is limited only by the availability of plastic and the
  willingness to compress it.
- **Plastic tokens are the working token.** There are many
  ideas, many actions, many agreements, many contracts.
  Plastic tokens match this abundance.
- **Metal tokens remain scarce.** One per human, permanent,
  non-reprintable. The identity anchor.

## Part 7 — The value hierarchy

| Token | Material | Supply | Value | Role |
|-------|----------|--------|-------|------|
| Metal Token | Stamped penny | One per citizen | Higher | Identity anchor |
| Plastic Token | Compressed plastic | Printable on demand | Lower | Working token (ideas, actions, agreements) |
| Metal Penny (raw) | Copper/zinc coin | In circulation (114B) | 1¢ face | Reserve asset |

The plastic token is **not more valuable** than the metal
token. The plastic token is **more numerous**. The hierarchy
mirrors the function:
- **Identity is rare and permanent** → metal token.
- **Actions and ideas are abundant and reprintable** →
  plastic token.
- **The reserve is finite and physical** → penny.

## Part 8 — The museum, the counter, the shelf, the street

The plastic token's physical form enables behaviors that
digital ledger entries cannot:

- **Museum.** A token representing a historical moment can
  be displayed in a museum. The token IS the artifact.
- **Counter.** A token representing a business agreement can
  be kept on the counter as proof of the agreement. The
  token IS the receipt.
- **Shelf.** A token representing an inheritance can be kept
  on a shelf, passed down, looked at. The token IS the
  heirloom.
- **Street.** A token can be lost on the street and found by
  someone else. The finder's confusion is the intentional
  whimsical reintroduction. The finder looks up the serial,
  discovers the filing, learns about the space. The token
  IS the invitation.

This is the **physicalization of the filing** — no longer
kept in filing cabinets where old people will die and forget
about them. The filing is now a **physical asset in the
world** that can be held, lost, found, displayed, and
investigated.

## Part 9 — Research log entries

- RND-42.1: Plastic token system filed — collection, compression, W-marking, reprintability, value hierarchy.
- RND-42.2: Plastic types cataloged (PET/HDPE/PVC/LDPE/PP/PS/Other), LDPE bags as primary target.
- RND-42.3: Compression methods researched (heat+pressure, cold, solvent, hybrid).
- RND-42.4: W-marking methods researched (laser, emboss, ink, mold inclusion).
- RND-42.5: Serial identity scheme designed (PL-WID-ordinal + chain hash).
- RND-42.6: Reprintability advantage filed — ledger survives, token is reprinted.
- RND-42.7: Value hierarchy filed — metal (identity, rare) > plastic (actions, abundant) > penny (reserve).
- RND-42.8: Physical use cases filed — museum, counter, shelf, street.

*Form RND-42 — Plastic Token R&D. Filed. Done. Next.*
