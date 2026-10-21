# The Teach Gap — what the language gates actually block

**R&D filing RND-53. The space claims it teaches (GOV-26). The language
gates say most of the corpus does not. This filing measures the gap,
explains why the floor is hard, and refuses the easy fix.**

---

## Part 1 — The measurement

The Hands ran the space's own gates over the whole corpus on 2026-10-21.
Every number below comes from a tool, not from an estimate.

| Measure | Result | Source |
|---------|--------|--------|
| Documents scanned | 276 | `govgen lang` |
| FRES CLEAR (RND-20 floor: 60) | 82 (29.7%) | `plain_lang` |
| STE CLEAR (RND-22 discipline) | 30 (10.9%) | `plain_lang --ste` |
| Filings teaching on all four rungs | 1 of 143 (0.7%), before this filing existed | `wubu_edu` |
| STATE filings passing the TEACH rung | 39 of 71 | `wubu_edu` |
| LEDGER filings passing the TEACH rung | 0 of 9 | `wubu_edu` |

Two defects hid the second half of that table.

1. `wubu_edu.py` joined the repo path onto a registry `file` that already
   carried it. Every document looked missing, so every filing read TEACH
   = 0. The tool reported 0 of 143 when the true figure was 1 of 143 and
   51 documents did pass.
2. The audit's reference scanner swallowed the period after a number, so
   a citation at the end of a sentence was never checked. See GOV-77.

## Part 2 — Why the floor is hard

Flesch Reading Ease is a function of two ratios: words per sentence and
syllables per word.

```
FRES = 206.835 - 1.015 x (words / sentences) - 84.6 x (syllables / words)
```

`precedents.md` (ECO-1) is a fair example. It holds 1,404 words in 166
sentences (8.5 words per sentence) and 1.71 syllables per word, so it
scores 53.8. The floor asks for 60. Holding syllables fixed, 60 needs
2.3 words per sentence — sixty per cent more sentences than there are.
Holding sentence length fixed, 60 needs 1.64 syllables per word, which
means replacing about one hundred syllables across the filing.

Neither is a formatting change. Both are a rewrite of the prose.

Removing the ledger bullets raises ECO-1 to roughly 53 on the same
measure. The density is in the sentences, not in the structure.

## Part 3 — The refusal

Someone can make the gate green in one afternoon. Lower the floor.
Exclude the bullets. Count only the paragraphs a reviewer chooses. Each
move is Goodhart's Law (GOV-8). A measure becomes a target, and the
target stops measuring.

The floor stays at 60. The corpus does not pass. This filing records
both facts.

## Part 4 — The path that does not lie

1. **New and amended filings clear both gates before filing** (RND-22,
   already binding). This is why GOV-77 and this filing use short sentences.
2. **Legacy filings form a queue, not an excuse.** `govgen lang` now
   writes the queue: the thirty documents furthest below the floor,
   ranked, with the points needed. Work comes off the queue in order.
3. **Split the doctrine from the record.** A filing has two jobs. It
   teaches a newcomer, and it keeps an exact ledger of what the space filed
   and from where. Dense filing-log bullets serve the second job. They block
   the first. The proposal: each LEDGER filing gains a short doctrine
   section that the gate reads. It keeps its dated ledger entries as a
   record the gate treats as structure, the way it treats tables and
   code.
4. **Measure the split before building it.** The next pass runs the gates
   on the doctrine sections alone. If LEDGER prose still scores below 60,
   the split did not help and the rewrite is the only path.

## Part 5 — What this filing is not

This is not a plan with dates. It is a measurement, a refusal, and a
queue. A tool generates the queue, so the space cannot lose it, and the
doctrine cannot pass by forgetting.

---

*Form RND-53 — The Teach Gap. Filed. Done. Next.*
