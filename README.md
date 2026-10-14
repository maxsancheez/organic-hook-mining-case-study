![cover](cover.svg)

# Mining Organic Hooks for Paid Ads

> **TL;DR:** The tip: if you need ad hooks, search TikTok for your customer's *problem* (not your product), study how the most-viewed videos open, and use those patterns in paid ads that look like regular posts. It's a solid way to *come up with* hooks, and the research on native-looking ads backs it up. But views aren't sales. In bait-heavy niches like health, the most-viewed hooks can convert worse than random ones, and a lot of them can't legally run as ads anyway. Rank by views relative to the creator's following, filter out what ads can't say, and let a cheap paid test pick the winners.

**Spark:** [Instagram reel by @markbuildsbrands](https://www.instagram.com/reel/DeM1R-loXgk/) · **Angle:** case study · **Date:** 2026-10-13

## The claim vs. reality

**What the reel says:** whatever you sell, figure out its niche and the problem it solves. Search TikTok for the problem (his example is knee pain), find the most-viewed videos, and study their hooks. He's clear that organic and paid are different (paid needs conversions, organic just needs views), but he says the openings that win attention organically carry over. Ads made that way look like normal posts in the feed, and he says it's made him good money. On screen he flashes an Ads Manager table with returns on ad spend of roughly 2.4–9.4× (dated Oct 2021–Feb 2022). Nothing ties those numbers to a specific hook, so treat it as an anecdote, not proof.

**What the comments said:** a performance marketer said digging through organic content before a brand's first campaign raised their win rate. Others asked how it works for static ads or a meal-prep business. One person pointed out that the comments under viral posts are free market research, and the research below backs that up.

**What the research says:**

| Claim | Evidence | Verdict |
|---|---|---|
| Hooks are where ads win or lose | Up to 47% of video campaign value in the first 3 seconds [1]; creative ~47% of sales lift [2] | ✅ Directionally right |
| Search the problem, study top organic hooks | TikTok sells the same idea as a tool (Creative Center, Keyword Insights) [3] | ✅ Good research habit |
| Ads that look like regular posts work better | Few people recognise native-style ads; recognition lowers evaluations [4] | ✅ Supported |
| Organic winners carry over to paid | Persuasiveness fell ~10% per million views in Tucker's study [5]; top picks are partly luck [6] | ⚠️ Partly. Depends on *why* the post got views |
| Copy what works | Many top health hooks break Meta policy or FTC claim rules [7][8]; copy patterns, not videos [9] | ⚠️ Filter first |

He's upfront that organic and paid want different things. What he skips is *how* to tell which organic winners will also sell, and which ones you can't run as ads at all.

## How it works

The idea splits the work between two channels. Organic is a giant free experiment in what grabs attention, with millions of people voting with their thumbs on thousands of hooks. Paid takes the winners and puts them in front of people who can buy.

```mermaid
flowchart LR
    A["Search the<br/>customer's problem"] --> B["Sort by views,<br/>adjust for reach"]
    B --> C["Tag the hook<br/>pattern"]
    C --> D["Rewrite with<br/>your footage"]
    D --> E["Cheap paid<br/>test"]
    E -->|"winners"| F["Scale"]
    style E fill:#cdeee6,color:#111
```

There are two filters along the way, and the reel only covers the first:

```mermaid
flowchart LR
    A["Organic<br/>winner"] --> B{"Views from<br/>appeal or bait?"}
    B -->|"appeal"| C{"Allowed<br/>in an ad?"}
    B -->|"bait"| X["Drops in<br/>paid"]
    C -->|"yes"| D["Good ad<br/>candidate"]
    C -->|"no"| Y["Rejected or<br/>risky claim"]
    style X fill:#e5e5e5,color:#111
    style Y fill:#e5e5e5,color:#111
```

## Deep dive

### 1. Why the hook matters so much

The first few seconds do a lot of the work. A 2016 Nielsen analysis commissioned by Facebook found that up to 47% of a video campaign's value came in the first three seconds, and up to 74% in the first ten [1]. That's a platform grading its own product, so take it as a rough guide. Across about 500 campaigns, the NCSolutions/Nielsen "Five Keys" study put about 47% of advertising's sales lift down to the creative, more than reach (22%) or targeting (9%) [2]. Creative is the biggest lever, and the hook is the biggest part of the creative. So better hooks are worth the effort.

### 2. Organic search is free creative research (TikTok agrees)

You type your customer's problem into TikTok search, look at what's most viewed, and study how those videos open. That's a manual version of something TikTok literally sells. Its Creative Center has a Top Ads library and a Keyword Insights tool that shows phrases from high-performing ads, how often each one's used and its average click-through rate [3]. TikTok has also told advertisers for years to make ads that look and feel like normal posts.

There's a good reason that works: ads that look organic are harder to spot as ads. In Wojdynski and Evans's experiments, only 7% of readers recognised a sponsored article as advertising in one study, and 17% in the other. And once people *did* spot it, they rated the content and the brand lower [4]. A hook that reads like a regular post slips past the "skip, it's an ad" reflex.

### 3. Views aren't the same as persuasion

He admits organic chases views and paid chases conversions, but he still treats winning hooks as if they transfer. The best evidence says that's only partly true.

- **Catherine Tucker (MIT)** tracked the reach of about 400 video ads and ran randomized persuasion tests with roughly 24,000 people. On average, ads got about **10% less persuasive for every million views**. Views won by being outrageous didn't make people want the product. The exceptions were ads with lots of comments, especially comments about the product, that got their views by being funny instead of shocking [5].
- **Big accounts inflate raw views.** 4 million views from a 600,000-follower account is less impressive than 1 million from a 50,000-follower account. Sort by raw views and you're partly sorting by creator size, which says nothing about the hook.
- **Luck inflates the winners.** Pick the top few out of hundreds and part of why they're on top is chance (timing, the algorithm). That part won't repeat. Airbnb's experimentation team saw the same "winner's curse" in A/B tests: the effects of winning experiments tend to get overestimated, systematically [6].

### 4. Organic creators can say things advertisers can't

In a health niche like knee pain, a lot of the most-viewed organic hooks would get your ad rejected or land you in legal trouble:

- **Meta's personal-attributes policy** doesn't let ads claim or hint that they know the viewer's health condition. Second-person lines like "your knee hurts?" are a common reason ads get rejected [7].
- **FTC health claims.** The FTC's 2022 Health Products Compliance Guidance says health benefit claims need competent and reliable scientific evidence, usually randomized controlled trials. Testimonials and anecdotes don't count, and hedging with "may help" doesn't fix a weak claim [8]. A home-remedy hook that goes viral organically turns into a claim you have to back up the moment you pay to promote it.
- **Copy the pattern, not the post.** Short phrases and ideas aren't protected by copyright [9], so a hook *pattern* ("Pain right here? Here's what it means") is fair game. Someone's actual video, voice and footage aren't.

### 5. What the code shows

**`hook_miner.py`** takes a set of posts you collect by hand (here, synthetic sample data for "knee pain"), ranks them by how far each one beat its own audience, tags the hook pattern and flags policy risks:

```
 #  score views/fol  views  hook
 1   1.36     12.7x   1.4M  Old remedy for achy knees grandma swore by  [health claim, bait]
 2   1.33     15.3x   2.3M  All you need is a lime and a spoon for achy knees  [health claim]
 3   1.18     36.7x   0.3M  I fixed my knee pain without surgery  [health claim]
 4   1.17     32.2x   2.9M  Doctors hate this knee trick  [bait]
 5   1.00     31.7x   0.4M  My husband had two knee replacements. Here is what helped  [health claim]
 ...
Only 5/10 of the most-VIEWED posts are in the top 10 by outlier score.
```

In this sample, **every one of the top five organic hooks is one you probably couldn't run as an ad**. Remedies, testimonials and bait do great organically for the same reasons they're risky in paid. What survives the filters is less exciting: a "where does it hurt?" question, a "2-minute routine," and a "this feels so good" hook. Authority hooks ("physio explains...") score low here partly because those accounts already have big followings, so their views look less surprising.

**`winners_curse.py`** simulates the whole thing. Every hook has hidden *appeal* (helps sales) and *bait* (wins views, hurts persuasion, per Tucker). You pick 5 out of 300 posts:

```
Scenario: no bait (views come only from real appeal)
  Random 5 hooks               CVR 1.07%      +0% vs random
  Top 5 by views (the reel)    CVR 1.66%     +55% vs random
  Top 5 by views/followers     CVR 1.90%     +79% vs random
  Shortlist 20, test, keep 5   CVR 2.16%    +103% vs random

Scenario: some bait (typical feed)
  Top 5 by views (the reel)    CVR 1.44%     +34% vs random
  Top 5 by views/followers     CVR 1.57%     +46% vs random
  Shortlist 20, test, keep 5   CVR 2.04%     +90% vs random

Scenario: heavy bait (health/outrage niches)
  Top 5 by views (the reel)    CVR 0.98%     -12% vs random
  Top 5 by views/followers     CVR 0.97%     -13% vs random
  Shortlist 20, test, keep 5   CVR 1.59%     +43% vs random

Winner's curse (no bait, reach removed): the top 5 hooks' organic edge is about 50% real appeal and 50% luck.
```

How to read it:
- **The reel's method works in most feeds.** Copying the top organic hooks beat random picks by 34–55%.
- **Adjusting for creator size is a free upgrade**: +79% instead of +55% in the clean case.
- **In bait-heavy niches it can backfire.** When views mostly come from provocation, the most-viewed hooks convert *worse* than random ones. Health is one of those niches.
- **A cheap test of a 20-hook shortlist wins in every scenario.** Organic data is great for coming up with candidates and pretty bad at telling you which ones will sell.

## Apply it

```bash
python3 code/hook_miner.py
python3 code/winners_curse.py
```

Using it on your own niche:

1. **Search the problem, not the product.** Type what your customer would search when they've got the problem ("knee pain," "dog pulls on leash," "meal prep for the week"), on TikTok and Instagram.
2. **Log 20–50 posts by hand** into a CSV with views, likes, comments, shares, follower count and the hook (first line or on-screen text). Run `hook_miner.py my_posts.csv`.
3. **Rank by views ÷ followers, not raw views.** A small account with a huge post is the best sign the hook did the work.
4. **Read the comments on the winners.** Comments about the problem, or "where do I get this?", mean it persuaded people. Arguments and jokes usually mean bait (Tucker's comment finding).
5. **Rewrite, don't repost.** Keep the pattern, use your own words and footage, and drop anything that implies the viewer's condition or makes a claim you can't back up.
6. **Test before you scale.** Run 10–20 hooks on the same body and offer, with a small budget each. Judge them on cost per purchase, not just thumb-stop rate, then put your money behind the top few.

## Assumptions

| Parameter | Value | Anchored to |
|---|---|---|
| Sample posts (`sample_posts.csv`) | 24 knee-pain hooks | Synthetic, written for this repo; not real TikTok data |
| Hook score weights | outlier 1.0, share rate 0.5, comment rate 0.25 | Illustrative. Comments weighted lightly because they can mean outrage [5] |
| Posts scanned / hooks picked | 300 / 5 | Illustrative guess |
| Reach SD / luck SD | 1.2 / 1.0 | Illustrative. Creator size varies more than algorithm luck |
| Bait penalty on paid persuasion | 0.6 × bait | Direction from Tucker's ~10% loss per million views [5]; size is a guess |
| Paid test noise | 0.5 SD | Illustrative small-budget test |
| Base conversion rate | 1.0% | Illustrative |
| Bait levels | 0 / 0.7 / 1.5 | Illustrative scenarios |

## Takeaways

- Searching your customer's problem is a free, massive hook experiment. Use it to come up with candidates.
- Rank by views relative to the creator's following, not raw views, and read the comments to tell real appeal from bait.
- Views aren't sales. Going viral can cost you persuasion, especially in health and outrage niches.
- A lot of the best organic hooks can't run as ads, legally or by platform policy. Filter out "you have X" phrasing and claims you can't back up.
- Copy the pattern, not the post, and let a cheap paid test pick the winners.

## Open questions

- How well do organic views actually predict paid results? There's no public dataset that pairs the two for the same hooks.
- Does Tucker's reach-versus-persuasion trade-off hold for short-form vertical video in 2026? Her data was from earlier video ads.
- How quickly does a copied hook pattern wear out once many advertisers use it?
- Do TikTok's Keyword Insights CTR numbers predict conversions, or only clicks?

## Sources

1. [Facebook and Nielsen (2016), video ad value in the first seconds, via Facebook Newsroom](https://about.fb.com/es/news/2016/02/capta-la-atencion-con-nuevas-funcionalidades-para-anuncios-de-video/): up to 47% of campaign value in the first 3 seconds; platform-commissioned
2. [NCSolutions/Nielsen "Five Keys to Advertising Effectiveness," as reported by Inside Radio](https://www.insideradio.com/free/reach-creative-drive-nearly-70-of-sales-more-than-twice-ad-industry-perception/article_47b93892-ff24-11eb-80de-1beb2f9e01ea.html): creative ~47% of sales lift (reported; original report not public)
3. [TikTok Keyword Insights launch, Social Media Today](https://www.socialmediatoday.com/news/TikTok-Adds-Keyword-Insights-for-Marketers/644491/): phrases from top ads with usage and average CTR
4. [Wojdynski & Evans (2016), "Going Native," *Journal of Advertising* 45(2)](https://doi.org/10.1080/00913367.2015.1115380): few readers recognise native ads; recognising them lowers evaluations
5. [Tucker (2015), "The Reach and Persuasiveness of Viral Video Ads," *Marketing Science* 34(2)](https://doi.org/10.1287/mksc.2014.0874): ~10% lower persuasiveness per million views
6. [Lee & Shen (2018), "Winner's Curse: Bias Estimation for Total Effects of Features in Online Controlled Experiments," KDD](https://doi.org/10.1145/3219819.3219905): winning experiments' effects are overestimated
7. [Meta personal attributes policy, summarised by Accelerated Digital Media](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/): ads can't imply knowledge of a viewer's health condition
8. [FTC, "FTC Announces New Business Guidance for Marketers and Sellers of Health Products" (Dec 2022)](https://www.ftc.gov/news-events/news/press-releases/2022/12/ftc-announces-new-business-guidance-marketers-sellers-health-products): health claims need competent and reliable scientific evidence
9. [U.S. Copyright Office Circular 33](https://www.copyright.gov/circs/circ33.pdf): names, titles, short phrases and ideas aren't protected by copyright

---
*Assumptions:* the sample data and simulation numbers are illustrative, not measured. I summarised the reel in my own words. No transcript is reproduced here.
