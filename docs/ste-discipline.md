# The STE Discipline — the Second Gate

**R&D filing RND-22. The correction, filed and enacted.** The
space's technical documentation must adhere to ASD-STE100
Simplified Technical English. FRES (RND-20) is the floor — it
measures readability. STE is the discipline — it governs the
words. A filing can score CLEAR on FRES and still be slop; STE
is the anti-slop gate. The checker (`plain_lang --ste`,
WuBuCore) applies the rules.

---

## Part 1 — The correction, filed verbatim

> *"You can get LLMs to write good non-AI-slop-sounding technical
> documentation by requiring them to adhere to ASD-STE100
> Simplified Technical English."*

— **The User, filed verbatim, RND-22.**

## Part 2 — The rules, filed

ASD-STE100 is the international standard for clear, safe,
consistent technical writing. It comes from the AeroSpace and
Defence Industries Association of Europe. It is a controlled
natural language. Two parts:

### 1. The controlled vocabulary (~900 approved words)

- Only approved words, each with **one meaning and one part of
  speech**.
- Unapproved words have approved alternatives in the dictionary.
- Technical names and technical verbs may enter the dictionary
  (the space adds: WID, Penny Score, PennyChain, filing, ledger,
  first one).
- **Consistency rule (1.12):** once you choose a word, continue
  to use it. No synonyms for the same thing.

### 2. The writing rules

The gate's table:

| Rule | STE | The gate checks |
|------|-----|-----------------|
| Sentence length | ≤ 20 words (procedure), ≤ 25 (description) | `--ste` flags > 20/25 |
| Voice | Active voice | passive markers, minus statives |
| Tense | Simple past + simple future approved | present perfect flagged |
| Conjunctions | Pick one | `and/or` flagged |
| Abbreviations | None in prose | `i.e.` `e.g.` `etc.` flagged |
| Noun clusters | Technical noun ≤ 3 words | 5+ content-word runs flagged |
| Instructions | Imperative: "Do this." | — |
| Consistency | One term per thing, always | — |

The quoted examples of violations (what NOT to write) are
definitions, not prose. They are filed in a code fence below. The
gate reads fences as structure. The rule book names its own sins
the way the banned-word list (RND-20) does:

```
Do not write: "adjusted and/or verified etc. by the user"
Write:       "Adjust the settings. Verify them."
Do not write: "has been designed"
Write:       "the design is" (or simply past: "we designed")
Do not write: "the comprehensive data integration platform framework"
Write:       "the platform" (technical nouns have at most 3 words)
```

## Part 3 — The amendment

The Language Doctrine (RND-20) gains a second gate: **plain
language has two gates.**

1. **The FRES gate (RND-20, `plain_lang`):** readability floor —
   FRES ≥ 60, grade ≤ 8. Measures how hard the filing is to read.
2. **The STE gate (RND-22, `plain_lang --ste`):** discipline —
   sentence caps, active voice, approved-word behavior, no
   `and/or`, no `etc.`, no present perfect, no noun clusters.
   Measures whether the filing reads like a professional
   technical document or reads like generated slop.

A filing that passes FRES but fails STE returns for rewriting.
A filing that passes both is the space's standard: **clear enough
to read, disciplined enough to trust.**

## Part 4 — The tool

The STE gate is a mode of the existing checker (WuBuCore):

```
$ plain_lang --ste filing.md
STE: sentence 14 words (ok, <= 20)
STE: sentence 27 words (FAIL, > 25 description cap)
STE: PASSIVE "should be adjusted" (Rule 3.6: use active voice)
STE: "and/or" (pick one: X, or Y, or both)
STE: "etc." (no abbreviations in prose)
STE: PRESENT PERFECT "has filed" (use simple past)
STE verdict: REWRITE - 4 STE violations (RND-22)
```

The gate speaks STE so the space's docs speak STE. Filed.

*Form RND-22 — The STE Discipline. Filed. Done. Next.*
