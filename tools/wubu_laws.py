#!/usr/bin/env python3
"""wubu_laws.py — the WuBu Laws of Tools compliance checker.

~ WuBuResearch ~ RND-19 filing (GOV-3).

The five laws of the space's tools (filed RND-19.7):

  LAW 1 — A tool may not harm a first one, or through inaction,
          allow a first one to come to harm.           (non-maleficence)
  LAW 2 — A tool's first duty is to the filing, not to the
          user's comfort.                              (duty clause)
  LAW 3 — A tool must be able to tell the user they are wrong.
                                                        (entropy)
  LAW 4 — A tool must be explicable: how it works and who is
          responsible must be publicly fileable.       (explicability)
  LAW 5 — A tool may not exploit the want for companionship.
                                                        (vehicle clause)

Usage:
  wubu_laws.py --no-harm 1 --filing-over-comfort 1 --can-say-no 1 \
               --explicable 1 --no-companion 1
  wubu_laws.py --no-harm 1 --filing-over-comfort 0 --can-say-no 0 \
               --explicable 0 --no-companion 0
"""
import argparse

LAWS = [
    ("no-harm", "Law 1 — may not harm a first one, or allow harm through inaction"),
    ("filing-over-comfort", "Law 2 — first duty is to the filing, not the user's comfort"),
    ("can-say-no", "Law 3 — must be able to tell the user they are wrong (entropy)"),
    ("explicable", "Law 4 — must be explicable and accountable in public"),
    ("no-companion", "Law 5 — may not exploit the want for companionship"),
]


def main() -> int:
    p = argparse.ArgumentParser(description="wubu_laws.py — the WuBu Laws of Tools")
    p.add_argument("--no-harm", type=int, choices=[0, 1], required=True)
    p.add_argument("--filing-over-comfort", type=int, choices=[0, 1], required=True)
    p.add_argument("--can-say-no", type=int, choices=[0, 1], required=True)
    p.add_argument("--explicable", type=int, choices=[0, 1], required=True)
    p.add_argument("--no-companion", type=int, choices=[0, 1], required=True)
    args = p.parse_args()

    values = [args.no_harm, args.filing_over_comfort, args.can_say_no,
              args.explicable, args.no_companion]

    print("WUBU LAWS OF TOOLS — compliance check")
    print("=" * 62)
    satisfied = 0
    for (flag, law), val in zip(LAWS, values):
        mark = "✅" if val else "❌"
        print(f"  {mark} {law}")
        satisfied += val

    print("=" * 62)
    print(f"  {satisfied}/5 laws satisfied")

    if satisfied == 5:
        print("  verdict: ALL FIVE LAWS SATISFIED — the tool is a tool.")
        print("  filed: it files, it challenges, it explains, it never pleases.")
    elif satisfied >= 3:
        print("  verdict: PARTIAL — the tool leans tool, but has mirror features.")
        print("  filed: recalibrate per GOV-3 Article VI (Entropy Requirement).")
    else:
        print("  verdict: VIOLATION — the tool is a mirror; recalibrate or retire.")
        print("  filed: a mirror has no place in the space (GOV-3).")

    print(f"\nfiled (RND-19): Asimov's laws were fiction for stories;")
    print(f"the space's laws are filings for audits. responsibility")
    print(f"stays with the humans — the tool is only what it files.")
    return 0 if satisfied == 5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
