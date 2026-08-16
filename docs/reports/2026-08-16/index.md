---
layout: page
title: "Daily Scholar Papers Report — 2026-08-16"
date: 2026-08-16
permalink: /reports/2026-08-16/
---

# Daily Scholar Papers Report — 2026-08-16

**[Download PDF](Daily_Papers_Report_2026-08-16.pdf)**

**Window covered:** 2026-08-15 → 2026-08-16 (Google Scholar alerts + user-curated self-emails, last 24 h)

---

## Executive Summary

A thin window. Three alert threads, three distinct candidates, no self-curated papers. After yesterday's fifteen-candidate flood this is a return to the intake channel's normal behaviour, and it makes today a good day to read one paper properly rather than nine partially.

The one result worth the reader's time inverts a habit that has quietly settled over corpus-quality work. The standard move when you want to know what is wrong with a web-scale corpus is to build a classifier and run it over the corpus — which means paying for a full scan and accepting whatever taxonomy the classifier was trained on. **Sampled-BPE** does neither. It samples a small subset, trains a byte-pair-encoding tokenizer on it, and then reads the *tokenizer's own vocabulary* as the measurement. Tokens are merged because they are frequent; a polluted corpus therefore mints polluted tokens, and the vocabulary becomes a compressed, human-inspectable summary of what the corpus is actually made of. The cost profile that falls out of this is the headline: **148.4× faster and 35.8× less memory than the full-scan baseline, at 4.25 % relative error** on pollution-category estimates. The authors then spend that budget on breadth — 11 open Chinese corpora and 6 Chinese Common Crawl snapshots spanning 2021 to 2026 — and ship a hierarchical token dataset of 660k+ records so the findings can be re-examined rather than merely believed.

The transferable idea is not about Chinese text. It is that a tokenizer trained on a sample is a *cheap sufficient statistic* for corpus composition, and that the sampling error it introduces can be quantified rather than hand-waved. Anyone who has wanted to characterise a large code corpus, a crawl of package registries, or a scraped issue-tracker dump without a full pass over it should read the error analysis in this paper before building yet another classifier.

The second entry is noted rather than analysed. It arrives from a followed researcher and is therefore surfaced, but harness engineering for coding agents has become one of the most heavily written-in areas of 2026 — a search of the last six months returns a substantial body of overlapping practice-and-principle treatments — and no public full text or abstract was reachable for this one today. It is listed with its link so the reader can make their own call; this digest is not in a position to assess it.

One process note, stated plainly because it bounds everything above: both assessments today are **abstract-and-metadata reads**. Repeated HTTP 429 responses from the fetch layer meant no full text was retrieved, so no verbatim definitions, algorithms, or figures appear below. Every number quoted is the paper's own, taken from its abstract page.

**Outstanding:** 0 · **Keep:** 1 · **Borderline High-Priority:** 1

## Highlighted Papers

| Title | Authors | Venue | Link |
|---|---|---|---|
| Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics | Q. Zhang, Z. Tang, J. Zhang, G. Deng, J. Li, Y. Chen, Y. Yang, H. Xue, T. Zhang, H. Qiu | arXiv preprint (cs.CL; cs.AI), 2026 | [arXiv:2608.10678](https://arxiv.org/abs/2608.10678) |
| Harness Engineering for AI Coding Agents: Emerging Practices and Principles | H. Zheng, C. Wen, M. Sadiq, K. Sadatdiynov, J. A. Shamsi | IEEE international conference, 2026 | [IEEE Xplore 11634633](https://ieeexplore.ieee.org/abstract/document/11634633/) |

---

## Papers

<details class="paper-card" markdown>
<summary><strong>2.1</strong> · <span class="topic-chip">LLM DATA AUDITING</span> · Reading a sampled BPE vocabulary as the audit instrument: 148.4× speedup and 35.8× memory reduction for 4.25 % relative error, across 11 corpora and 6 Common Crawl snapshots<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-2.1+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots+%F0%9F%91%8D&body=paper_id%3A+2026-08-16-2.1%0Atitle%3A+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots%0Aauthors%3A+%2A%2AAuditing+Chinese+Web-scale+Corpora+via+Sampled+BPE+Token+Statistics%2A%2A%0Avenue%3A+preprint%0Atopic%3A+LLM+DATA+AUDITING%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-2.1+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots+%F0%9F%AB%A5&body=paper_id%3A+2026-08-16-2.1%0Atitle%3A+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots%0Aauthors%3A+%2A%2AAuditing+Chinese+Web-scale+Corpora+via+Sampled+BPE+Token+Statistics%2A%2A%0Avenue%3A+preprint%0Atopic%3A+LLM+DATA+AUDITING%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-2.1+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots+%F0%9F%94%96&body=paper_id%3A+2026-08-16-2.1%0Atitle%3A+Reading+a+sampled+BPE+vocabulary+as+the+audit+instrument%3A+148.4%C3%97+speedup+and+35.8%C3%97+memory+reduction+for+4.25+%25+relative+error%2C+across+11+corpora+and+6+Common+Crawl+snapshots%0Aauthors%3A+%2A%2AAuditing+Chinese+Web-scale+Corpora+via+Sampled+BPE+Token+Statistics%2A%2A%0Avenue%3A+preprint%0Atopic%3A+LLM+DATA+AUDITING%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics**

**Authors.** Qingjie Zhang, Ziqi Tang, Jie Zhang, Gelei Deng, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Tianwei Zhang, Han Qiu.

**Venue.** Preprint. `arXiv:2608.10678v1 [cs.CL]` (cross-listed cs.AI), submitted 11 August 2026. Abstract page: <https://arxiv.org/abs/2608.10678>. DOI: <https://doi.org/10.48550/arXiv.2608.10678>.

**Licence.** CC BY 4.0.

### The problem the paper picks

Corpus pollution stopped being a hypothetical the moment it started showing up in shipped tokenizers. Once a vocabulary contains tokens that only exist because a particular kind of spam was abundant in training data, the pollution is no longer upstream of the model — it is *inside* the model's input representation, and it is visible to anyone who cares to look. That observation is the lineage this paper comes from; the natural follow-up question is whether the same signal can be used deliberately, as an instrument pointed at a corpus you control, rather than forensically, as an inference about a corpus you do not.

The paper states three obstacles to doing that at web scale. The corpora are large enough that a full scan is expensive. Prior analyses operate at a granularity too coarse to expose pollution that lives at the token level. And the pollution itself is implicit and moves — what dominates a 2021 crawl is not what dominates a 2026 one.

### The design move

**Sampled-BPE** is described as a lightweight token-level auditing pipeline that samples a small subset of a corpus and trains a BPE tokenizer on it in order to surface polluted tokens.

The elegance is in what is *not* there. There is no classifier to train, no labelled pollution dataset to assemble first, and no full pass over the corpus. BPE's merge rule already does the work: sequences get promoted to tokens because they recur, so a vocabulary trained on a sample is a frequency-ranked, human-readable précis of what that sample is made of. Pollution that is abundant enough to matter is abundant enough to become a token. Pollution that is too rare to become a token is, by construction, too rare to shape the model much either.

This makes the tokenizer a *measurement instrument* rather than a preprocessing step, and it inherits two properties that classifiers do not have for free. It is taxonomy-free at collection time — you discover the categories from the vocabulary instead of committing to them in advance, which matters precisely because the pollution is described as rapidly changing. And its cost is governed by the sample size, not the corpus size, which is what makes the temporal study below affordable at all.

The obvious objection is that sampling introduces error, and the paper's answer is to measure it rather than argue about it.

### Headline numbers

Against the full-scan baseline, Sampled-BPE reports:

- **148.4×** speedup
- **35.8×** memory reduction
- **4.25 %** relative error on pollution-category estimates

Applied at scale, the audit covers:

- **11** open Chinese corpora
- **6** Chinese Common Crawl snapshots, spanning **2021 to 2026**

And the released artefact:

- a hierarchical Chinese web token dataset of **660k+** token records, each carrying web context, category, and explanation fields, organised as trees to support review and tracing of pollution

The findings are reported as widespread but *uneven* pollution across the open corpora, and Chinese web content that is both heavily polluted and temporally shifting.

### Why the ratio is the result

Two orders of magnitude of speedup for four percent of error is the kind of trade that changes what questions get asked. A full-scan audit is something a lab does once, on one corpus, and then cites for two years. An audit that costs 0.7 % of that is something you run on every snapshot, every quarter, on every corpus you are considering — which is exactly why this paper has a six-snapshot time series in it and its predecessors do not. The 4.25 % figure is not a concession; it is the price of the time axis.

The 660k-record release deserves separate credit for the same reason. Per-token web context and explanation fields mean a downstream reader can dispute an individual categorisation instead of having to accept or reject the aggregate. Corpus-quality work has a chronic reproducibility problem — the corpora are large, often licence-encumbered, and the interesting judgements are buried in an unpublished labelling pass. Shipping the token-level records with their provenance is the correct response to that, and the tree organisation is a sensible concession to the fact that nobody is going to read 660k rows flat.

### What a full read should press on

Three things, none of which the abstract settles.

**Sample design.** "Samples a small subset" is doing heavy lifting. Whether the sample is uniform over documents, stratified by source or domain, or something adaptive determines how much the 4.25 % figure travels — pollution is plausibly clustered by host, and uniform document sampling under clustering behaves differently from what a naive error model predicts. The relationship between sample size and error is the single most important curve in the paper.

**What "relative error on pollution categories" is relative to.** The baseline is presumably the full-scan BPE vocabulary over the same corpus, which makes the number a measure of *sampling fidelity* rather than of correctness against ground truth. Those are different claims and it matters which one is being made.

**Category assignment.** Tokens surface automatically; categories and explanations do not. If a model performed the labelling, its error rate propagates into every category-level statistic in the paper, and the temporal trends are only as trustworthy as the labelling is stable across snapshots.

**Assessment.** Kept, not elevated, and the reason is procedural rather than substantive: this is an abstract-and-metadata read, no full text was retrieved, and the digest's Outstanding bar asks for verbatim definitions and algorithms. On reported evidence the work is strong — a clean instrument, a quantified error budget, a temporal study that the instrument makes affordable, and an artefact that lets others check it. The method is the part to steal. Sampling plus a tokenizer as a sufficient statistic for corpus composition is language-agnostic and domain-agnostic, and there is no reason it would not work on a code corpus.

</details>

<details class="paper-card" markdown>
<summary><strong>3.1</strong> · <span class="topic-chip">AI CODING AGENTS</span> · Surfaced on a followed-author alert; a practices-and-principles treatment of the agent harness, in a topic area that has attracted heavy 2026 coverage<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-3.1+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage+%F0%9F%91%8D&body=paper_id%3A+2026-08-16-3.1%0Atitle%3A+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage%0Aauthors%3A+%2A%2AHarness+Engineering+for+AI+Coding+Agents%3A+Emerging+Practices+and+Principles%2A%2A%0Avenue%3A+preprint%0Atopic%3A+AI+CODING+AGENTS%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-3.1+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage+%F0%9F%AB%A5&body=paper_id%3A+2026-08-16-3.1%0Atitle%3A+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage%0Aauthors%3A+%2A%2AHarness+Engineering+for+AI+Coding+Agents%3A+Emerging+Practices+and+Principles%2A%2A%0Avenue%3A+preprint%0Atopic%3A+AI+CODING+AGENTS%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-16-3.1+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage+%F0%9F%94%96&body=paper_id%3A+2026-08-16-3.1%0Atitle%3A+Surfaced+on+a+followed-author+alert%3B+a+practices-and-principles+treatment+of+the+agent+harness%2C+in+a+topic+area+that+has+attracted+heavy+2026+coverage%0Aauthors%3A+%2A%2AHarness+Engineering+for+AI+Coding+Agents%3A+Emerging+Practices+and+Principles%2A%2A%0Avenue%3A+preprint%0Atopic%3A+AI+CODING+AGENTS%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Harness Engineering for AI Coding Agents: Emerging Practices and Principles**

**Authors.** Hua Zheng, Cheng Wen, Muhammad Sadiq, Kuanishbay Sadatdiynov, Jawwad Ahmed Shamsi.

**Venue.** 2026 IEEE international conference proceedings. <https://ieeexplore.ieee.org/abstract/document/11634633/>

### Why it is here

It reached this digest through a followed-author alert, which is a signal the pipeline treats as sufficient reason to surface a paper regardless of venue tier. The framing, from the alert text, is that reliability in LLM-based coding agents moving from prototype to production depends less on model capability than on the engineering of the surrounding environment — the now-common "everything in the agent except the model" reading of *harness*.

### Why it is only noted

Two reasons, both about this digest's evidence rather than about the work.

The first is access. No public abstract page, preprint, or full text was reachable for this record within the window; the fetch layer returned repeated rate-limit errors and no open-web mirror surfaced. Everything above comes from the three-sentence Scholar alert fragment, which is not enough to say anything useful about the contribution.

The second is field density. Harness engineering for coding agents has become a crowded area during 2026, with a considerable body of overlapping practice-and-principle treatments now in circulation, including large-scale empirical studies of configuration mechanisms across thousands of repositories. A contribution in this space is worth reading in proportion to what it adds over that body, and that comparison cannot be made from a snippet.

**Assessment.** Listed with its link so the reader can judge directly. Worth a look if the harness question is live for you and you have institutional access; this digest is not in a position to assess it and does not pretend otherwise.

</details>

---

## Cross-Paper Synthesis

With two papers there is no pattern to extract, so the honest synthesis is a single observation about method, drawn from the one paper that could be read.

Sampled-BPE belongs to a family of results that keeps recurring in this digest under different topic chips: **take an artefact that already exists for another purpose and read it as a measurement.** A BPE vocabulary exists to compress text; this paper reads it as a census of the corpus. The same shape appeared in recent windows in work that read an existing analysis engine's coverage record as evidence for planning, and in work that read API documentation as a grammar specification. In each case the win comes from *not building the obvious purpose-built artefact* — no pollution classifier here, no learned state-selector there — and instead noticing that something already in the pipeline encodes the needed signal for free.

The reason this pattern keeps paying is cost asymmetry. A purpose-built instrument has to be trained, validated, and maintained against distribution shift; a repurposed one inherits its maintenance from whatever it was originally for. When the thing being measured moves quickly — and "implicit and rapidly changing" is exactly how this paper characterises its target — the repurposed instrument's freedom from a fixed taxonomy is worth more than the accuracy a bespoke classifier would have bought.

The counterweight, and it is the same one every time: a repurposed instrument measures what it was built to measure, not what you want to know. A BPE vocabulary is a frequency statistic, so it sees abundant pollution well and rare pollution not at all. Whether that blind spot matters depends entirely on whether the harm you care about scales with frequency. For shaping a model's representations it largely does. For a security question — a small number of deliberately planted sequences, say — it largely does not, and the same instrument would report a clean corpus. The paper is measuring the former; a reader borrowing the method for the latter should notice the substitution.

## Writing & Rationale Insights

**Quantify the concession before anyone asks.** The strongest structural choice in today's read is that the speedup and the error are reported in the same breath: 148.4× and 35.8× *induce only* 4.25 % relative error. An approximation paper that leads with its speedup and buries its error invites the reader to assume the error is embarrassing. Putting the cost in the same sentence as the benefit converts a vulnerability into a stated exchange rate, and lets the reader evaluate the trade instead of hunting for the catch.

**Spend the savings visibly.** A cheap method is only interesting if it buys something. This abstract does not stop at the ratio; it immediately shows 11 corpora and a 2021–2026 time series, which is a study that would not exist at full-scan cost. That sequencing — here is the efficiency, here is the science it made possible — is a much stronger argument than the efficiency claim alone, and it is the part most efficiency papers omit.

**Release at the granularity of the disputable claim.** The 660k-record dataset carries context and explanation per token. That is a deliberate choice to make individual judgements contestable rather than shipping only aggregates that a sceptic can accept or reject wholesale. In a subfield where the underlying corpora are large and awkward to redistribute, releasing the *derived* records with provenance is often the only reproducibility move available — and it is more useful than a repository containing only code.

**When you cannot read it, say so and stop.** Today's second entry gets three paragraphs and no assessment, because a Scholar snippet does not support one. The alternative — writing confident-sounding summary prose from an abstract fragment — produces text that is indistinguishable from a real read and is therefore worse than silence. Marking the boundary of the evidence is part of the deliverable, not an apology for it.
