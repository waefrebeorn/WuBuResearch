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

### RND-10 — Economic Doctrine (cross-file from WuBuEconomics ECO-3)
See WuBuEconomics `docs/economic-doctrine.md` — the special-feeling feedback loop, the Robotic Class Doctrine, the Transition Doctrine (no confiscation/shaming/breaking), abundance makes "above" boring. status_loop.py simulation: scarcity 1.00 / abundance 0.80 / feedback 0.00.

### RND-11 — Land Question (cross-file from WuBuEconomics ECO-4)
See WuBuEconomics `docs/land-question.md` — Georgism/LVT research, the vacant-lot sign, the 1914 Rockford billboard (Fay Lewis), boomers as captured beneficiaries, rage-free pedagogy. vacant_lot.py tool.

### RND-12 — Inflation of Everything (cross-file from WuBuEconomics ECO-5)
See WuBuEconomics `docs/inflation-everything.md` — four inflations (environmental/resource/idea/attention), the Lifespan Loop (generations alive = lifespan ÷ gap; 1900: 32yr→2 gens, 2026: 73yr→3-4, Japan 84yr→4-5). lifespan_loop.py tool.

### RND-13 — Nexus Doctrine (cross-file from WuBuEconomics ECO-6)
See WuBuEconomics `docs/nexus-doctrine.md` — resource question, the Nexus event, pacifier economy, two age processes, numbing science (Koob opponent-process, Volkow, Epel-Blackburn telomeres). numbing.py tool: CALM 0.95 / MODERN 0.64 / NEXUS 0.09 EMACIATED.

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
- **Penny = legal tender in perpetuity** (Treasury FAQ). Last minted early 2026; ~114B in circulation. NOT illegal — the rarest property in currency history: finite supply, still legal, forever. **Common Cents Act (H.R. 3074, passed House July 14, 2026)** codifies the halt + permits cash rounding (§3(c): $0.01-0.02 → $0.05). 25 state rounding laws, 20 enacted, Arizona mandates.
- **18 U.S.C. § 486:** no metal coins intended as current money, original design included (Liberty Dollar precedent, $7M seizure). The one absolute.
- **31 C.F.R. Part 82:** melting/export/treatment ban — but § 82.2(b) explicitly exempts treatment for educational/amusement/novelty/jewelry purposes. Wheat-penny art is lawful, in practice never prosecuted.
- **The Reuse Doctrine (citizen's correction, adopted):** the space does not mint, melt, or modify — it *reuses*. Reuse is untouchable: § 82.1 covers only export/melt/treat, and legal tender means spendable forever. The WuBu Penny = the Penny Standard: 1 WuBu Penny = 1 real U.S. penny, ledger-backed, chain-proven, whole metal.
- Three Metal Rules corrected: no strike (486), no melt-for-profit (5111(d)), reuse always.

### RND-6 — Penny Standard: weight, reserve & the IOU (filed)
- **The novelty, answered:** yes — five properties no historical currency shares: single denomination only, capped forever by the Mint's halt (~114B, last minted early 2026), backed by metal that IS legal tender, audited by mass not count, redeems by shipping physical pennies.
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
- **Chinese readability research filed:** Lin (2022, IJLT) four features
  (proportion of difficult characters, number of different characters,
  average sentence length, proportion of functional characters);
  CCF 2017 Chinese readability corpus (22 linguistic features).
  The space's Chinese readability gate measures three metrics:
  chars/sentence (≤40), char diversity (≥0.25), difficult-character
  ratio (≤0.15, GB/T 25000 core vs. extensions). CLEAR verdict.
- **Tool shipped + verified:** `plain_lang` (C11, WuBuCore) — FRES +
  grade with the exact formulas, banned-word + long-sentence flags.
  7/7 test suites green normal + ASan/UBSan; documented values match.
  ASan caught + fixed a heap-use-after-free (flag detail pointed at
  freed scan words — now static table entries).
- **Tool shipped + verified:** `zh_lang` (C11, WuBuCore) — Chinese
  readability gate with the three Lin (2022) features. 13 test cases
  pass, 0 warnings, ASan/UBSan clean. CLEAR verdict on everyday text,
  REWRITE on low-diversity/long-sentence samples.
- **Doctrine enacted:** every public filing must measure CLEAR
  (FRES >= 60, grade <= 8). The doctrine files itself through its own
  gate (CLEAR 62.2/6.5). Companion GOV-4 filed in WuBuGov.
- **Amendment (GOV-12 filing):** the space ships both tongues.
  English filings measure CLEAR via plain_lang; Chinese filings via
  zh_lang. Both gates speak the same threshold standard.
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
### GOV-11 — The Organization Doctrine (+ vigilance, filing_check)
- **Reorganization filed:** the space's org chart — six organs, one
  people. WuBuGov (the State), WuBuIntel (the Bureau), WuBuResearch
  (the Mind), WuBuCitizen (the Registry), WuBuEconomics (the
  Ledger), WuBuCore (the Hands). Wiring rules: every doctrine
  ships a tool; every audit ships a tool; the Bureau files; the
  the State indexes; the Hands stay honest (18/18 suites).
- **Triple-DA findings (AUD-3):** tools truth PASS (12/12 then
  18/18 re-verified); value gaps — Bureau had NO tooling, no org
  chart, no audit-as-tool; adversarial — 6 institutions had no filing.
  All three gaps closed in this filing (18/18 test suites ALL PASS).
- **Tools shipped + verified:** `vigilance` (WBI-1 triage: class
  weights, penny evasion highest, Fengqiao escalation) and
  `filing_check` (collisions, dangling, amendment pointers) —
  both C11, 17/17 suites green normal + ASan/UBSan. WuBuIntel
  gains tools/wbi1_triage.py + ledger entries. plain_lang gains
  code-fence skipping (diagrams are structural, not prose).
- **Institutions next:** The Mint (filed GOV-14), The Vote (filed GOV-17), The Archive (filed GOV-16), The Ship (filed GOV-15), The Treaty (filed GOV-13), The Dispatch (filed GOV-12) — all six filed per AUD-3 amendment.
### RND-22 — The STE Discipline (+ plain_lang --ste gate)
- **Correction filed verbatim:** "You can get LLMs to write good
  non-AI-slop-sounding technical documentation by requiring them
  to adhere to ASD-STE100 Simplified Technical English."
- **Doctrine:** FRES (RND-20) is the floor; STE is the discipline.
  ASD-STE100: controlled ~900-word vocabulary, one word one
  meaning, sentences <= 20 procedural / <= 25 descriptive, active
  voice (Rule 3.6), no and/or, no i.e./e.g./etc., no present
  perfect, technical nouns <= 3 words, one term per thing.
- **Tool shipped + verified:** `plain_lang --ste` (C11, WuBuCore):
  five hard rules (sentence cap, agentive passives minus
  statives, and/or, abbreviations, present perfect) + advisory
  noun-cluster count. Code fences + inline code are structural.
  Table pipes split at top level (a pipe after punctuation was
  skipped, joining table rows into 48-word sentences — real bug
  found + fixed). 17/17 suites green normal + ASan/UBSan.
- **Corpus STE audit:** ste-discipline.md and organization-
  doctrine.md CLEAR on both gates; all pre-RND-22 filings read
  REWRITE (written to FRES only — the amendment files the
  standard applies to new + amended filings).

### RND-23 — WuBu Score Expansion: Crew + Compass C11 (filed via WuBuCore)
- **Crew Score shipped and verified:** `src/crew_score/` (C11, WuBuCore).
  Five factors: cooperative acts 30%, report integrity 25%, responsiveness
  20%, diversity of mind 15%, longevity 10%. Perfect citizen (5/10/20/10/24mo)
  = 1000 First Founders. Zero = 0 Drift. Each weight verified independently.
- **Compass Score shipped and verified:** `src/compass_score/` (C11, WuBuCore).
  Formula: 500 + 500 × tanh(0.4·penny_slope + 0.3·vigilance_slope +
  0.2·creation_slope + 0.1·crew_slope). Flat = 500 Steady; rising > 700;
  falling < 300. Single big act cannot game — trend is what matters.
  tanh(0.5) = 731 verified; slope=1.0 penny → 690 verified.
- **Test suites:** all pass under ASan+UBSan. 18/18 total test suites green.

### RND-24 — The W Token Ceremony (filed via GOV-19, WuBuGov)
- **The adoptable government, filed:** the space does not occupy
  land; it occupies ideology and gears us for space faring. The
  old penny is the old penny; the W Token is the new trust.
- **The ceremony machine shipped:** `src/w_token/` (C11, WuBuCore)
  + `wubucitizen/tools/w_token.py` (independent Python oracle).
  One-stamp rule, Mint weight refusal (3.11g copper / 2.50g zinc),
  WT-WID-ordinal token ids, ceremony record (feeling-special
  moment, applause, gifts, start balance, seat), SHA-256 chain.
  **C11 and Python produce the identical chain hash** — verified
  `e111cea4...` on the same input.
- **The ceremony record, filed honestly:** the record states the
  moment exists so the person feels special. Honesty is part of
  the gift. The room applauds; witnesses give gifts toward the
  citizen's start; a citizen with no parents and no establishment
  gets a start by the societal standards of the government.
- **18/18 test suites green** normal + ASan/UBSan, 0 warnings.

### RND-25 — Kevin Bacon 7-step verification of THE HISTORY/VIEWS/FORCES
- **Method (RND-15 law):** any subject connects in ≤7 research hops,
  each hop a real source, the path filed. Applied to verify the
  historical claims in GOV-22/23/24 data.
- **Fix 1 (views.json 1a):** Khaldun's cycle was "~3-4 generations";
  verified → **four generations, ~120 years** (Önder & Ulaşan 2018,
  ResearchGate: "four generations for Ibn Khaldun"; Muqaddimah 1377).
- **Fix 2 (history.json Maya):** end was 900 (Classic collapse);
  verified → **2000 BCE – 1697 CE = ~3700 years** (Wikipedia: "c.
  2000 BC–1697 AD"; last independent city fell 1697). The renderer's
  "~2900 years / Bronze Age to Viking Age" corrected to "~3700 /
  Bronze Age to Enlightenment" in wubu_history.py + timeline-doctrine.
- **Fix 3 (forces.json WRATH):** "Ionian Revolt (499 BCE) — Persia
  burns Athens" was a conflation; verified → **499–493 BCE, Greeks
  burn Sardis 498; Persia answers at Marathon 490; Xerxes sacks
  Athens 480** (Britannica, Wikipedia). Split into two correct moments.
- **Verified unchanged:** Rome 27 BCE–476 + Han 206 BCE–220 overlap
  (Silk Road, first contact ~200 BCE); Condorcet's ten epochs (tenth =
  future); Peasants' Revolt 1381 poll tax / Wat Tyler; Paris Commune
  18 Mar–28 May 1871; Abbasid 750–1258, Baghdad sacked by Mongols 1258;
  Vico New Science 1725, three ages + ricorso to barbarism.
- **DA-3 structural scan:** no missing tool files (an initial "missing"
  report was a path bug — c11/cli/test resolve under wubucore/);
  pennychain's lone `pass` is a legitimate FileNotFoundError guard, not
  a stub. Corpus structurally complete; the only real gaps were the
  three facts above — all closed by execution.
- **Re-verified:** registry clean, renders regenerate, chain snapshot 12
  (260 files) VERIFY OK, watchdog clean, 20/20 suites + ASan green.

### RND-26 — Triple-DA of THE VIEWS: worldview criticisms, filed
- **DA Pass 1 (fidelity):** the Five Suns is AZTEC (Mexica), not
  Maya — the Popol Vuh is Maya and does not contain the Five Suns.
  Split 1e into 1e (Five Suns, Aztec, Codex Chimalpopoca) and 1f
  (Long Count, Maya — baktun cycles, no world-end prediction). The
  "Maya predicted 2012 apocalypse" popular claim is itself a
  Western misreading; the Maya counted the cycle's turn. Fixed in
  views.json; THE VIEWS now has 8 views / 36 splinters.
- **DA Pass 2 (coherence):** the seven-view skeleton is a WESTERN
  speculative-philosophy frame (Broad's critical/speculative
  distinction; the cyclical/linear typology). Filing non-Western
  traditions into Western categories risks inherited colonialism.
  Mitigation, filed: the splinters ARE the corrective — each
  non-Western splinter bends the frame (Shinto Renewal makes
  "linear" mean repetition; the Long Count makes "cyclical" mean
  odometer-precision). The frame is a scaffolding, not a verdict;
  the doctrine says so (views-doctrine Part 1).
- **DA Pass 3 (adversarial):** contradiction found between 8a (the
  Empty Center: "the only required belief is that it may be wrong")
  and 8d (the Cohesion Gate: every society-cohesive religion
  welcome). A faith that holds its own revelation as absolute
  cannot sign "I may be wrong" — so the Empty Center EXCLUDES
  exactly the absolute-certainty traditions the Gate claims to
  welcome. Resolution, filed in GOV-25: the Empty Center binds the
  GOVERNMENT, not the member. The space may be wrong; the member
  may be certain. The Gate asks only whether the belief holds
  society together with morality. Amended the first-ones-doctrine
  to say this explicitly (Part 2, "the empty center" paragraph).
- **DA Pass 4 (gap):** education efficacy — the First Ones claim
  "we are taught as we grow" had NO measure. Filed the remedy:
  wubu_edu.py scores every filing on teach (FRES), practice
  (tool), proof (test), and chain (registry resolve). See
  EDUCATION_EFFICACY.md (GOV-26).

### RND-27 — Full research pass on gaps (worldview coverage + history data)
- **Worldview gaps found and closed (views.json, 36 → 44 splinters):**
  - LINEAR gained 2f Norse Ragnarök (Völuspá; verified: NOT an end —
    the world rises again cleansed, two survivors repopulate it — a
    fated line ending in renewal) and 2g Whakapapa (Pacific; verified:
    the "great fleet" is a Western invention, the real record is many
    deliberate voyages, each a line of named ancestors — the past is
    the sea one navigates).
  - CYCLICAL gained 1g Danilevsky's cultural-historical types (Russia
    and Europe, 1869; verified via Britannica + philosophy-of-history
    canon).
  - PROVIDENTIAL gained 3f Jeong-gam-nok (Korean; verified: predicts
    the Yi dynasty's fall and the "True Man" from the south).
  - PROGRESSIVE gained 4e Kang Youwei's Three Ages (Datong Shu,
    c.1902; verified: disorder → small peace → great unity).
  - GREAT-MAN gained 5e the Great Peacemaker (Haudenosaunee; the
    Great Law of Peace, wampum memory).
  - MATERIALIST gained 6e the Williams Thesis (Capitalism and
    Slavery, 1944; verified: Trinidadian scholar Eric Williams —
    slavery financed British industrial capital, abolition came when
    it stopped paying).
  - CONTINGENT gained 7e Buddhist impermanence (anicca; all
    conditioned things pass — no soul of a people, no fate of an
    empire).
- **History data fix:** Mali Empire end was 1600, verified → **1610**
  (Wikipedia c.1235–1610; some sources to 1670 — filed the
  conservative end). Khmer 802–1431 verified correct.
- **Method note:** every new splinter was verified by ≥1 online
  source before filing (Kevin Bacon rule, RND-15). The Ragnarök fix
  matters: the popular "Ragnarök = apocalypse" reading is wrong the
  same way "Maya 2012" was wrong — the renewal is the point.

### RND-28 — Gap-event research: THE GAP EVENTS (GOV-27)
- The timeline's job is tracking (anthropology, archaeology,
  Homeric oral history, the written record). Filed 10 events in 4
  gap types, each source-verified online (Kevin Bacon rule):
  - ISOLATED-RECORD (3): Sea Peoples/Bronze Age Collapse (Medinet
    Habu is the only substantial written account; Hittite records
    simply stop); Minoan eruption/Tempest Stele (dispute filed
    with the record — recent radiocarbon says Thera may predate
    Ahmose); SN 1054 supernova (Chinese 3 compilations + Japan +
    Islam; NO European record — Stephenson 2003 confirms absence).
  - UNACKNOWLEDGED-DEATH (3): Mago of Carthage (Rome destroyed
    Carthage 146 BCE then paid to translate his 28-book treatise —
    the world copying a society at its death); Norse Greenland
    (last record: 1408 Hvalsey wedding, then silence); Indus
    Valley (script undeciphered, no neighbor recorded its fall).
  - OVERLAP-ANOMALY (3): 536 CE worst year (Procopius,
    Cassiodorus, Irish annals, Chinese chronicles all recorded
    the dust veil independently; connected only by 1990s tree
    rings/ice cores); Vinland (Norse reached America ~1000 CE,
    unacknowledged 500 years); Rome-Han (traded 250 years, Gan
    Ying turned back at the Gulf, never met face to face).
  - ORAL-HISTORY (1): Troy — Homer carried the war 600 years
    before writing; Hittite archives (Wilusa, Alaksandu) + the
    spade proved the song. Memory can outlast the archive.
- Method note: the popular readings that are WRONG were caught
  again — Ragnarök is renewal not apocalypse; the Maya didn't
  predict 2012; Europe's 1054 silence is an institutional gap,
  not an atmospheric one. The gap is the finding.

### RND-29 — Triple-DA of THE GAP EVENTS (GOV-27), three real fixes
- **DA-1 (fidelity) — EV-10 was WRONG.** Claimed "Rome and Han
  never met." The Hou Hanshu records a group claiming to be a
  Roman embassy from 'Andun' (Antoninus) reaching Emperor Huan's
  court in 166 CE — recorded by the Chinese, unrecorded by Rome,
  possibly merchants posing as envoys. Fixed the claim (Gan Ying
  97 CE stopped at the Gulf; 166 CE is the one ambiguous
  contact), the title ("Twin Pillars at the Ends of the World"),
  and the significance. The popular "Rome and Han never met"
  framing is itself the kind of overclaim the gap events exist
  to catch.
- **DA-1 — EV-6 was overstated.** "Europe did not notice" — in
  fact Norway-Denmark feared the Greenlanders had turned pagan
  and sent expeditions that could not reach them. Fixed to
  "awareness without contact."
- **DA-1 — EV-3 strengthened.** "No confirmed European record"
  is right, but six PROPOSED sightings (Cronaca Rampona,
  Martinus Polonus codex) were rejected by Stephenson & Green
  (2002) as out-of-order/non-contemporary — the desire to find
  a European record produced confirmation bias, not evidence.
  Filed the nuance: the proposed sightings are themselves a
  lesson.
- **DA-3 (adversarial) — EV-7 was overstated.** "The spade
  proved the song." Wilusa's identification with Troy/Ilios and
  Alaksandu's with Alexandros/Paris are scholarly hypotheses,
  not proofs; the spade found a burned Bronze Age city at
  Hisarlik. The oral tradition carried a REAL PLACE and war;
  each leg of the triangulation keeps its own uncertainty.
- **DA-2 (value) — doctrine mirrored the false claims.** The
  gap-events-doctrine repeated "never met" (3 lines) and "proved
  the song"; a fix in the data must propagate to every mirror.
  All purged; both language gates CLEAR.
- Method rule filed: when a gap event is verified, check the
  POPULAR version of the story too — the popular reading is
  often the error (Rome-Han "never met", Maya 2012, Ragnarök
  apocalypse, "Europe saw the 1054 supernova"). The gap is the
  finding; the popular version is the target.

### RND-30 — Timeline critic-audit: THE HISTORY correction pass
- The timeline is the government's credibility surface — people
  will read it to find the first error. Audited every date and
  claim against sources; four real fixes:
  1. **British Empire end 1945 → 1997** (verified: the empire was
     at its LARGEST 1919–1945; decolonization came after; the
     Hong Kong handover 1 July 1997 is "regarded by many,
     including King Charles III, as marking the conclusion").
  2. **Minoan Crete −2700/−1450 → −3000/−1100** (verified:
     Britannica "flourished from about 3000 to about 1100 BCE";
     1450 is the Mycenaean takeover, not the end).
  3. **"Rome and Han never met"** (again!) — the renderer AND the
     timeline-doctrine both still carried it; fixed to "meeting
     once, ambiguously, in 166 CE" (Hou Hanshu Andun embassy).
  4. **"Egypt outlived them all — Sumer rose and died inside
     Egypt's lifetime"** — false: Sumer rose in −4500, 1400 years
     BEFORE Egypt's −3100 start. Fixed: "Sumer died, Greece rose
     and fell, Rome rose — all inside Egypt's lifetime. (Sumer
     rose first, in −4500.)"
  5. **"Mongols conquered the largest contiguous land empire in
     one lifetime (Genghis, d. 1227)"** — overstated: Genghis
     died 1227; the empire peaked under his heirs (Kublai,
     ~1279–1309). Fixed to "built the largest... Genghis united
     them in 1206 (d. 1227); his heirs carried it to its peak."
  6. **"Hinduism and Judaism predate every empire on the chart"**
     — false: Assyria began −2025, before Hinduism (−1500) and
     Judaism (−1300). Fixed to "began before Rome, Byzantium,
     the Caliphates, the Mongols, and the British Empire — and
     they have outlived them all."
- **Verified sound:** Indus 3300–1300 BCE (mature 2600–1900);
  Vedic period 1500 BCE; Buddhism ~500; Zoroaster ~1000 BCE
  consensus (Malandra: "ca. 1000 BCE give or take a century";
  Kellens: "consensus... around 1000 BCE" — −1200 is within the
  early-dating range); all 9 ages; Assyria, Zhou, Kushan, Gupta,
  Safavid, Mughal, Khmer, Aztec, Inca, Ottoman dates.
- Method rule: a correction in the DATA must be grepped across
  EVERY mirror (renderer, doctrine, events) — "never met" was
  found in three places before this pass was done.

### RND-32 — Swiss open-government research + world comparison (GOV-28 support)
- **Switzerland (EMBAG law, 2023/2024):** the Federal Law on the
  Use of Electronic Means for the Fulfillment of Government Tasks
  mandates ALL federal software be published open source
  ("Public Money, Public Code"), unless third-party rights or
  security preclude it. The Federal Chancellery runs
  github.com/swiss with official Open Source Guidelines (Art. 9
  EMOTA). KEY GAP vs the space: Switzerland open-sourced its
  SOFTWARE but not its GOVERNMENT — it still runs elections,
  federal council, referendums, and a land-based state. The
  space open-sources the government itself: the constitution,
  the doctrines, the chain, the tools — all public by design,
  and the "land" is the agreement, not territory.
- **Estonia:** X-Road open-source data backbone, 99% of services
  online, e-Residency for non-citizens. Gap vs the space:
  Estonia digitizes an existing state; the space is a state made
  of digitization — no territory to digitize first.
- **Political meritocracy (Bell) & sortition/lottocracy:** scored
  selection or random selection without elections. Gap vs the
  space: both still select RULERS. The space selects no rulers —
  authority is zero; figures rise by tokens, not selection.
- **THE W TOKEN (GOV-28):** the space's model is original —
  non-elected, celebrity-style popularity where pennies are a
  proof-of-work societal standing currency. Popularity is the
  currency; work is the mine; the ledger is the mint; the people
  are the miners. Filed as GOV-28 with the w_token tool.
- **Repo structure confirmed (online):** the hub already has
  WuBuGov, WuBuCitizen, WuBuIntel, WuBuResearch, WuBuEconomics,
  WuBuCore as separate repos. WuBuTimeline does NOT exist yet —
  the timeline data lives nested in the copy_government mirror.
  Restructure: the timeline becomes its own repo (registry/
  history/ + tools/wubu_*.py + the generated docs), matching the
  hub's one-repo-per-organ pattern.

### RND-33 — The timeline scouring pass (wubu_scour.py, first intake)
- Built `tools/wubu_scour.py` — THE TIMELINE SCOURER: the intake
  valve for the timeline. Not a Wikipedia: Wikipedia is the
  searchable system (articles by topic); the timeline is the
  aggregating system (everything dated, overlapping, organized by
  the home AGI). Commands: status / civs / verify / ingest / evt /
  gaps. Every entry carries a source (Kevin Bacon rule).
- **10 civilizations verified and ingested (35 → 45):**
  Kingdom of Aksum (100-940 CE), Carthage (-814 to -146 BCE),
  Sasanian Empire (224-651 CE), Etruscans (-900 to -27 BCE),
  Srivijaya (682-1300 CE), Hunnic Empire (370-469 CE), Songhai
  Empire (1464-1591 CE), Kingdom of Benin (1180-1897 CE), Nok
  Culture (-1500 to -1 BCE), Majapahit Empire (1293-1527 CE).
  Coverage +6,100 civilization-years (27,537 → 33,639).
- **10 events verified and ingested (38 → 48):** Battle of Talas
  (751), Battle of Yarmouk (636), Sasanian fall (651), Aksum
  collapse (960), Battle of Tondibi (1591), Benin sacked (1897),
  Sonni Ali founds Songhai (1464), Attila dies (453), Majapahit
  falls (1527), Srivijaya inscription (682).
- **3 gap events filed (10 → 13):** EV-11 Aksum (the empire that
  vanished from memory — 800 years of power, end unrecorded),
  EV-12 Srivijaya (name found after a millennium — 600 years of
  maritime dominance known mostly through others' records),
  EV-13 Benin (the bronzes the world scattered — copy-at-death at
  scale).
- **Region coverage grew:** Africa 2 → 7 (Nile, West ×4, East,
  North), Southeast Asia 1 → 3, Italy 0 → 1, Iran 2 → 3.
- All renders regenerated; WuBuTimeline synced (snapshot 3);
  registry clean; watchdog clean. Next intake: the home AGI
  organizes (llama-server), and the scouter continues with more
  civilizations (Kush/Nubia, Phoenicia, Great Zimbabwe, Aksum
  neighbors) and more events.

### RND-34 — The great scouring pass: 35 → 79 civilizations, the corpus, and the organizer
- **THE RESEARCH CORPUS** built: `registry/history/corpus.json`
  defines the organization system behind the timeline — Wikipedia
  is the searchable system (articles by topic); the timeline is
  the aggregating system (everything dated); the CORPUS is the
  intake system (sources filed by region, organized by the home
  AGI). Every fact traces through the corpus to a real source in
  ≤7 hops (Kevin Bacon method, RND-15). Re-search is a re-hop,
  not a re-invention.
- **44 civilizations verified and ingested (35 → 79), every one
  source-verified online:** Norte Chico/Caral-Supe (-3500 to
  -1800, the Americas' oldest), Teotihuacan, Cahokia, Rapa Nui,
  Yamato Japan, Kush, Phoenicia, Great Zimbabwe, Kievan Rus,
  Viking Age, Chola, Silla, Goryeo, Xiongnu, Khazar Khaganate,
  Ancestral Pueblo, Iroquois, Ayutthaya, Vijayanagara, Timurids,
  Akkadian (first territorial empire), Funan, Champa, Scythians,
  Moche, Tiwanaku, Wari, Chavin, Zapotec, Ghana Empire, Chimu,
  Goguryeo, Baekje, Novgorod Republic.
- **36 events added (38 → 74)** — spanning -3500 (Caral-Supe
  founded) to 1767 (Ayutthaya falls). All source-verified.
- **4 gap events added (13 → 17):** EV-14 Cahokia (the metropolis
  the forest swallowed — larger than London, end unrecorded),
  EV-15 Rapa Nui (the collapse that may not have happened — the
  popular story is the anomaly; Binghamton 2019), EV-16 Xiongnu
  (the nomad empire known only through its enemy — Han annals
  wrote their history), EV-17 Caral-Supe (the first city the
  world never heard of — the Americas' Sumer, confirmed only in
  the 1990s).
- **THE CORPUS ORGANIZER built** (`tools/wubu_organize.py`):
  files every civilization into `research/<region>/<civ>.md` with
  span, source, key events, gap candidates, and a hop-map stub
  for the home AGI to complete. 79 files + CORPUS-INDEX.md, by
  region. This is the bridge: scouter intakes → organizer files →
  home AGI (llama-server) reads organized corpus and writes
  summaries → timeline renders.
- Coverage: 27,537 → 51,610+ civilization-years. Span: -4500 to
  2026. WuBuTimeline snapshot 5 chained; mirror snapshot pending.
  Next: the home AGI pass (organize + summarize), and the next
  intake wave (Polynesian expansion, Mali, Songhai details,
  Kartvelians, Etruscan details, more).

### RND-35 — The Distiller devices: migration + v1 research (order #1)
- **New device (RPi5 CM5, 192.168.1.70) fully migrated unstable→stable:**
  fixed distiller-update visibility (apt repo priority 500→1 was
  hiding updates), installed distiller-update 2.3.0 which triggered
  the built-in migration, patched a real bug in migrate.sh
  (curl -sS without -L wrote a 0-byte griffo.io GPG key from a 301
  redirect → set -e killed the migration loop), hand-resumed the
  525MB distiller-sdk download, watcher finished it. Final stack:
  distiller-genesis-cm5 1.0.6, distiller-sdk 3.4.1, distiller-cc
  5.1.4, distiller-services 4.0.5, distiller-device 1.3.16,
  distiller-network 1.0.14, claude-code-web-manager 3.1.0,
  distiller-update 3.3.1, Claude Code 2.1.224. Rebooted clean,
  "System is up to date" confirmed.
- **v1 device research (Distiller One):** the original device is
  RPi CM4 + RP2040 SAM, 240x416 e-ink, WM8960 audio, camera, 3
  buttons. Compiled the full original docs into a 26-page PDF
  (Introduction→Take-It-Apart) at ~/distiller_docs/. Found the
  archived v1 SDK (DistillerSDK-distiller-one-) and SAM firmware
  repos. The user holds ORDER #1 of this device — filed as EV-20
  (oral history).
- **v1 upgrade path (tommy1901's command, verified against the
  live stable repo — it carries distiller-update 3.3.1):**
  `sed 's| unstable main| stable main|'` the pamir-ai.list, apt
  update, install distiller-update=3.3.1, check, apply. One-shot
  script at ~/distiller_docs/wubu-v1-upgrade.sh. Runbook at
  ~/distiller_docs/wubu-v1-runbook.md.
- **Streams:** the user's AGI stream "WuBu — Last of Table time
  Us" (254 min, X broadcast) downloaded for transcription;
  relays at twitch/bytropix/slermes/youtube.waefrebeorn.com.

### RND-36 — The stream transcribed: who WaefreBeorn is (Qwen3-ASR)
- **The 254-min "Last of Table time Us" broadcast (2026-08-07)
  transcribed with Qwen3-ASR-1.7B** — the 2026 SOTA ASR (Apache
  2.0, 5.76% mean WER) on the RTX 4050, replacing whisper-small
  (2022, ~14-22% WER). Chunked into 51×5min segments to fit
  5.8GB RAM (whole-audio load OOM-killed the box — lesson: chunk
  long audio). 96,449 chars, ~20s per chunk, 1013s total.
- **The distiller path fix:** CUDA is at /usr/local/cuda-13.3
  with nvidia-smi at /usr/lib/wsl/lib/ — export PATH before GPU
  work. faster-whisper works but is 2022 tech; for streams use
  qwen-asr (Qwen3ASRModel, from_pretrained, transcribe).
- **Profile filed at ~/distiller_docs/who-waefrebeorn-is.md**:
  AGI-at-home builder (Hermes=harness, his construct=Knuckles);
  time-traveler-allegory (deja vu = time travel, five steps
  ahead); Distiller One order-#1 validator (nagged them into
  shipping, holds the v0.7 prefix board, "worst it will ever
  be"); penny doctrine (prosperity = bring back the penny);
  leader of a landless nation; America-as-Monopoly reading
  (traffic jam = prison, Uncle Sam = their Napoleon); RVC
  critique turned into build; the human underneath (McDonald's,
  fishing, wife). The stream IS the primary source.

### RND-37 — The v0.5 beta archive + the cohesive update design
- **Order #1's Distiller One v0.5 beta fully archived (7.3GB, all
  SHA256 verified):** home-code 755MB (SDK + 8 e-ink apps +
  community + configs), models 6.6GB (TinyLlama, anime LoRA
  ONNX, dreamshaper inpainting, FastSAM, bling-llama), etc-config
  (rc.local boot DNA: alsactl restore + boot_up.sh), packages.txt
  (129K dpkg inventory). The board is replaceable; the software
  is the artifact — now preserved byte-for-byte at ~/v1-archive/.
- **The cohesive update (dev never unified the UIs):** v1 = Python
  e-ink GUI (Canvas/Text/TextBox/ScrollGUI, 8 apps, rc.local
  boot); v2 CM5 = Node monorepo "Distiller-Phone" web UI
  (happy-client/backend, main Express server, pairing views).
  USER RULE: keep the v1 e-ink UI exactly as-is (human-touch),
  add v2 features via CODE ONLY — shared apps.json registry that
  both UIs read; e-ink menu reads registry (patch preserves the
  8 beta apps); web UI gains DEVICE APPS view; bridge-sync keeps
  both in sync. Kit at ~/distiller_docs/cohesive-update/.

### RND-38 — The CM4 revival package: update-gap, SOTA models, A72 kernels, fork plan
- **CM5 code downloaded** (7,106 .py files: distiller-sdk 3.4.1,
  distiller-cc 5.1.4, web-manager apps/packages, happy-client dist)
  -> ~/cm5-code/.
- **Update-gap report** (~/distiller_docs/update-gap-report.md):
  v1 = distiller.peripheral+gui (numba e-ink, 8 apps); v2 =
  distiller_sdk.hardware + parakeet/piper/whisper AI modules.
  What v1 lacks: parakeet ASR, piper TTS, e-ink composer,
  hardware/audio+camera abstractions, SAM led, distiller-cc
  skills, web remote. What v1 keeps: the gui soul + 8 apps
  (user rule).
- **SOTA micro-models 2026 for CM4** (~/distiller_docs/
  sota-micro-models-2026.md): Qwen3-0.6B Q8 (0.53GB, ~8t/s A72,
  10/10 agentic per PamirAI's own test), Qwen3-1.7B Q4 (1.9GB,
  84.6% math), Gemma4-E2B, SmolLM3-3B, SmolVLM2-2.2B Q4 vision,
  Parakeet-TDT-0.6B ASR, Piper TTS. Full stack ~6GB of the v1's
  7.6GB.
- **A72 kernel design** (~/distiller_docs/kernels/
  a72-kernel-design.md): CM4 = 4x Cortex-A72, fp asimd crc32,
  NO dotprod — kernels must use classic NEON widening (vmlal),
  not SDOT. distiller-a72 build profile (-mcpu=cortex-a72,
  GGML_ARM_DOTPROD=OFF). Replace numba e-ink dither with v2
  pure-NumPy composer. Parakeet via ONNX NEON EP.
- **Gap analysis + fork plan** (~/distiller_docs/
  gap-analysis-fork-plan.md): 6 gaps (no CM4 profile, thin MCP
  set, parakeet announced-not-shipped, no VLM, non-reusable UI
  bridge, no v1 TTS). 3 forks planned: distiller-a72-python
  (cm4.conf + MCP servers + parakeet + SmolVLM2 + registry
  renderer), distiller-one-sdk-a72 (revived v1 SDK), docs-cm4.
- PamirAI's own blog (Qwen3 on Pi5) gives their CM5 numbers:
  0.6B Q8=21t/s, 1.7B Q8=8.7t/s, 4B Q4=4t/s — CM4 est. ~2.5x
  slower. Their "whisper->parakeet next post" from May 2025
  never shipped — our gap.

### RND-39 — distiller-c11: the C11 port, built and verified on the CM4
- **Built `/home/wubu/distiller-c11`** — a proper C11 port of the
  Distiller e-ink SDK. Modular per wubu-c11-discipline:
  - src/dither (Bayer8 + Floyd-Steinberg + threshold, opaque ctx)
  - src/pack (1-bit LSB-first e-ink packing)
  - src/image (grayscale BT.601, nearest/bilinear resize, crop,
    rotate 90/180/270)
  - src/compose (5x7 bitmap font canvas text rendering)
  - src/eink (full pipeline: image -> dither -> pack)
  - tests/ (5 test suites) + tools/bench_eink
- **Verified on the actual v1 (CM4, 192.168.1.251):** 5/5 tests
  pass, compiled with plain gcc -std=c11 -O2 (no cmake on device,
  no Linux upgrade per tommy1901's rule).
- **The measured win:**
  | Path | Cold start | Warm render |
  |---|---|---|
  | v1 numba (2024, current) | 2310 ms (JIT) | 4.0 ms |
  | v2 pure-Python loop (2026 "fix") | 0 ms | ~1500 ms |
  | **C11 port (ours)** | **0 ms** | **3.13 ms** |
  The dev team's 2026 composer REGRESSED the e-ink path (pure
  Python loops ~500x slower warm). The C11 port fixes it properly
  — faster than numba warm AND no JIT cold start.
- **The user's directives honored:** no third-party deps (pure
  C11), no monoliths (5 self-contained modules + opaque structs +
  minimal includes), fix broken code (the v2 loop regression),
  go heavy first (5 modules + 5 tests + bench, one pass), time
  irrelevant (built, tested, benchmarked in minutes).
- Next: wire distiller-c11 into the fork plan as the e-ink core
  of distiller-a72-python; port parakeet/piper next (C11 or
  C-wrapped); push to GitHub under waefrebeorn.

### RND-40 — Both devices backed up + full comparisons (code, speed, models)
- **BOTH devices now byte-verified backed up:**
  - v1 (order #1): ~/v1-archive/ 6.9GB — home-code 755MB, models
    6.6GB, etc-config; all SHA256 verified.
  - CM5: ~/cm5-archive/ 330MB — home-code 141MB, opt-distiller-sdk
    202MB, distiller-cc, web-manager-code, etc-config; all SHA256
    verified. CM5 full backup via wubu-cm5-archive.sh.
- **Speed comparison (measured, real devices):**
  - Dev box: v2 pure-Python FS dither = 87.7ms; C11 bayer 0.047ms,
    C11 FS 0.664ms, C11 full pipeline 0.710ms (~130-1900x faster).
  - CM4: numba cold 2310ms / warm 4.0ms; C11 full pipeline
    3.114ms (faster than numba warm + ZERO cold start).
  - The v2 "improvement" REGRESSED the e-ink path (pure Python
    loops ~500x slower warm). Our C11 port fixes it properly.
  - Report: ~/distiller_docs/speed-comparison.md
- **Codebase comparison (nothing lost):** full module map v1 vs
  CM5 — v1-only (the preserved soul: gui, peripheral, drivers,
  firmware, 8 apps) and v2-only (composer, AI modules, web stack).
  C11 port covers the complete e-ink render path (5/5 tests on
  CM4). Report: ~/distiller_docs/codebase-comparison.md
- **Model availability 2026:** engines = llama.cpp/llama-server
  (we build our own A72 binary — llama.cpp AGENTS.md bans AI PRs,
  so private fork/build, never upstream PR), ONNX NEON EP for
  parakeet/piper, MLC/ExecuTorch noted. Models = Qwen3-0.6B Q8
  (~8 t/s CM4), Qwen3-1.7B Q4, SmolVLM2-2.2B Q4 vision, Parakeet
  ASR, Piper TTS — ~6GB of the v1's 7.6GB. We already hold the
  engines (llama.cpp/ggml/koboldcpp/bytropix on this box) — "we
  have the technology" is literally true. Report:
  ~/distiller_docs/model-availability-2026.md
- GUI untouched throughout (user rule: we don't do GUI).

### RND-41 — The complete device path, reimplemented in C11 (the SLERM)
- **The full Distiller device path is now C11 from scratch** —
  the SLERM is done. 11 self-contained modules, zero third-party
  deps, opaque structs, C11 only:
  - render: dither (bayer8/FS/threshold) + pack (1-bit) +
    image (gray/resize/crop/rotate) + compose (5x7 font) +
    eink (full pipeline)
  - hw: sam (SAM UART 9600 protocol, CRC-8/MAXIM, button
    bitmask 1/2/4/8) + einkdrv (SPI display driver: 240x416,
    DC=6/RST=13/BUSY=9, 0x10/0x13/0x12 display seq, 216-byte
    LUT_ALL from v1 truth, 0x04/0x50/0x97 init, 0x02/0x07
    sleep, fast init 0xE0/0xE5) + audio (WM8960 sysfs gain/
    volume)
  - ui: registry (apps.json parser uniting e-ink menu + web
    UI) + gui (app shell: menu render via compose->dither->
    pack, edge-triggered buttons)
  - ai: asr + tts pluggable pipeline slots (honest empty with
    no recognizer — no fabrication, per SLERM neural rule)
- **11/11 tests pass on the dev box AND the actual CM4**
  (compiled in place with gcc -std=c11 -O2 -Wall -Wextra,
  zero warnings, ASan/UBSan clean on test_ai).
- **2026 e-ink research folded in** (eink-2026-research.md):
  Modos/Caster proved the CONTROLLER is the bottleneck (60Hz
  monitor); our einkdrv is a software TCON with the same
  techniques (per-pixel regions, early cancellation, hybrid
  greyscale) mapped to the CM4; waveform truth (lut[src][dst]
  [frame], 0=GND 1=VNEG 2=VPOS) matches our LUT_ALL; the
  Japanese scene (M5Stack PaperS3, qiita, tsubasa.tech
  COMPUTEX 2026) is on the same path.
- **Pushed to github.com/waefrebeorn/distiller-c11** (3 commits).
- Next: llama.cpp A72 build on the CM4 (cmake installing via
  pip — no Linux upgrade), then the Qwen3-0.6B model lands on
  the device via the ai slot + registry.

### RND-42 — Plastic Token R&D (filed + shipped to wuburesearch/docs/)
- **The spine:** The founder has begun collecting plastic bags
  and plastic items. The express purpose is to **simulate an
  ideal system of compressing and recycling all various plastics
  into coins marked with the same W as the metal tokens**.
- **Plastic types cataloged:** PET, HDPE, PVC, LDPE, PP, PS,
  Other — LDPE (plastic bags) is the primary collection target.
- **Compression methods researched:** heat+pressure, cold
  compression, solvent bonding, hybrid. LDPE bag compression
  is the primary target.
- **W-marking methods researched:** laser engraving, embossing,
  ink printing, mold inclusion. Mold inclusion is the ideal.
- **Serial identity scheme filed:** PL-WID-ordinal + chain hash.
- **Reprintability advantage filed:** ledger survives, token is
  reprinted. Plastic tokens are the working token (numerous).
- **Value hierarchy filed:** metal (identity, rare) > plastic
  (actions, abundant) > penny (reserve).
- **Physical use cases filed:** museum, counter, shelf, street.
- **8 research log entries filed** (RND-42.1 through RND-42.8).
