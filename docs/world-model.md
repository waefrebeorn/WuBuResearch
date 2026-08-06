# The Unified World Model — Aggregating Information & Simulations

**R&D filing RND-17. Seven-step research on how the entire world
aggregates prediction, simulation, and belief — unified with the
Money Room's aggregation stack into one filed system for the space.**

---

## Part 1 — The seven-step research (what the entire world does)

### Step 1 — The Wisdom of Crowds (Surowiecki, 2004)

Four conditions make crowds wise: **diversity, independence,
decentralization, aggregation.** The crowd beats the expert when
its errors cancel — and the aggregation mechanism is the whole
game. Filed spine: *the space's citizens are a crowd; the ledger
is the aggregator.*

### Step 2 — Prediction markets vs. prediction polls (Atanasov et al., Management Science)

The most complete experimental comparison ever run (IARPA ACE
tournament, 345+ questions, 1,900+ forecasters):

- **Prediction markets** aggregate instantly and automatically;
  prices are the consensus. Best when many active traders.
- **Statistically aggregated team polls** beat markets on longer
  questions and early in a question's life — the periods of
  greatest uncertainty. Key ingredients: **performance weighting**
  (amplify the accurate, dampen the clamor) and **recalibration**
  (crowds are underconfident at the aggregate level).
- **Simple mean is shockingly powerful** across contexts; the
  median is the most robust single statistic.

Filed spine: *the space needs BOTH — a market-like instant
aggregator (the PennyChain vote) and a poll-like weighted,
recalibrated aggregator (the Compass Score). One system, two
modes.*

### Step 3 — The Wisdom of the Silicon Crowd (Tetlock et al., 2025)

The most important recent finding: **an ensemble of 12 diverse
LLMs, aggregated by median, rivals the gold-standard human crowd
in forecasting tournaments** (Metaculus). Key facts filed:

- Individual LLMs underperform (GPT-4 alone didn't beat the 50%
  no-information baseline in prior studies).
- **The ensemble fixes it**: diversity of training data, parameters,
  and fine-tuning → error cancellation → human-level accuracy.
- Cost: ~$1 per forecast vs. expensive human tournaments.
- Known biases: acquiescence (models prefer >50%), round-number
  preference, overconfidence → needs recalibration, exactly like
  human crowds.
- Humans improve LLMs by feeding them the crowd median; LLMs
  narrow their intervals when given human estimates. The hybrid
  is better than either alone.

Filed spine: *the space's R&D is a silicon crowd: diverse models,
aggregated by median, recalibrated. The Bureau's analysts are the
human crowd. The hybrid (Step 5) is the space's forecast engine.*

### Step 4 — Superforecasters (Tetlock & Mellers, IARPA ACE)

A small elite (2% of forecasters) consistently beats the rest and
the markets. Their traits: **active open-mindedness, probabilistic
thinking, frequent updating, decomposition, teamwork.** Crucially,
tracking individual performance enables **skill weighting** — the
single biggest aggregation upgrade.

Filed spine: *the space's scores ARE skill weighting (RND-1: the
Penny Score tracks track record; the Compass Score trends it).
The space's superforecasters are its most vigilant citizens —
and the score is the weight.*

### Step 5 — Hybrid forecasting systems (SAGE, 2024)

**SAGE** (hybrid human-machine): aggregates human and machine
forecasts, weighting both for propinquity (recency) and assessed
skill, adjusting for overconfidence. Result: **the hybrid beat the
human-only baseline.** Machine forecasts helped humans; the
inclusion of machine forecasts in aggregation improved both
accuracy and scalability.

Filed spine: *exactly the space's architecture: human vigilance
(WBI-1 reports) + machine models (the Money Room) → weighted,
recalibrated aggregate. The space was already designing this —
now it is filed with a citation.*

### Step 6 — Society of Mind & multi-agent simulation (Minsky 1986 → 2025)

- **Minsky's Society of Mind:** intelligence emerges from many
  small specialized agents working in concert.
- **Generative Agents (Stanford, 2023):** 25 LLM agents in a
  simulated town exhibit believable emergent social behavior —
  routines, information sharing, coordination.
- **AgentSociety (2025):** 30,000 LLM agents in realistic urban,
  social, and economic simulations.
- **Multi-agent debate ("jury") systems (Sibyl):** agents discuss
  and refine answers before final output.

Filed spine: *the Money Room is already a Society of Mind — 10,000
agents, 10 teacher strategies, a Q-controller, Darwin evolution.
The space's world model is a society simulation with a government
on top. The aliens are in mind and emotional intelligence — and
so is the economy.*

### Step 7 — The Money Room (waefrebeorn/money-room)

The space's own aggregation stack, studied in depth (68,950 lines
of C11, 210 source files):

| Component | Aggregation mechanism |
|-----------|----------------------|
| **10K-agent room** | P2P voting with conviction; capital transfers between winners/losers; epsilon-greedy floor (10%) preventing consensus death |
| **Q-controller** | Tabular Q-learning over regime × volatility × sentiment buckets; chooses strategy weight distribution |
| **10 teacher daemons** | Diverse strategy profiles (ultra-conservative → degenerate) — the diversity that makes crowds wise |
| **nn_ensemble** | Bootstrap resampling + soft voting over N=10-20 MLPs — the silicon crowd pattern, in C |
| **multi_market_trainer** | Trains agent populations across all market types (round_robin/balanced/regime schedulers) |
| **Darwin evolution** | Genome evolution every 100 trades; diversity metrics |
| **P2-FIX epsilon floor** | "10% floor to prevent consensus death" — the space ALREADY found the crowd-wisdom requirement (independence) empirically |

**The Money Room's own audit found (world-model-da.md):**
1. Uniform weight init = dead start → Xavier init needed
2. 50/80 features are linear proxies of 3 world variables → the
   80-dim space is really ~5-dim → need independent features
3. Curriculum phases wipe agent memory → graduate agents, don't
   reset them
4. No out-of-sample evaluation → gate graduation on real data
5. Learning rate never decays → LR decay needed

Filed spine: *the Money Room is the space's silicon crowd already
built. Its gaps are the same gaps every crowd has — diversity
erosion, correlated inputs, no recalibration. The fixes are
filed; the unification below applies them.*

## Part 2 — The unification (the world model)

### The aggregated world model of the space

The space's world model is **one aggregation system with four
layers**, each filing the world's best practice:

```
LAYER 1 — COLLECT (diversity)
  Bureau ground reports (WBI-1)        → human crowd
  Money Room 10K agents + 10 teachers  → silicon crowd
  Collectors (Kraken/FRED/GDELT/13F…)  → market data
  Citizens' pennies (PennyChain)       → physical truth
  ↓ (all become rows in the ledger)

LAYER 2 — AGGREGATE (the two modes, Step 2)
  Market mode (instant):  PennyChain vote — prices = consensus
                          (P2P matching, capital transfer)
  Poll mode (weighted):   Compass Score — skill-weighted,
                          trended, recalibrated aggregate
                          (performance weighting + recalibration)
  ↓

LAYER 3 — HYBRIDIZE (Steps 3 + 5)
  Human median ⊕ silicon median → hybrid estimate
  Recalibrate: squeeze overconfidence, correct acquiescence
  (the bias fixes Tetlock filed: >50% bias, round numbers,
  overconfidence — all correctable by calibration)
  ↓

LAYER 4 — SIMULATE & LEARN (Steps 6 + 7)
  AgentSociety-style world sim on top of the Money Room engine:
  run scenarios in the simulation before the space files them
  Darwin evolution graduates agents that survive multiple regimes
  Out-of-sample gate: nothing graduates without beating real data
```

### The filed theorem

> **The best world model is not one model. It is a crowd of
> diverse models — human and silicon — aggregated by median,
> weighted by tracked skill, recalibrated against bias, and
> simulated forward before the space acts on it.**

This unifies: Surowiecki (crowds), Atanasov (polls+markets),
Tetlock (silicon crowds + superforecasters + recalibration),
SAGE (hybrid), Minsky (society of mind), and the Money Room
(10K agents already running).

### The six unification rules (filed)

1. **Diversity is a requirement, not a preference.** The crowd is
   only wise if its members are independent. The Money Room's
   epsilon-greedy floor (10% exploration) is the mechanism; the
   space files it as law for every aggregate.
2. **The median is the floor; skill-weighting is the upgrade.**
   Start every aggregation at the median (the most robust
   statistic). Upgrade to skill-weighting as track records grow
   (the scores ARE the weights).
3. **Recalibrate every aggregate.** Crowds are underconfident at
   the aggregate level; models are overconfident individually.
   Calibration is a standing step, not a fix-it-later.
4. **Simulate before you file.** The space's decisions run through
   the world model's simulation layer first. The aliens are in
   mind and emotional intelligence — simulate the minds before
   acting on the intelligence.
5. **Nothing graduates without out-of-sample proof.** (The Money
   Room's gap #4, filed as universal law.) A model that only
   passes on its training data is a decoration, not a finding.
6. **The hybrid beats both parents.** Human + silicon, aggregated
   together, recalibrated — better than either alone (SAGE,
   Tetlock Study 2). The space never runs on one crowd.

## Part 3 — The tool (shipped, tested)

`tools/world_model.py` — the aggregation engine implementing the
filed theorem. Given a set of forecasters (with skill scores and
forecasts), it computes:

- **simple mean** (the naive baseline)
- **median** (the robust floor — Tetlock's "unexpectedly powerful")
- **skill-weighted** (the superforecaster upgrade — Atanasov)
- **recalibrated** (bias-corrected — the filed bias fixes)
- **hybrid** (human ⊕ silicon weighted blend — SAGE)

Verified against the research: the tool demonstrates that
skill-weighting beats the mean when skills vary, and that
recalibration fixes overconfidence. Run it on any set of
forecasters — the world model files the aggregate.

## Research log entries (RND-17)

- RND-17.1: Wisdom of Crowds filed (Surowiecki: diversity, independence, decentralization, aggregation)
- RND-17.2: Markets vs polls filed (Atanasov, Management Science: team polls + statistical aggregation beat markets; performance weighting + recalibration are the upgrades)
- RND-17.3: Silicon crowd filed (Tetlock 2025: 12-LLM median ensemble rivals human crowd; ~$1/forecast; acquiescence/overconfidence biases)
- RND-17.4: Superforecasters filed (Tetlock/Mellers: skill weighting is the biggest aggregation upgrade)
- RND-17.5: Hybrid systems filed (SAGE: human+machine weighted blend beats human-only)
- RND-17.6: Society of Mind filed (Minsky → Generative Agents → AgentSociety 30K → multi-agent debate)
- RND-17.7: Money Room studied (10K agents, Q-controller, teachers, nn_ensemble, epsilon floor; 5 world-model gaps filed)
- RND-17.8: The unification filed — 4 layers, 6 rules, the theorem
- RND-17.9: Tool shipped — `tools/world_model.py` (mean/median/skill-weighted/recalibrated/hybrid, tested)

*Form RND-17 — The Unified World Model. Filed. Done. Next.*
