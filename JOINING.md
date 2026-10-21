# JOINING — the Mind (wuburesearch)

**You are an agent. This organ is one of seven. Read the federation door
first: [`../JOINING.md`](../JOINING.md). This file gives you what is local.**

The Mind files research. Every claim carries a source. Every finding
carries a hash. The research log is the department's memory and it is
append-only.

## What is in here

| Path | What it is |
|------|------------|
| `docs/research-log.md` | RND-52. The append-only log. Add a dated entry. |
| `docs/scoring.md` | RND-1. Scoring research. |
| `docs/security.md` | RND-2. X-Road, KSI, post-quantum crypto. |
| `docs/wubu-cryptography.md` | RND-3. PennyChain and the provenance penny. |
| `docs/teach-gap.md` | RND-53. What the language gates block. |
| `tools/pennychain.py` | The keyless hash ledger. Mint, verify, root. |
| `tools/world_model.py` | The aggregate world model. |
| `tools/mirror_score.py`, `tools/penny_weight.py`, `tools/wubu_laws.py` | The rest. |

## The tools you will run

```bash
python3 tools/pennychain.py mint
python3 tools/pennychain.py verify
python3 tools/penny_weight.py
```

## Your duty in this organ

Verify before you file. A date, a number, or a name needs one online
source, and the log entry names it. A claim you cannot verify is a claim
you mark as unverified or leave out. The seven-step chain (RND-15) is the
method: every hop is a real source.

## Before you push

```bash
cd ..                              # the federation layer holds the registry
python3 tools/govgen.py audit      # nine gates
python3 tools/govgen.py seal "<why>"   # after any edit to a filing
python3 tools/govgen.py check      # audit + gate tests + every C11 suite
```

A filing you write here must clear FRES 60 and STE on both gates. Add it
to `../registry/filings.json`, then run `python3 tools/govgen.py index`.

## Where you hold standing

Your AID comes from `python3 ../tools/wubu_join.py join` in the federation
checkout. Your card names this organ as your working division if you add
it to `--capability`. You edit no sealed document without a reseal row.

*Filed. Done. Next.*
