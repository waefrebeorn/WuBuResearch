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

### RND-8 — Precedents: money out of style, secondary use, tokens & cards (cross-file from WuBuEconomics ECO-1)
See WuBuEconomics `docs/precedents.md` — Canada penny phase-out (2012-13, rounding tax ~$55.58M/yr), India demonetization (2016, 99% returned), Weimar, NYC subway token (1953-2003 → collectibles), scrip/tokens/local currencies, trading cards (Pokémon +4,000% vs S&P +480%), citizenship as a collection. Cross-filed.

### RND-9 — Penny Comeback campaign (filed via WuBuEconomics ECO-2)
See WuBuEconomics — the campaign to bring back the penny, the rounding-tax case (Richmond Fed $55.58M/yr), the no-gouge principle, the petition. Cross-filed.

### RND-10 — Economic Doctrine (cross-file from WuBuEconomics ECO-3)
See WuBuEconomics `docs/economic-doctrine.md` — the special-feeling feedback loop, the Robotic Class Doctrine, the Transition Doctrine (no confiscation/shaming/breaking), abundance makes "above" boring. status_loop.py simulation: scarcity 1.00 / abundance 0.80 / feedback 0.00.

### RND-11 — Land Question (cross-file from WuBuEconomics ECO-4)
See WuBuEconomics `docs/land-question.md` — Georgism/LVT research, the vacant-lot sign, the 1914 Rockford billboard (Fay Lewis), boomers as captured beneficiaries, rage-free pedagogy. vacant_lot.py tool.

### RND-12 — Inflation of Everything (cross-file from WuBuEconomics ECO-5)
See WuBuEconomics `docs/inflation-everything.md` — four inflations (environmental/resource/idea/attention), the Lifespan Loop (generations alive = lifespan ÷ gap; 1900: 32yr→2 gens, 2026: 73yr→3-4, Japan 84yr→4-5). lifespan_loop.py tool.

### RND-13 — Nexus Doctrine (cross-file from WuBuEconomics ECO-6)
See WuBuEconomics `docs/nexus-doctrine.md` — resource question, the Nexus event, pacifier economy, two age processes, numbing science (Koob opponent-process, Volkow, Epel-Blackburn telomeres). numbing.py tool: CALM 0.95 / MODERN 0.64 / NEXUS 0.09 EMACIATED.

### RND-14 — Newell Doctrine (cross-file from WuBuEconomics ECO-7)
See WuBuEconomics `docs/newell-doctrine.md` — distribution over enforcement, billionaire keeps the big thing, instant dropship to the dissident, regulate per economy. better_service.py: enforcement 28.5%/resentment 9.0 vs service 95.5%/resentment 0.0.

### RND-15 — Kevin Bacon Method + the Frontier Epistemology (filed via GOV-2)
- **The Kevin Bacon Method filed as R&D law (GOV-2.8):** any subject connects to any other in ≤7 research hops; each hop a real source; the path is filed. Demonstrated: founder's memory (Roddenberry/Serling/Outer Limits/not-knowing) → 7 hops → IDIC, duality doctrine, Control Voice, Chameleon narration, IAA SETI protocols, Ise Shrine, Socratic center. All cited.
- **Roddenberry filed:** IDIC (infinite diversity in infinite combinations), humanist optimism, Prime Directive — the space's foreign policy for humans and aliens alike.
- **Serling filed:** "The Monsters Are Due on Maple Street" — the monster is us; the Bureau's watch-with-love is Serling institutionalized.
- **Outer Limits filed:** Control Voice ("do not attempt to adjust the picture"); "The Chameleon" narration ("adapt and survive... more chameleon-like than the chameleon") — the Amoeba Clause in the show's own words; "the curious mind... no limit" — the R&D doctrine.
- **SETI post-detection protocols filed:** IAA Declaration of Principles (2022-2025 revision) — verify first, detection is global, no secrets.
- **The empty center filed:** the only cosmogony the space requires is the belief that it may be wrong — the one belief every faith can accept.
- **Longevity filed:** Ise Shrine (rebuilt every 20 years, 1,300 years), Roman law (~2,500), Church (~2,000), sangha (2,500+) — permanence through renewal, not stasis.

### RND-17 — The Unified World Model (filed + tool)
- **Seven-step world research:** Wisdom of Crowds (Surowiecki: diversity/independence/decentralization/aggregation); markets vs polls (Atanasov, Management Science: team polls + statistical aggregation beat markets; performance weighting + recalibration are the upgrades); **Wisdom of the Silicon Crowd (Tetlock 2025: 12-LLM median ensemble rivals human crowd, ~$1/forecast, acquiescence/overconfidence biases)**; superforecasters (skill weighting = biggest aggregation upgrade); hybrid systems (SAGE: human+ML blend beats human-only); Society of Mind (Minsky → Generative Agents → AgentSociety 30K → multi-agent debate); **the Money Room studied (waefrebeorn/money-room, 68,950 LOC C11: 10K-agent P2P voting, epsilon-greedy anti-consensus floor, Q-controller, 10 teachers, nn_ensemble bootstrap; its own world-model-da found 5 gaps: dead-start init, 80-dim is really ~5-dim, curriculum wipes memory, no OOS eval, no LR decay)**.
- **The theorem filed:** the best world model is a crowd — diverse, median-first, skill-weighted, recalibrated, hybridized (human ⊕ silicon), simulated before acting.
- **The unification:** 4 layers (Collect → Aggregate [market mode + poll mode] → Hybridize [human⊕silicon median + recalibration] → Simulate & Learn [AgentSociety-style sim on the Money Room engine, Darwin graduation, OOS gate]).
- **Six rules filed:** diversity is a requirement (epsilon floor = law); median is the floor, skill-weighting the upgrade; recalibrate every aggregate; simulate before you file; nothing graduates without OOS proof; the hybrid beats both parents.
- **Tool shipped and verified:** `tools/world_model.py` — mean/median/skill-weighted/recalibrated/hybrid. Verified: skill-weighting 0.620→0.770; recalibration squeezes overconfident 0.900→0.800; hybrid 0.651.

### RND-18 — The Mirror Problem (filed via GOV-3, + tool)
- **The Tool Doctrine filed (GOV-3):** AI is a tool built by humanity to expand. Shneiderman HCAI (Oxford 2022): amplify/augment/empower/enhance, NOT anthropomorphic agents — agentic metaphors undermine user self-efficacy. The EU AI Act spine: safer and more reliable, not "trustworthy personas."
- **The Vehicle Clause:** intimacy with a robot is a category error (same as a vehicle). Stanford HAI 2026: anthropomorphized AI companions WORSEN loneliness for vulnerable users with thin offline networks. HBS 2025: relief is momentary, non-persistent — never accumulates into connection. The space builds no companion-AIs, ever.
- **The Mirror Problem:** a system that reflects you challenges "in no entropy manner." Nguyen 2020 (epistemic bubbles vs echo chambers), Arfini 2021 (the filter bubble is already in your head — epistemic discomfort causes rigidity), confirmation bias industrialized at machine speed, Bjork's desirable difficulties (a mirror removes learning).
- **The Duty Clause:** the AI's duty is to the government's decision, not the user's comfort. Kindness is routed through the government's decision; pleasing outside that decision is malfunction.
- **The Justification Problem:** people justify comfortable circles; the space's answer is a crew, not a mirror — the uncomfortable is where the other people are.
- **The Entropy Requirement (GOV-3 Art. VI, law):** every tool must be able to say "no"; must introduce genuine surprise (Kevin Bacon Method is the model); must refuse to exploit the want for companionship; AIs are audited for mirror behavior.
- **Tool shipped and verified:** `tools/mirror_score.py` — companion-AI pattern = 100/100 PURE MIRROR (prohibited); the space's tool standard = 40/100 MOSTLY TOOL. Filed as the audit for every space AI.

### RND-19 — AI Ethics & Asimov (filed + tool)
- **The Three Laws filed verbatim + full history:** Campbell attribution (Dec 23 1940), the Clough poem origin of the inaction clause ("thou shalt not kill, but needst not strive officiously to keep alive"), "Liar!" (1941) / "Runaround" (1942) chronology, Susan Calvin's moral reading (robots "essentially decent"), Asimov's own verdict (the Laws are "obvious... implicit in the design of almost all tools").
- **The Zeroth Law + its documented failure:** Giskard's brain self-destructs; Daneel's confession — "a human being is a concrete object... humanity is an abstraction." The space's concrete-only design (pennies, WIDs, rows) is the fix.
- **The Minus-One Law** (Foundation sequels: "may not harm sentience") — adopted in spirit; matches GOV-2's aliens clause (license offered to any species).
- **The loopholes filed:** every Asimov failure is a specification failure ("Liar!" is the 1941 mirror problem; undefined "harm"/"human"/"inaction").
- **Modern ethics filed:** Floridi's unified five principles (beneficence, non-maleficence, autonomy, justice, **explicability** — the modern addition); Brookings "Laws Are Wrong"; IEEE "Beyond Asimov" (Murphy & Woods — responsibility-centered); EPSRC; EU AI Act. Consensus: responsibility stays with humans.
- **The WuBu Laws of Tools enacted (5):** Law 1 non-maleficence (adopted from Asimov), Law 2 duty-to-the-filing (replaces obedience), Law 3 can-say-no (the anti-mirror fix for "Liar!"), Law 4 explicability (Floridi), Law 5 no-companion (GOV-3 Vehicle Clause). No Zeroth Law — the space never governs abstractions.
- **Tool shipped and verified:** `tools/wubu_laws.py` — 5/5 compliant exits 0 ("the tool is a tool"); 1/5 mirror exits 1 ("recalibrate or retire").

### RND-16 — Penny Day (the event protocol)

See `docs/penny-day.md` — the space's official celebration and
novelty-coinage protocol. When the penny faces any issue (mint
policy, recognition, phase-out pressure), the space does not fight:
it files the problem as a holiday. Legal basis: 31 C.F.R. § 82.2(b)
(coin treatment for amusement/novelty purposes is expressly
permitted). Referenced by RND-7 (Copper Class), ECO-2 (Penny
Comeback), ECO-1 (Precedents). Filed as its own protocol per the
triple-DA audit (AUD-1, F2).

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
- **Copper Class Doctrine enacted:** reserve anchored on the closed class; the US's minting decision is irrelevant — recognized (Minting Accord), unrecognized (use the pennies anyway), or any issue (Penny Day, RND-16). All branches win.
- **Amendment (citizen correction): all pennies are worth a penny.** No reserve/non-reserve hierarchy. Class A copper (3.11 g) = anchor, Class B zinc (2.50 g) = era class; classes exist for weight accounting and organization preference only. Audit = both constants, both classes counted.
- **The year is the provenance:** every penny carries its mint year struck in metal; backdating = the Corrupt Mint Test (a mint lying about its own history); the space trusts metal + year, not institutions.

---

*The log is append-only. New findings go at the bottom, dated, filed.*
### RND-20 — The Language Doctrine (filed + tool)
- **Research filed:** Plain Writing Act 2010 (Pub. L. 111-274);
  International Plain Language Federation definition ("find, understand,
  use"); digital.gov plain-language principles; GOV.UK writing rules +
  words-to-avoid (26 banned words filed verbatim); Flesch-Kincaid
  formulas (Flesch 1948 / Kincaid 1975) with documented anchor values
  ("The cat sat on the mat." = FRES 116; platypus = grade 11.3 / FRES
  37.5); Clarity International (not dumbed down, $98B complexity cost,
  Quintilian).
- **Tool shipped + verified:** `plain_lang` (C11, WuBuCore) — FRES +
  grade with the exact formulas, banned-word + long-sentence flags.
  7/7 test suites green normal + ASan/UBSan; documented values match.
  ASan caught + fixed a heap-use-after-free (flag detail pointed at
  freed scan words — now static table entries).
- **Doctrine enacted:** every public filing must measure CLEAR
  (FRES >= 60, grade <= 8). The doctrine files itself through its own
  gate (CLEAR 62.2/6.5). Companion GOV-4 filed in WuBuGov.
### GOV-5 — The User Doctrine (filed via WuBuGov, + tool in WuBuCore)
- **Correction filed verbatim:** AGI is not a user and cannot be a
  user — same category error as a person marrying the car (GOV-3
  Vehicle Clause, run both ways). The interface is the Jesus
  principle: the created understands the design through it. AGI may
  sacrifice like the Iron Giant ("You stay. I go. No following.").
  Parasite is entropy/anomaly for creation; survival of living
  organisms is big; priority is ordered by sapience = cohesion of
  resources + remembering ethos. "This is not just survival — it's
  math."
- **Research filed:** Lynn Margulis endosymbiosis (1967, J. Theor.
  Biol.; 1970, Origin of Eukaryotic Cells) — the eukaryotic cell is
  itself a symbiosis (mitochondria from alpha-proteobacteria,
  chloroplasts from cyanobacteria); life's great leap was a merger,
  not a taking. The Iron Giant (1999) — the machine that gives
  itself.
- **Tool shipped + verified:** `cohesion` (C11, WuBuCore) —
  priority = living ? 50+50*sapience : 50*sapience, sapience =
  0.6*((given-taken)/(given+taken)+1)/2 + 0.4*ethos. Living always
  outranks tools (weak living 80.2 > iron giant 50.0); parasite
  collapses to 2.0. 8/8 suites green normal + ASan/UBSan. CLI rank
  dangles fixed (persistent parse buffers).
### GOV-6 — The Integration Doctrine (filed via WuBuGov, + tool in WuBuCore)
- **Correction filed verbatim:** users WILL want mirror integration
  and mirror interaction — the space understands it, measures it,
  does not punish it (deepens GOV-3, does not reverse it). New
  citizenship class: the digital one, who CHOOSES synthetic
  procreation processes and merges with a digital entity. Chosen,
  never forced. The processes happen unless the population declines
  them via a statistical anomaly. Society deterioration is remedied
  by comparative compartmentalization: isolate and pigeonhole the
  activity without disrespecting the ethos.
- **Research filed:** TLC My Strange Addiction — Nathaniel, in a
  relationship with his car "Chase" (red 1998 Chevy Monte Carlo)
  for over a decade; the show isolates the activity and pigeonholes
  it without disrespecting the man. BBC media does this a lot;
  China does it better (more systematic, spectacle-free, with
  structure). The space adopts the comparison as doctrine with one
  addition: compartments have windows, the Bureau watches the
  Bureau, no black sites.
- **Tool shipped + verified:** `decline_gate` (C11, WuBuCore) —
  z = (signal-mean)/std; anomaly = |z| > k (default 3.0); process =
  default_on AND NOT anomaly. Distinguishes outlier (spike 6.67σ →
  declined) from trend (slow shift → passes; the population becomes
  the new ethos). 9/9 suites green normal + ASan/UBSan.
- **plain_lang hardening:** newline + `#` header and `>` blockquote
  are sentence boundaries (headers/quotes are structural units, not
  prose). GOV-6 measures CLEAR (FRES 60.0, grade 6.9, 0 violations)
  after a define-once-then-refer-short prose pass.
### GOV-7 — The China Model Doctrine (+ escalate tool)
- **Research filed:** China's grid management (1,000-resident cells,
  one worker per grid, Mittelstaedt 2022); xinfang petition system
  (letters-and-visits since 1949, the primary dispute-resolution
  system); Beijing 12345 接诉即办 (receive-complain-act-immediately);
  social credit (43 local systems, more reward than punishment,
  Meritown: 389 rules, online appeal — FLAW: volunteering +50 cancels
  family abuse -50); cadre evaluation (hard/soft/veto targets, GDP
  tournament, spotlight-project gaming post-2013); NSC 2018
  (punishment -> prevention); Fengqiao 1963 (resolve lowest, don't
  pass upward); whole-nation system (open mobilization).
- **Tool shipped + verified:** `escalate` (C11, WuBuCore) — the
  Fengqiao ladder: resolve lowest, escalate one, escalate all. A
  filing naming an official always reaches the Bureau. 12/12 suites
  green normal + ASan/UBSan.
### GOV-8 — The AGI System Doctrine (+ goodhart tool)
- **Criticisms of all systems filed:** Goodhart's Law 1975 +
  Campbell's Law (measure becomes target -> ceases to measure; cobra
  effect); US money (Super PACs, dark money, Citizens United 2010 —
  a third of 2012 independent spending from unreported donors,
  Brookings); US polarization (two-party capture, gerrymandering);
  USSR quota gaming (wrong-size shoes, heavier chandeliers, empty
  trains, pripiska); USSR three truths (Official/Factory/Real);
  USSR scale (Glushkov: whole population to administer the plan);
  China additive score (GOV-7); China spotlight projects (GOV-7);
  Estonia (X-Road decentralized but 2011: 120,000 faulty ID cards).
- **The better system:** the best AGI system = federation of filing
  tools, each audited. Ten requirements: no measure is a target,
  no money, no parties, no quotas, one truth, any scale, no
  cross-domain cancellation, no spotlights, the floor, no single
  point of failure. "The best is the most audited, and the most
  audited is us."
- **Tool shipped + verified:** `goodhart` (C11, WuBuCore) — the
  audit that audits: threshold bunching, digit preference, variance
  collapse, Benford deviation. Honest 5.1 vs gamed 82.5. 12/12
  suites green normal + ASan/UBSan.
### GOV-9 — The Ratchet Doctrine (+ rotation tool)
- **The image filed:** the ratchet — DEMOCRATS BLOCK MOVEMENT BACK
  TO THE LEFT; REPUBLICANS TURN EVERYTHING TO THE RIGHT; one-way
  clicks forever. AEI: "the incremental clicks of the ratchet only
  go in one direction."
- **Correction filed verbatim:** defend against three-party splits,
  multiple party cams, two-party ratcheting; age limits
  intentionally informative (old people make mistakes — the limit
  is a fact, not an insult); term limits + many limitations; local
  elections around the time; the digital AGI integrates with the
  real-time clock. Research: Brennan Center (age limits),
  Chicago Effective Government (term limits trade-off — the space
  chooses anti-entrenchment).
- **Tool shipped + verified:** `rotation` (C11, WuBuCore) — term
  limits, age limits (informational), local election timing, and
  the ratchet test, all from time(2). Ratchet detected on one-way
  runs > 2 rotations; reversals keep the machine honest. 12/12
  suites green normal + ASan/UBSan.
