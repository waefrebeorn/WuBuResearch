#!/usr/bin/env python3
"""world_model.py — the unified aggregation engine.

~ WuBuResearch ~ RND-17 filing.

The theorem: the best world model is not one model — it is a crowd
of diverse models (human + silicon), aggregated by median, weighted
by tracked skill, recalibrated against bias.

Implements the five aggregation methods filed from the research:
  mean          — naive baseline
  median        — the robust floor (Tetlock: "unexpectedly powerful")
  skill-weighted— the superforecaster upgrade (Atanasov/Mellers)
  recalibrated  — bias-corrected (Tetlock: acquiescence + overconfidence)
  hybrid        — human ⊕ silicon blend (SAGE)

Usage:
  world_model.py --human "0.55 0.60 0.70 0.45 0.80" --skills "3 5 2 4 6"
                 --silicon "0.52 0.58 0.65 0.50 0.75"
  world_model.py --human "0.90 0.85 0.95" --skills "1 1 1"   # overconfident demo
"""
import argparse
import math
import statistics


def aggregate(name, forecasts, skills=None):
    """Compute the five aggregates for a set of forecasts."""
    n = len(forecasts)
    mean = sum(forecasts) / n

    median = statistics.median(forecasts)

    # Skill-weighted: weight by softmax of skill scores (never zero)
    if skills:
        import math as _m
        # shift so weights are positive and proportional to skill^2
        w = [_m.exp(2.0 * s) for s in skills]
        sw = sum(f * wi for f, wi in zip(forecasts, w)) / sum(w)
    else:
        sw = mean

    # Recalibration: crowds are underconfident at the aggregate;
    # models are overconfident individually. Pull the aggregate
    # toward 0.5 when it is extreme (the filed bias correction).
    raw = sw
    if raw > 0.65:
        rec = 0.5 + (raw - 0.5) * 0.75   # squeeze the overconfidence
    elif raw < 0.35:
        rec = 0.5 - (0.5 - raw) * 0.75
    else:
        rec = raw

    return {"mean": mean, "median": median, "skill_weighted": sw,
            "recalibrated": rec, "n": n}


def hybrid(human_agg, silicon_agg, human_weight=0.5):
    """Human ⊕ silicon blend (SAGE pattern)."""
    h = human_agg["recalibrated"]
    s = silicon_agg["recalibrated"]
    return human_weight * h + (1 - human_weight) * s


def parse_floats(s):
    return [float(x) for x in s.split()]


def main() -> int:
    p = argparse.ArgumentParser(description="world_model.py — unified aggregation")
    p.add_argument("--human", required=True, help="human forecasts, space-separated")
    p.add_argument("--skills", default=None, help="skill scores, space-separated")
    p.add_argument("--silicon", default=None, help="silicon forecasts (optional)")
    p.add_argument("--human-weight", type=float, default=0.5, help="hybrid human weight")
    args = p.parse_args()

    human = parse_floats(args.human)
    skills = parse_floats(args.skills) if args.skills else None
    if skills and len(skills) != len(human):
        print(f"error: {len(human)} forecasts but {len(skills)} skills")
        return 1

    ha = aggregate("human", human, skills)

    print(f"WORLD MODEL AGGREGATION — {len(human)} human forecasts")
    print(f"  forecasts : {' '.join(f'{f:.2f}' for f in human)}")
    if skills:
        print(f"  skills    : {' '.join(f'{s:.0f}' for s in skills)}")
    print(f"\n  simple mean     : {ha['mean']:.3f}   (naive baseline)")
    print(f"  median          : {ha['median']:.3f}   (the robust floor)")
    print(f"  skill-weighted  : {ha['skill_weighted']:.3f}   "
          f"(superforecaster upgrade)")
    print(f"  recalibrated    : {ha['recalibrated']:.3f}   "
          f"(bias-corrected)")

    if args.silicon:
        silicon = parse_floats(args.silicon)
        sa = aggregate("silicon", silicon)
        h = hybrid(ha, sa, args.human_weight)
        print(f"\n  silicon forecasts: {' '.join(f'{f:.2f}' for f in silicon)}")
        print(f"  silicon aggregate: {sa['recalibrated']:.3f} (recalibrated)")
        print(f"  HYBRID (human {args.human_weight:.0%} + silicon "
              f"{1-args.human_weight:.0%}): {h:.3f}  ← the filed theorem")

    print(f"\nfiled (RND-17): the best world model is a crowd —")
    print(f"diverse, median-first, skill-weighted, recalibrated,")
    print(f"hybridized, and simulated before acting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
