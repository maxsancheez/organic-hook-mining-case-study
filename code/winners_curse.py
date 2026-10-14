#!/usr/bin/env python3
"""
Do the most-viewed organic hooks make the best-converting ads?

A toy model of why "copy the top organic hooks" works, and where it breaks.
Every hook has three hidden traits:
  appeal  - genuinely stops the right person and makes them want the product
  bait    - provocation/outrage/curiosity that wins views but not trust
            (Tucker 2015: viral ads lose ~10% persuasiveness per 1M views)
and every post gets
  reach   - the creator's audience size (known: you can see follower counts)
  luck    - algorithm timing and randomness (unknown)

Organic views  = appeal + bait_weight * bait + reach + luck
Paid result    = appeal - bait_weight * bait * PERSUASION_PENALTY + test noise

All parameters are ILLUSTRATIVE. The point is the shape of the result.
Standard library only.  Run:  python3 winners_curse.py
"""

import math
import random
import statistics

N_POSTS = 300          # organic posts you scroll through for one keyword
PICK = 5               # hooks you can afford to turn into ads
REACH_SD = 1.2         # creators differ a lot in audience size
LUCK_SD = 1.0          # algorithm randomness
PERSUASION_PENALTY = 0.6
TEST_NOISE_SD = 0.5    # a small paid test measures the paid result noisily
BASE_CVR = 0.010       # 1.0% conversion rate for an average hook
CVR_SENSITIVITY = 0.35 # each 1 SD of paid result = ~42% relative CVR change
REPS = 2000


def cvr(paid):
    return BASE_CVR * math.exp(CVR_SENSITIVITY * paid)


def one_round(rng, bait_weight):
    posts = []
    for _ in range(N_POSTS):
        appeal, bait = rng.gauss(0, 1), rng.gauss(0, 1)
        reach, luck = rng.gauss(0, REACH_SD), rng.gauss(0, LUCK_SD)
        posts.append({
            "views": appeal + bait_weight * bait + reach + luck,
            "outlier": appeal + bait_weight * bait + luck,  # views minus known reach
            "paid": appeal - bait_weight * bait * PERSUASION_PENALTY,
        })

    def avg_cvr(chosen):
        return statistics.mean(cvr(p["paid"]) for p in chosen)

    random_pick = rng.sample(posts, PICK)
    top_views = sorted(posts, key=lambda p: -p["views"])[:PICK]
    top_outlier = sorted(posts, key=lambda p: -p["outlier"])[:PICK]
    # test-then-scale: shortlist 20 by outlier score, run cheap tests, keep best 5
    shortlist = sorted(posts, key=lambda p: -p["outlier"])[:20]
    tested = sorted(shortlist, key=lambda p: -(p["paid"] + rng.gauss(0, TEST_NOISE_SD)))[:PICK]
    best_possible = sorted(posts, key=lambda p: -p["paid"])[:PICK]
    return {
        "Random 5 hooks": avg_cvr(random_pick),
        "Top 5 by views (the reel)": avg_cvr(top_views),
        "Top 5 by views/followers": avg_cvr(top_outlier),
        "Shortlist 20, test, keep 5": avg_cvr(tested),
        "Perfect hindsight": avg_cvr(best_possible),
    }


def run(bait_weight, seed=11):
    rng = random.Random(seed)
    totals = {}
    for _ in range(REPS):
        for k, v in one_round(rng, bait_weight).items():
            totals.setdefault(k, []).append(v)
    return {k: statistics.mean(v) for k, v in totals.items()}


def main():
    print(f"{N_POSTS} organic posts, pick {PICK} hooks to run as ads, "
          f"{REPS} simulated rounds, base CVR {BASE_CVR:.1%}\n")
    for bait_weight, label in ((0.0, "no bait (views come only from real appeal)"),
                               (0.7, "some bait (typical feed)"),
                               (1.5, "heavy bait (health/outrage niches)")):
        res = run(bait_weight)
        base = res["Random 5 hooks"]
        print(f"Scenario: {label}")
        for k, v in res.items():
            print(f"  {k:28} CVR {v:.2%}   {v / base - 1:+6.0%} vs random")
        print()

    # Winner's curse: how much of the organic outperformance carries over?
    rng = random.Random(3)
    carry = []
    for _ in range(REPS):
        posts = [(rng.gauss(0, 1), rng.gauss(0, LUCK_SD)) for _ in range(N_POSTS)]
        top = sorted(posts, key=lambda p: -(p[0] + p[1]))[:PICK]
        seen = statistics.mean(a + l for a, l in top)
        real = statistics.mean(a for a, _ in top)
        carry.append(real / seen)
    print(f"Winner's curse (no bait, reach removed): the top {PICK} hooks' organic edge is "
          f"about {statistics.mean(carry):.0%} real appeal and "
          f"{1 - statistics.mean(carry):.0%} luck.")


if __name__ == "__main__":
    main()
