#!/usr/bin/env python3
"""penny_weight.py — the Penny Standard audit & redemption calculator.

~ WuBuResearch ~ R&D filing RND-6.

The reserve is verified by MASS, not by count. Class-counted weighing:
weigh the copper class and the zinc class separately, divide by the
Mint's constants, sum. That is the reserve. That is the audit.

Verified specs (U.S. Mint):
  copper (pre-1982, some 1982): 3.11 g per penny
  zinc   (Oct 1982-present):    2.50 g per penny

Usage:
  penny_weight.py audit  --copper 3110 --zinc 25000
      # weigh each class (grams) -> reserve count + face value

  penny_weight.py worth  --total 28110 --copper-share 0.1106
      # a mixed pile: total grams + fraction that is copper

  penny_weight.py redeem --pennies 10000
      # what a 10,000-penny IOU ships as: weight per class

  penny_weight.py shipping --pennies 500 --per 100
      # how many shipping envelopes at N pennies per envelope
"""
import argparse

COPPER_G = 3.11   # grams per pre-1982 copper penny
ZINC_G = 2.50     # grams per post-1982 zinc penny


def audit(copper_g: float, zinc_g: float) -> dict:
    copper_count = copper_g / COPPER_G
    zinc_count = zinc_g / ZINC_G
    total = copper_count + zinc_count
    return {
        "copper_class": copper_g,
        "zinc_class": zinc_g,
        "copper_pennies": copper_count,
        "zinc_pennies": zinc_count,
        "total_pennies": total,
        "face_value_cents": round(total),
        "face_value_dollars": round(total / 100, 2),
    }


def worth(total_g: float, copper_share: float) -> dict:
    copper_g = total_g * copper_share
    zinc_g = total_g * (1 - copper_share)
    return audit(copper_g, zinc_g)


def redeem(pennies: int, copper_share: float = 0.0) -> dict:
    """What a redemption ships: weight per class."""
    copper_n = pennies * copper_share
    zinc_n = pennies * (1 - copper_share)
    return {
        "pennies": pennies,
        "copper_pennies": copper_n,
        "zinc_pennies": zinc_n,
        "copper_weight_g": copper_n * COPPER_G,
        "zinc_weight_g": zinc_n * ZINC_G,
        "total_weight_g": copper_n * COPPER_G + zinc_n * ZINC_G,
        "total_weight_kg": (copper_n * COPPER_G + zinc_n * ZINC_G) / 1000,
    }


def shipping(pennies: int, per_envelope: int) -> dict:
    envelopes, remainder = divmod(pennies, per_envelope)
    return {
        "pennies": pennies,
        "per_envelope": per_envelope,
        "full_envelopes": envelopes,
        "remainder": remainder,
        "envelopes_needed": envelopes + (1 if remainder else 0),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Penny Standard audit & redemption")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("audit", help="audit the reserve by class weight")
    a.add_argument("--copper", type=float, required=True, help="grams of copper-class pennies")
    a.add_argument("--zinc", type=float, required=True, help="grams of zinc-class pennies")

    w = sub.add_parser("worth", help="a mixed pile: total grams + copper share")
    w.add_argument("--total", type=float, required=True, help="total grams of the pile")
    w.add_argument("--copper-share", type=float, default=0.0, help="fraction that is copper (0..1)")

    r = sub.add_parser("redeem", help="what a redemption ships, by weight")
    r.add_argument("--pennies", type=int, required=True, help="number of pennies to ship")
    r.add_argument("--copper-share", type=float, default=0.0, help="fraction that is copper")

    s = sub.add_parser("shipping", help="envelope math for a redemption")
    s.add_argument("--pennies", type=int, required=True)
    s.add_argument("--per", type=int, default=100, help="pennies per envelope")

    args = p.parse_args()
    if args.cmd == "audit":
        res = audit(args.copper, args.zinc)
        print(f"RESERVE AUDIT — class-counted weighing")
        print(f"  copper class {res['copper_class']}g / 3.11 = {res['copper_pennies']:.0f} pennies")
        print(f"  zinc class   {res['zinc_class']}g / 2.50 = {res['zinc_pennies']:.0f} pennies")
        print(f"  RESERVE: {res['total_pennies']:.0f} pennies = ${res['face_value_dollars']}")
    elif args.cmd == "worth":
        res = worth(args.total, args.copper_share)
        print(f"MIXED PILE — {args.total}g, copper share {args.copper_share:.1%}")
        print(f"  copper ~{res['copper_pennies']:.0f} pennies, zinc ~{res['zinc_pennies']:.0f} pennies")
        print(f"  RESERVE: ~{res['total_pennies']:.0f} pennies = ~${res['face_value_dollars']}")
    elif args.cmd == "redeem":
        res = redeem(args.pennies, args.copper_share)
        print(f"REDEMPTION — {res['pennies']} pennies (copper share {args.copper_share:.1%})")
        print(f"  ships: {res['copper_pennies']:.0f} copper ({res['copper_weight_g']:.0f}g) + "
              f"{res['zinc_pennies']:.0f} zinc ({res['zinc_weight_g']:.0f}g)")
        print(f"  total weight: {res['total_weight_kg']:.3f} kg")
    elif args.cmd == "shipping":
        res = shipping(args.pennies, args.per)
        print(f"SHIPPING — {res['pennies']} pennies at {res['per_envelope']}/envelope")
        print(f"  envelopes needed: {res['envelopes_needed']} "
              f"({res['full_envelopes']} full + {res['remainder']} remainder)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
