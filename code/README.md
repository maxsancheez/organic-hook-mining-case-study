# code

Two standard-library Python scripts (Python 3.8+, no installs).

## hook_miner.py: rank and tag organic hooks

```bash
python3 hook_miner.py
```

```bash
python3 hook_miner.py my_posts.csv
```

Feed it a CSV you collect by hand from a TikTok or Instagram search for your customer's problem. Columns: `post_id, hook, views, likes, comments, shares, followers, days_live`. `sample_posts.csv` is **synthetic** example data for a knee-pain search, written for this repo.

It:
1. Scores each post by how far it beat its own audience (views ÷ followers), plus share rate and a little comment rate
2. Tags the hook *pattern* (body-spot callout, question, number/list, authority, contrarian, home remedy, testimonial, sensation)
3. Flags hooks that organic creators can post but advertisers often can't: implying the viewer's health condition (Meta's personal-attributes policy), unsupported health claims (FTC), and engagement bait
4. Prints a shortlist: one above-average, unflagged hook per pattern, to rewrite and test

It doesn't scrape anything. Collecting 20–50 posts by hand is safer than scraping (platform terms) and makes you actually watch them.

## winners_curse.py: do the top organic hooks make the best ads?

```bash
python3 winners_curse.py
```

A toy simulation. Each hook has hidden *appeal* (helps sales) and *bait* (wins views, hurts persuasion), and each post gets *reach* and *luck*. It compares picking hooks at random, by raw views, by views ÷ followers, and by a cheap paid test of a 20-hook shortlist, under three levels of bait. All parameters are illustrative.
