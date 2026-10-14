#!/usr/bin/env python3
"""
Rank organic posts by how far they outperformed their own audience, tag the
hook pattern each one uses, flag ad-policy risks, and pick a shortlist of
hooks to test as paid ads.

Input: a CSV you collect by hand from TikTok/Instagram search for your
customer's problem (columns: post_id, hook, views, likes, comments, shares,
followers, days_live). sample_posts.csv is SYNTHETIC example data.

Standard library only.  Run:  python3 hook_miner.py [posts.csv]
"""

import csv
import math
import os
import re
import statistics
import sys

# Hook patterns: the reusable "shape" of a hook, not its exact words.
PATTERNS = {
    "body-spot callout": r"\b(right here|behind|front of|inside of|outside of|back of|where exactly|tap the spot)\b",
    "question":          r"\?",
    "number/list":       r"\b\d+\b",
    "authority":         r"\b(physio|doctor|doctors|surgeon|patient)\b",
    "contrarian":        r"\b(stop|not|isn'?t|hate|myth|wrong)\b",
    "home remedy/hack":  r"\b(lime|remedy|grandma|all you need|trick)\b",
    "testimonial":       r"\b(i|my)\b",
    "sensation":         r"\b(feels|so good)\b",
}

# Ad-policy risk flags (organic posts can say things paid ads can't).
FLAGS = {
    # Meta's personal-attributes policy: ads can't imply they know your health condition
    "personal-attribute": r"\b(your knee|your knees|you have|your pain)\b",
    # FTC: health benefit claims need competent and reliable scientific evidence
    "health claim":       r"\b(fixed|fix|cure|without surgery|remedy|helped|all you need)\b",
    # engagement bait: high views, likely low persuasion (Tucker 2015)
    "bait":               r"\b(hate this|trick|swore by)\b",
}


def zscores(values):
    mu, sd = statistics.mean(values), statistics.pstdev(values) or 1.0
    return [(v - mu) / sd for v in values]


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in ("views", "likes", "comments", "shares", "followers", "days_live"):
            r[k] = float(r[k])
    return rows


def score(rows):
    # 1. Outlier ratio: views relative to the creator's own following.
    #    A 4M-view post from a 600k account is less surprising than 1M from 50k.
    outlier = [math.log10(r["views"] / max(r["followers"], 1)) for r in rows]
    # 2. Share rate: shares mean "this is useful/relatable enough to send".
    share = [math.log10(1 + 1000 * r["shares"] / r["views"]) for r in rows]
    # 3. Comment rate: comments can mean interest or outrage, so weigh lightly.
    comment = [math.log10(1 + 1000 * r["comments"] / r["views"]) for r in rows]
    zo, zs, zc = zscores(outlier), zscores(share), zscores(comment)
    for r, a, b, c, o in zip(rows, zo, zs, zc, outlier):
        r["outlier_x"] = 10 ** o
        r["score"] = a + 0.5 * b + 0.25 * c
        text = r["hook"].lower()
        r["patterns"] = [p for p, rx in PATTERNS.items() if re.search(rx, text)]
        r["flags"] = [f for f, rx in FLAGS.items() if re.search(rx, text)]
    return sorted(rows, key=lambda r: -r["score"])


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "sample_posts.csv")
    rows = score(load(path))

    print(f"Ranked {len(rows)} organic posts (score = audience outlier + share rate + comments)\n")
    print(f"{'#':>2} {'score':>6} {'views/fol':>9} {'views':>6}  hook")
    for i, r in enumerate(rows[:10], 1):
        flag = f"  [{', '.join(r['flags'])}]" if r["flags"] else ""
        print(f"{i:>2} {r['score']:>6.2f} {r['outlier_x']:>8.1f}x {r['views']/1e6:>5.1f}M  "
              f"{r['hook'][:58]}{flag}")

    by_views = sorted(rows, key=lambda r: -r["views"])[:10]
    overlap = len({r["post_id"] for r in by_views} & {r["post_id"] for r in rows[:10]})
    print(f"\nOnly {overlap}/10 of the most-VIEWED posts are in the top 10 by outlier score.")

    print("\nHook patterns (median score, posts using it):")
    stats = []
    for p in PATTERNS:
        s = [r["score"] for r in rows if p in r["patterns"]]
        if s:
            stats.append((statistics.median(s), len(s), p))
    for med, n, p in sorted(stats, reverse=True):
        bar = "#" * max(0, int((med + 1.5) * 6))
        print(f"  {p:18} {med:>6.2f}  n={n:<2} {bar}")

    print("\nShortlist to test as paid ads (above-average score, no policy flags, one per pattern):")
    used, picks = set(), []
    for r in rows:
        lead = r["patterns"][0] if r["patterns"] else "plain"
        if r["score"] > 0 and not r["flags"] and lead not in used:
            used.add(lead)
            picks.append(r)
        if len(picks) == 5:
            break
    for r in picks:
        print(f"  - [{', '.join(r['patterns']) or 'plain'}] {r['hook']}")
    print("\nRewrite each in your own words and footage. Copy the pattern, not the video.")


if __name__ == "__main__":
    main()
