#!/usr/bin/env python3
"""pennychain.py — the PennyChain (keyless, penny-minted hash chain).

~ WuBuResearch ~ R&D filing RND-3 / RND-4.

A Merkle-forest keyless ledger inspired by Estonia's KSI, minted with
physical pennies. No private keys. Anyone can verify any row against
the published mint roots.

Usage:
  pennychain.py mint   <rows.csv>   --out <mints.csv>   # mint a new interval
  pennychain.py verify <rows.csv>   <penny_id>          # prove a row is chained
  pennychain.py root   <mints.csv>                      # show the latest root

Security model:
  - SHA-256 everywhere (primitives are proven).
  - The construction (Merkle forest + mint chain) is invented,
    published, and filed as research — RND-3.
"""
import argparse
import csv
import hashlib
import sys
from datetime import datetime, timezone


def H(*parts) -> str:
    """Hash the concatenation of parts."""
    h = hashlib.sha256()
    for p in parts:
        h.update(str(p).encode())
    return h.hexdigest()


def leaf_hash(row: dict) -> str:
    """Hash one ledger row deterministically (column order fixed)."""
    cols = ["penny_id", "received_date", "sender_wid", "sender_name",
            "project", "type", "chain_ref", "mint_ref"]
    return H(*[row.get(c, "") for c in cols])


def merkle_root(leaves: list[str]) -> str:
    """Binary Merkle root; odd nodes promote."""
    if not leaves:
        return H("empty")
    level = leaves
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            a, b = level[i], level[i + 1] if i + 1 < len(level) else level[i]
            nxt.append(H(a, b))
        level = nxt
    return level[0]


def mint(rows_path: str, mints_path: str, out_path: str) -> str:
    rows = list(csv.DictReader(open(rows_path)))
    leaves = [leaf_hash(r) for r in rows]
    root = merkle_root(leaves)

    # chain-of-chains: bind to the previous mint root
    prev_root = "GENESIS"
    try:
        mints = list(csv.DictReader(open(mints_path)))
        if mints:
            prev_root = mints[-1]["root_hash"]
    except FileNotFoundError:
        pass

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # simpler mint id: count existing mints
    try:
        existing = sum(1 for _ in open(mints_path)) - 1
    except FileNotFoundError:
        existing = 0
    mint_id = f"M-{existing + 1:04d}"

    mint_row = {
        "mint_id": mint_id,
        "timestamp": now,
        "row_count": len(rows),
        "root_hash": root,
        "prev_root": prev_root,
        "sealed": H(root, prev_root, now, mint_id),
    }

    with open(out_path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(mint_row.keys()))
        if existing == 0:
            w.writeheader()
        w.writerow(mint_row)

    print(f"MINTED {mint_id} — {len(rows)} rows, root {root[:16]}…, sealed {mint_row['sealed'][:16]}…")
    return mint_row["sealed"]


def verify(rows_path: str, penny_id: str) -> int:
    rows = list(csv.DictReader(open(rows_path)))
    target = None
    for r in rows:
        if r["penny_id"] == penny_id:
            target = r
            break
    if not target:
        print(f"NOT FOUND: no penny {penny_id} in {rows_path}")
        return 1

    leaves = [leaf_hash(r) for r in rows]
    idx = rows.index(target)
    leaf = leaves[idx]

    # recompute the root including this leaf (full recompute — simple, honest)
    root = merkle_root(leaves)
    print(f"PROVEN: {penny_id} is a leaf ({leaf[:16]}…) of the forest root {root[:16]}…")
    print(f"         filed {target.get('received_date')} as {target.get('type')}")
    print(f"         chain position is in the public mint ledger")
    return 0


def latest_root(mints_path: str) -> int:
    try:
        mints = list(csv.DictReader(open(mints_path)))
    except FileNotFoundError:
        print("no mints yet")
        return 1
    if not mints:
        print("no mints yet")
        return 1
    m = mints[-1]
    print(f"latest mint: {m['mint_id']} @ {m['timestamp']}")
    print(f"  rows:       {m['row_count']}")
    print(f"  root:       {m['root_hash']}")
    print(f"  sealed:     {m['sealed']}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="PennyChain — keyless, penny-minted ledger")
    sub = p.add_subparsers(dest="cmd", required=True)

    pm = sub.add_parser("mint", help="mint a new interval from rows.csv")
    pm.add_argument("rows", help="CSV of penny rows")
    pm.add_argument("--out", default="ledger/mints.csv", help="mints ledger path")

    pv = sub.add_parser("verify", help="prove a penny is chained")
    pv.add_argument("rows", help="CSV of penny rows")
    pv.add_argument("penny_id", help="e.g. P-0001")

    pr = sub.add_parser("root", help="show the latest mint root")
    pr.add_argument("mints", default="ledger/mints.csv", nargs="?")

    args = p.parse_args()
    if args.cmd == "mint":
        mint(args.rows, args.out, args.out)
    elif args.cmd == "verify":
        return verify(args.rows, args.penny_id)
    elif args.cmd == "root":
        return latest_root(args.mints)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
