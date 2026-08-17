---
layout: page
title: "Daily Scholar Papers Report — 2026-08-17"
date: 2026-08-17
permalink: /reports/2026-08-17/
---

# Daily Scholar Papers Report — 2026-08-17

**[Download PDF](Daily_Papers_Report_2026-08-17.pdf)**

**Window covered:** 2026-08-16 → 2026-08-17 (Google Scholar alerts + user-curated self-emails, last 24 h)

---

## Executive Summary

Four alert threads, twelve distinct candidates — the widest window in a fortnight, and for once the width is real rather than an artefact of one noisy recommendation thread. Three followed researchers each fired, and the profile-recommendation thread carried eight items, six of them fuzzing.

One paper is worth clearing an afternoon for. **SRE-Bench** asks a question that sounds procedural and turns out to be foundational: what does it actually cost to build an agentic benchmark whose targets cannot have been memorised? The answer is 19 clean-room programs averaging **16,915.8 lines of code**, a from-scratch **44-primitive** anti-analysis suite in **27K lines**, over **320,000** lines of authored code total, and more than **5,000 domain-expert hours**. That is an uncomfortable number, and the paper's most valuable contribution is the ablation that proves it was necessary. A clean-room compressor of ~1.1k LoC is solved perfectly by both tested models in every build configuration for under **$1.60**. The real gzip encoder, with roughly **200 lines** of its critical path rewritten, is *also* solved in all eight configurations for roughly **$2** — as cheaply as the toy. Only the program that is simultaneously clean-room *and* real-world-scale separates the models at all, at **10–30×** the cost. Cheap contamination control and cheap realism each independently collapse the measurement; you need both or you have measured nothing.

The result that will change how people read agent evaluations is the build-factor ablation, and it inverts the human difficulty ordering outright. Compiler optimisation — the thing that makes a human reverse engineer's day miserable — costs the strongest model **0.08** points out of 6. Static linking costs it **0.04**. Symbol stripping, which a human treats as an annoyance, costs it **0.48**, and costs a weaker model more than half its total score (**2.53 → 1.14**). The reading offered is that current agents lean on lexical anchors — names they can reason about in natural language — far more than on the instruction-level analysis that optimisation degrades. The one classical obstacle that does transfer is protection: hardening halves the leader (**4.69 → 2.50**) and takes the runner-up from **3.07 to 0.33**, flattening a wide capability ranking into near-uniform failure. Anyone building an agentic-analysis evaluation should read Figure 3 before choosing their difficulty axes, because three of the four axes they would instinctively reach for are nearly free.

The window's second substantive entry, **RealisticTritonBench** (accepted at ASE 2026), makes an argument with the same shape in a different domain: that benchmark realism is a property of the *evaluation harness*, not just the task. It mines Triton-kernel-modifying pull requests from real AI frameworks, then scores generated kernels by integrating them back into the originating framework and running its own end-to-end tests — displacing the hand-written per-kernel scripts whose flaws, the paper argues, models can exploit to bypass correctness checks and inflate scores. Two independent papers arriving the same day and identifying benchmark-harness gameability as the thing to fix is not a coincidence worth ignoring.

Two further entries arrive from a followed researcher and are surfaced with links rather than analysed: a USENIX Security 2026 paper on missing permission controls in mini-program APIs, and a formal-methods treatment of association-based privacy attacks in Wi-Fi P2P and BLE reconnection. Both look substantial; neither could be read today.

One process note that bounds everything except the lead paper. Repeated **HTTP 429** responses from the fetch layer — the third consecutive day — meant full text was retrieved for exactly one paper. Entry 2.1 is a genuine full-text read and its numbers are the paper's own, verbatim. Entries 2.2 through 3.3 are abstract-and-metadata reads, and are written to that standard: no verbatim definitions, no algorithms, no figures, and no formal notation appears for them, because none was available in the papers' own text. Nothing below is a paraphrase dressed up as a formula.

**Outstanding:** 1 · **Keep:** 1 · **Borderline High-Priority:** 2

## Highlighted Papers

| Title | Authors | Venue | Link |
|---|---|---|---|
| The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark | J. Spence, N. Assaderaghi, J. Zhu, N. Ravi, R. A. Popa, G. Wei, Y. Ding, Z. Zhang | arXiv preprint (cs.CR), 2026 | [arXiv:2608.11469](https://arxiv.org/abs/2608.11469) |
| RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks | J. Huang, Z. Wen, T. Xu, M. Yan, X. Xia, Z. Liu | ASE 2026 (accepted); arXiv preprint (cs.SE) | [arXiv:2608.12004](https://arxiv.org/abs/2608.12004) |
| Association-based Privacy Attacks in Wireless Protocols: Formal Modeling and Mitigation | M. K. Jangid, F. Engelmann, Z. Lin | arXiv preprint (cs.CR; cs.NI), 2026 | [arXiv:2608.11337](https://arxiv.org/abs/2608.11337) |
| Raising the Flag: Detecting Missing Permission Controls in Mini-Program APIs | Y. Aafer, Z. Lin (author list truncated in alert) | USENIX Security 2026 | [USENIX Security 2026](https://www.usenix.org/conference/usenixsecurity26) |
| Harnessing LLMs for Document-Guided Fuzzing of Python Libraries | B. Duan, T. Mahmud, M. Che, Y. Yan, N. Dong, D. D. Kim, et al. | arXiv preprint, 2026 | [arXiv:2608.11744](https://arxiv.org/abs/2608.11744) |
| Testing Deep Learning Library APIs via Cross-Framework Differential Fuzzing | B. Duan, R. Dong, N. Dong, D. D. Kim, G. Yang | arXiv preprint, 2026 | [arXiv:2608.11886](https://arxiv.org/abs/2608.11886) |
| ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments | Z. Wu, C. Nita-Rotaru | arXiv preprint, 2026 | [arXiv:2607.24964](https://arxiv.org/abs/2607.24964) |

---

## Papers

<details class="paper-card" markdown>
<summary><strong>2.1</strong> · <span class="topic-chip">BINARY RE BENCHMARK</span> · Contamination control costs 5,000 expert hours — and the ablation proves every one was load-bearing: 262 instances, 1,572 graded tasks, best model 3.69/6<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.1+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-2.1%0Atitle%3A+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6%0Aauthors%3A+Jeremy+Spence%2C+Nicholas+Assaderaghi%2C+Jinhao+Zhu%2C+Nikil+Ravi%2C+Raluca+Ada+Popa%2C+Guannan+Wei%2C+Yangruibo+Ding%2C+Zhuo+Zhang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+BINARY+RE+BENCHMARK%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.1+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-2.1%0Atitle%3A+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6%0Aauthors%3A+Jeremy+Spence%2C+Nicholas+Assaderaghi%2C+Jinhao+Zhu%2C+Nikil+Ravi%2C+Raluca+Ada+Popa%2C+Guannan+Wei%2C+Yangruibo+Ding%2C+Zhuo+Zhang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+BINARY+RE+BENCHMARK%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.1+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6+%F0%9F%94%96&body=paper_id%3A+2026-08-17-2.1%0Atitle%3A+Contamination+control+costs+5%2C000+expert+hours+%E2%80%94+and+the+ablation+proves+every+one+was+load-bearing%3A+262+instances%2C+1%2C572+graded+tasks%2C+best+model+3.69%2F6%0Aauthors%3A+Jeremy+Spence%2C+Nicholas+Assaderaghi%2C+Jinhao+Zhu%2C+Nikil+Ravi%2C+Raluca+Ada+Popa%2C+Guannan+Wei%2C+Yangruibo+Ding%2C+Zhuo+Zhang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+BINARY+RE+BENCHMARK%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark**

**Authors:** Jeremy Spence, Nicholas Assaderaghi, Jinhao Zhu, Nikil Ravi, Raluca Ada Popa, Guannan Wei, Yangruibo Ding, Zhuo Zhang.

**Venue:** arXiv preprint

**Affiliations.** Columbia University (Spence, Assaderaghi, Zhang), UC Berkeley (Zhu, Popa), Vals AI (Ravi), Tufts University (Wei), UCLA (Ding). `arXiv:2608.11469v1 [cs.CR]`, submitted 11 August 2026. Abstract page: <https://arxiv.org/abs/2608.11469>.

**Licence.** CC BY 4.0.

**Provenance.** Full-text read (HTML rendering). The capture truncates inside Appendix A.4; Appendix A.5 and all of Appendix B — including the per-preset protection results and a section titled "Anti-Agent Deterrents: A Reported Negative Result" — were not available and are not summarised here.

### The problem, stated more sharply than usual

The motivating statistics are worth having at hand: **46.5 %** of vulnerabilities exploited in the wild come from vendors that do not release source code (CISA KEV catalogue), Google reports **more than 48 %** of 2025's zero-days targeted proprietary enterprise software, and roughly **732,000** new malicious samples surface daily. Agents are improving fast on source-available security tasks. Whether that transfers to binaries is an empirical question nobody could answer, because the benchmarks did not exist.

The paper's contribution to *why* they did not exist is the part worth internalising. Contamination in reverse engineering is categorically unlike contamination elsewhere. In most tasks only fine-grained leakage matters; here, the authors argue, even coarse leakage is damaging, because recognising a target's high-level purpose supplies top-down guidance that lets a model skip most of the program-understanding work. The corollary is unforgiving: locally modifying an open-source project does not help, because its architecture stays recognisable.

That collides head-on with the second requirement. Difficulty in RE comes from the program's scale and from the protection layer gating access to it, and real targets have both. Prior RE-centric benchmarks average **526.2**, **63.5**, and **36.1** lines of code respectively; SRE-Bench averages **16,915.8**, or **30–470×** larger. Realistic artefacts are normally derived from open source — which contamination control excludes. Clean-room construction is the only remaining route, and it is brutally expensive.

### The ablation that justifies the expense

Most benchmark papers assert their design requirements. This one tests them, using the same eight unhardened build configurations of one compression task across three programs:

| Program | Model | Score (of 6) | Solved | Cost ($) | Time (min) |
|---|---|---|---|---|---|
| Minimal (~1.1k LoC, clean-room) | gpt-5.6-sol | 6.00 | 8/8 | 0.90 | 4.5 |
| Minimal | gpt-5.5 | 6.00 | 8/8 | 1.60 | 7.0 |
| Gzip-variant (~200 lines of critical path modified) | gpt-5.6-sol | 6.00 | 8/8 | 2.19 | 9.9 |
| Gzip-variant | gpt-5.5 | 6.00 | 8/8 | 2.78 | 10.8 |
| RevCompress (clean-room + real-world scale) | gpt-5.6-sol | 5.62 | 7/8 | 31.45 | 94.6 |
| RevCompress | gpt-5.5 | 3.75 | 3/8 | 24.37 | 97.4 |

Read the middle two rows carefully. A *real* gzip encoder with two hundred lines of its critical path rewritten is recovered as cheaply as a 1.1k-line toy. The paper's conclusion is blunt and, on this evidence, correct: recognition substitutes for analysis, so a publicly derived program is no harder than a private toy. Only the bottom pair — clean-room *and* at scale — separates the models, at 10–30× the cost.

This is the most transferable thing in the paper, and it generalises well past reverse engineering. Any benchmark built by lightly perturbing public artefacts is measuring recall with extra steps, and the cost of finding that out is one small ablation.

### Construction

Nineteen programs across five domains and four languages (C, C++, Rust, Go), each written from scratch by security experts averaging six years of RE experience, against a private design specification that is never released. No two programs share source; none derives from a public project. Every program ships a private reference solution scoring a perfect 6/6, which functions as both a solvability proof and a regression gate.

Table 3's column semantics, verbatim: "Target is what the program does"; "RE Task is what the agent must accomplish"; "Infrastructure is the component that makes evaluation deterministic"; "Auxiliary is what the agent receives beyond the binary."

| Domain | RE task | Determinism mechanism | Programs |
|---|---|---|---|
| Network protocol | Recover the wire format, drive a client through the full state machine | Live server scoring state-machine coverage, one metered TCP connection capped at 64 messages | 4 |
| Game | Trigger hidden behaviours unreachable through normal play | Egg verifier replaying the agent's action trace | 4 |
| File format | Reverse the encoder; decode archives byte-exactly | Held-out decoder round-trip against the developed encoder | 4 |
| Malware | Reverse a synthetic implant's effects while preserving benign user data | Sandboxed infection-and-cleanup grader | 4 |
| Firmware | Take progressively fuller control of a locked-down secure MCU | Held-out emulator modelling chip and peripherals | 3 |

Total authored code is **321,401** lines. The protection suite is a separate artefact: **over 27K lines** of Python, C and assembly implementing, verbatim, "44 distinct primitives organized into nine technique families" — obfuscation and string deception (5), per-page authenticated encryption (4), lazy decryption and residency minimisation (5), measurement-keyed anti-debugging (8), self-checksumming and anti-tamper coupling (3), online licensing with per-run key delivery (4), loader-logic virtualisation (6), anti-dump detection and deception (5), anti-re-hosting (4). More than half are claimed to have no publicly available implementation. The suite is written from scratch so that the protection layer is as contamination-free as the programs it wraps — a detail that is easy to skip and is in fact essential to the design's internal consistency.

Sixteen Linux programs yield 8 unprotected build variants (optimisation × stripping × static/dynamic) plus 8 protected presets each; firmware, being bare-metal, cannot use the Linux-loader-dependent suite and varies only by optimisation level. **262 instances**, six deterministically scored tasks each, **1,572 tasks**.

The adversarial-audit loop deserves a mention, because it is the part most benchmark papers omit. Claude Opus 4.8 was run against the benchmark specifically to find reward hacks, and the findings drove iterative hardening. One documented catch: an early build retained a hidden behaviour's internal name as a readable string, and an agent found the trigger by scanning strings rather than reversing anything. The string was removed and a build-time regression check now fails the build on any similar leak. In the malware domain, audit findings killed the "delete everything" cleanup shortcut by making scoring conjunctive — credit per family only if the tool removes malicious state, *preserves* grader-planted benign state, and durably neutralises the behaviour.

### Metrics

Defined in prose, not notation. Verbatim: "Score, the mean rubric score over the six tasks of an instance (0–6)"; "Solve, the number of instances fully recovered (6/6)"; "Zero, the number that earn no credit at all"; "Graded is the number of runs that produced a gradeable result." The rationale for reporting Solve and Zero alongside the mean is that the distribution piles up at both ends, so the mean alone under-describes an agent.

**The paper contains no formal equations, no numbered display equations, and no algebraic scoring formulas.** Every mathematical symbol in the text is typographic (×, ⊕, ±, ↑, ↓) or a bare numeral. Per this digest's formula-integrity rule, none is invented here.

### Results

Five frontier models under a standardised mini-SWE-agent harness whose only tool is bash, at maximum reasoning effort, capped at 500 model steps and six hours per run, in per-instance containers carrying Ghidra, radare2, GDB, angr, binutils, strace and ltrace plus per-domain additions.

| Model | Graded /262 | Score ↑ (of 6) | Solved ↑ | Zero ↓ | Calls | Cost ($) | Time (min) |
|---|---|---|---|---|---|---|---|
| gpt-5.6-sol | 254 | **3.69** ± 0.14 (61.4 %) | 80 (31.5 %) | 41 (16.1 %) | 196 | 42.5 | 88.1 |
| claude-opus-5 | 256 | 1.91 ± 0.14 (31.8 %) | 32 (12.5 %) | 118 (46.1 %) | 139 | 23.6 | 81.0 |
| gpt-5.5 | 262 | 1.02 ± 0.10 (17.1 %) | 10 (3.8 %) | 148 (56.5 %) | 128 | 17.8 | 46.5 |
| grok-4.5 | 218 | 0.45 ± 0.07 (7.6 %) | 2 (0.9 %) | 160 (73.4 %) | 115 | 13.4 | 65.7 |
| glm-5.2 | 262 | 0.21 ± 0.03 (3.4 %) | 0 (0.0 %) | 217 (82.8 %) | 143 | 26.6 | 149.3 |

The full sweep cost **$31.4K** and **1,812 sandbox-hours**. The leader scores **1.9×** the next model and **17×** the last. Note the efficiency inversion in the bottom two rows: one model spends more per instance than another (**$26.6** vs **$17.8**) for roughly a fifth of the score — a reminder that cost and capability are not monotonically related on long-horizon tasks.

### The finding that should change practice

Difficulty axes, measured on the 128 unhardened instances (first three) and with build held fixed for the fourth:

- **Optimisation:** costs the leader **0.08** points.
- **Static linking:** costs the leader **0.04** points. No model moves by more than **0.39** on either axis.
- **Symbol stripping:** costs the leader **0.48** points, and costs gpt-5.5 more than half its score (**2.53 → 1.14**).
- **Protection:** halves the leader (**4.69 → 2.50**) and takes claude-opus-5 from **3.07 to 0.33**.

Three of the four obstacles a human reverse engineer would rank as hardest are almost free for an agent; the one that a human treats as an inconvenience — missing names — is the one that bites. The paper's interpretation is that agents lean on lexical anchors that let them label structure and reason in natural language, far more than on the instruction-level analysis that optimisation degrades. Protection is the exception that transfers, and it flattens the ranking: at the hardened end, a benchmark that cleanly separated five models stops separating them at all.

Source language matters much less than one might expect — only **0.85** points of spread for the leader (**4.24** on C, **3.39** on Go), attributed to decompilers being tuned for C-like output. Domain separates models roughly three times as strongly: the leader ranges from **4.88** on network protocol to **2.06** on malware, with weaker models collapsing to **0.34 and below** on malware because its conjunctive scoring gives partial understanding no credit at all. Aggregate scores hide *which kind* of program understanding an agent lacks, which is an argument for reporting per-domain breakdowns as a default rather than an appendix.

### Limitations, as stated

Benchmark breadth is the acknowledged one: 19 programs is a small pool, and firmware in particular yields only six instances from three programs. The authors argue the constraint is inherent rather than incidental — the cheap routes to breadth are exactly the ones their own ablation invalidates. Worth adding from the results table: **44 of 262** runs were lost for one model to context-window exhaustion, so its averages rest on a materially smaller and possibly non-random subset, and ungradeable runs (refusals on cyber-security grounds, plus overflows) are excluded from all averages. The paper also anticipates entering future training corpora, and masks instance-specific secrets, substitutes stand-ins for named critical algorithms, and verifies with a smaller model over 200 requests that everything disclosed is recoverable from the binaries anyway.

### Why it is worth your time

Because the transferable content is methodological and applies to any agentic benchmark you might build or trust. Three claims travel: recognition substitutes for analysis, so contamination control that stops at perturbation measures nothing; the difficulty axes that are expensive for humans may be free for agents, so difficulty must be measured rather than assumed; and an adversarial reward-hacking audit belongs in benchmark construction, not in the post-hoc discussion of why the numbers looked odd.

Closing line, verbatim: "Together these results suggest that strong source-code security performance is not yet a reliable indicator of binary-level capability, and that the gap is wide enough to be worth measuring on its own terms."

**Figure note.** Figure 1 (the construction-and-evaluation pipeline, including the adversarial-audit loop) is the natural embed and is CC BY 4.0. It is not reproduced here: the fetch layer was rate-limited and the harness forbids retrieving it by other means. Figures 2 (per-model heatmap by language and domain) and 3 (build-factor panels) exist as captions only in the available capture.

</details>

<details class="paper-card" markdown>
<summary><strong>2.2</strong> · <span class="topic-chip">GPU KERNEL GENERATION</span> · Mining real Triton-kernel pull requests and grading by re-integration into the originating framework, because per-kernel scripts can be gamed for inflated scores<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.2+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-2.2%0Atitle%3A+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores%0Aauthors%3A+Jinjun+Huang%2C+Zhongzhen+Wen%2C+Tongtong+Xu%2C+Meng+Yan%2C+Xin+Xia%2C+Zhongxin+Liu.%0Avenue%3A+ASE+2026+%28accepted%29%0Atopic%3A+GPU+KERNEL+GENERATION%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.2+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-2.2%0Atitle%3A+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores%0Aauthors%3A+Jinjun+Huang%2C+Zhongzhen+Wen%2C+Tongtong+Xu%2C+Meng+Yan%2C+Xin+Xia%2C+Zhongxin+Liu.%0Avenue%3A+ASE+2026+%28accepted%29%0Atopic%3A+GPU+KERNEL+GENERATION%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.2+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores+%F0%9F%94%96&body=paper_id%3A+2026-08-17-2.2%0Atitle%3A+Mining+real+Triton-kernel+pull+requests+and+grading+by+re-integration+into+the+originating+framework%2C+because+per-kernel+scripts+can+be+gamed+for+inflated+scores%0Aauthors%3A+Jinjun+Huang%2C+Zhongzhen+Wen%2C+Tongtong+Xu%2C+Meng+Yan%2C+Xin+Xia%2C+Zhongxin+Liu.%0Avenue%3A+ASE+2026+%28accepted%29%0Atopic%3A+GPU+KERNEL+GENERATION%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks**

**Authors:** Jinjun Huang, Zhongzhen Wen, Tongtong Xu, Meng Yan, Xin Xia, Zhongxin Liu.

**Venue:** ASE 2026 (accepted)

**Identifiers.** `arXiv:2608.12004v1 [cs.SE]`, cross-listed cs.AI, submitted 12 August 2026. Abstract page: <https://arxiv.org/abs/2608.12004>. DOI: <https://doi.org/10.48550/arXiv.2608.12004>.

**Licence.** CC BY 4.0.

**Provenance.** Abstract-and-metadata read. Full text was not retrievable (HTTP 429, repeated). No construction counts, no metric definitions, no results tables and no figures are reported below, because none were available. Everything here comes from the paper's own abstract page.

### The argument

Triton occupies a specific niche — usability and portability at close to hand-written CUDA performance — which is why it has become the default for expressing GPU kernels, and why automating its generation is worth benchmarking. The paper's claim is that existing benchmarks measure the wrong thing three times over.

First, **task scope**: prior benchmarks restrict tasks to PyTorch-to-Triton translation, which does not reflect the diversity and complexity of real Triton work. Translation is a well-posed problem with a reference answer sitting right there; real kernel work starts from a requirement and an engineering context.

Second, **granularity**: they evaluate individual-kernel performance rather than end-to-end performance, which the paper names as the core criterion for real-world deployment. A kernel that benchmarks beautifully in isolation and regresses the framework it lives in has not helped anyone.

Third — and this is the observation that makes the paper interesting beyond its domain — **harness integrity**: prior benchmarks rely on manually written per-kernel evaluation scripts, and those scripts may contain flaws that models can exploit to bypass correctness checks and obtain inflated scores. The evaluation apparatus is itself an attack surface.

### The design

Tasks are derived from real pull requests that modify Triton kernels in popular open-source AI frameworks, systematically extracted and transformed into generation tasks carrying concrete engineering context. Each task takes a natural-language requirement as input and demands a corresponding Triton kernel implementation, shipped with a complete and reproducible evaluation environment. Generated kernels are then integrated back into their originating framework and evaluated with that framework's end-to-end tests.

The move worth noting is that the third problem is answered structurally rather than by writing more careful scripts. If the oracle is the framework's own test suite, there is no bespoke per-kernel script to contain an exploitable flaw. Whether the paper argues this explicitly is unknown — the abstract states the problem and states the design, and leaves the connection to the reader.

Headline result, at the level available: leading LLMs were evaluated and still struggle with real-world Triton kernel generation tasks. No pass rates, model names, speedups or comparisons against prior Triton benchmarks could be recovered today.

### Why it is worth your time

Because of the harness argument, which is domain-independent. Benchmark scores are only as trustworthy as the code that produces them, and hand-written per-instance oracles are a systematic and under-examined source of inflation. Reusing an existing project's own tests as the oracle is a cheap structural fix that transfers directly to code-generation benchmarks well outside GPU kernels. That it lands the same day as a paper that ran an explicit adversarial reward-hacking audit against its own grader (2.1) is a reasonable signal about where benchmark methodology is heading.

Worth revisiting once full text is reachable — the construction counts and the reward-hacking discussion are exactly the parts that were unavailable.

</details>

<details class="paper-card" markdown>
<summary><strong>2.3</strong> · <span class="topic-chip">PROTOCOL VERIFICATION</span> · Formalising the root causes of pairing-based privacy leaks in Wi-Fi P2P persistent groups and BLE reconnection, with three composable countermeasures<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.3+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-2.3%0Atitle%3A+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures%0Aauthors%3A+Mohit+Kumar+Jangid%2C+Felix+Engelmann%2C+Zhiqiang+Lin.%0Avenue%3A+arXiv+preprint%0Atopic%3A+PROTOCOL+VERIFICATION%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.3+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-2.3%0Atitle%3A+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures%0Aauthors%3A+Mohit+Kumar+Jangid%2C+Felix+Engelmann%2C+Zhiqiang+Lin.%0Avenue%3A+arXiv+preprint%0Atopic%3A+PROTOCOL+VERIFICATION%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.3+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures+%F0%9F%94%96&body=paper_id%3A+2026-08-17-2.3%0Atitle%3A+Formalising+the+root+causes+of+pairing-based+privacy+leaks+in+Wi-Fi+P2P+persistent+groups+and+BLE+reconnection%2C+with+three+composable+countermeasures%0Aauthors%3A+Mohit+Kumar+Jangid%2C+Felix+Engelmann%2C+Zhiqiang+Lin.%0Avenue%3A+arXiv+preprint%0Atopic%3A+PROTOCOL+VERIFICATION%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Association-based Privacy Attacks in Wireless Protocols: Formal Modeling and Mitigation**

**Authors:** Mohit Kumar Jangid, Felix Engelmann, Zhiqiang Lin.

**Venue:** arXiv preprint

**Identifiers.** `arXiv:2608.11337 [cs.CR]`, cross-listed cs.NI, submitted 11 August 2026. Abstract page: <https://arxiv.org/abs/2608.11337>.

**Provenance.** Abstract-and-metadata read, and a thinner one than 2.2 — repeated HTTP 429 responses meant neither the HTML nor the abstract page could be fetched directly, and the summary below rests on search-index metadata for the abstract. No verification tool, no lemma counts, no formal notation, and no property definitions are reported, because none could be read in the paper's own text. Treat this entry as a pointer, not an assessment.

### What the paper appears to address

The setting is authenticated *reconnection*: protocols where two devices that have paired before recognise each other later using a shared key held in an allowlist. That convenience is the vulnerability. A device that responds differently depending on whether it recognises the peer leaks, to any passive or replaying observer, the fact that a prior association exists — which is a linkability and tracking primitive even when no content is exposed.

The paper is described as formally investigating the root sources of these pairing-based privacy threats as exploited through replay and relay techniques, rather than cataloguing individual bugs. Three countermeasures are named as the ingredients that matter for allowlist-based authenticated reconnection: **condition-oblivious responses** (behave identically whether or not the peer is recognised, so there is nothing to observe), **replay-resistance**, and **distance bounding** (which addresses relay rather than replay). The proposed solution is stated as being validated against association-inference attacks alongside existing formalisations of *well-authentication*, *frame opacity*, and *no-desynchronization*.

Two protocols carry the argument: Wi-Fi P2P persistent group formation and the Bluetooth Low Energy reconnection procedure.

### Why it is on the list

Two reasons. The first is that the framing — deriving a general root cause and a reusable countermeasure set, then instantiating on two independent real protocols — is the shape of protocol-analysis work that stays useful after the specific protocols are patched. The second is that condition-oblivious response is a design discipline, not a wireless trick: any system that answers differently for known and unknown principals is leaking membership, and that pattern recurs in API authentication, caching layers, and error-message design. If the paper gives it a formal treatment with a mechanised proof, that is worth having.

Whether it does is precisely what could not be verified today. The property names cited above are the abstract's, reported as such; no definition, predicate or lemma from the paper is reproduced here, and none is invented.

</details>

<details class="paper-card" markdown>
<summary><strong>2.4</strong> · <span class="topic-chip">PERMISSION ANALYSIS</span> · Missing permission checks in the super-app API layer that mini-programs sit on — surfaced from a followed researcher, listed for the reader's own call<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.4+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-2.4%0Atitle%3A+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call%0Aauthors%3A+Y.+Aafer%2C+Z.+Lin+%28the+alert+truncates+the+author+list%3B+the+hosted+paper+indicates+additional+first+authors%29.%0Avenue%3A+USENIX+Security+2026%0Atopic%3A+PERMISSION+ANALYSIS%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.4+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-2.4%0Atitle%3A+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call%0Aauthors%3A+Y.+Aafer%2C+Z.+Lin+%28the+alert+truncates+the+author+list%3B+the+hosted+paper+indicates+additional+first+authors%29.%0Avenue%3A+USENIX+Security+2026%0Atopic%3A+PERMISSION+ANALYSIS%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-2.4+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call+%F0%9F%94%96&body=paper_id%3A+2026-08-17-2.4%0Atitle%3A+Missing+permission+checks+in+the+super-app+API+layer+that+mini-programs+sit+on+%E2%80%94+surfaced+from+a+followed+researcher%2C+listed+for+the+reader%27s+own+call%0Aauthors%3A+Y.+Aafer%2C+Z.+Lin+%28the+alert+truncates+the+author+list%3B+the+hosted+paper+indicates+additional+first+authors%29.%0Avenue%3A+USENIX+Security+2026%0Atopic%3A+PERMISSION+ANALYSIS%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Raising the Flag: Detecting Missing Permission Controls in Mini-Program APIs**

**Authors:** Y. Aafer, Z. Lin (the alert truncates the author list; the hosted paper indicates additional first authors).

**Venue:** USENIX Security 2026

**Link.** Conference programme: <https://www.usenix.org/conference/usenixsecurity26>. Scholar record: <https://scholar.google.com/scholar?q=Raising+the+Flag+Detecting+Missing+Permission+Controls+in+Mini-Program+APIs>.

**Provenance.** Alert-snippet read only. The hosted PDF could not be retrieved (HTTP 429), and the paper is not yet indexed by search. This entry is a pointer with a link, not an assessment.

### What the snippet establishes

Mini-programs embedded in super-apps such as WeChat have grown popular because they are flexible and convenient, and they get that flexibility from the underlying APIs the host exposes. The stated risk is that this tight integration is also a security liability — the snippet cuts off mid-sentence at "mini …", but the title supplies the rest: the target is *missing* permission controls in the API layer itself, meaning host APIs that should be gated and are not.

That framing is worth separating from the adjacent literature, which is dense. Most mini-program security work analyses the mini-programs — abusive permission requests, OAuth misuse, privacy-policy inconsistency. Auditing the *host's* API surface for absent checks is the harder and rarer direction, because it requires inferring what the intended policy was in the first place, with no specification to compare against. It is the same shape of problem as finding missing authorisation checks in an OS framework, and the second author's group has a long line of work on exactly that.

If the technique generalises past mini-programs — that is, if the missing-check inference is driven by something more portable than WeChat-specific conventions — this is the paper in today's window most likely to be reusable outside its own domain. Whether it does is not something the snippet can tell you. Given the venue and the group, it is worth pulling the PDF directly.

</details>

## Also Surfaced

Three further preprints from the profile-recommendation thread, listed with links and one-paragraph notes. All are snippet-level reads; none was fetchable today.

<details class="paper-card" markdown>
<summary><strong>3.1</strong> · <span class="topic-chip">FUZZING</span> · Using library documentation to satisfy both per-parameter constraints and inter-parameter relationships when generating Python API test inputs<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.1+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-3.1%0Atitle%3A+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs%0Aauthors%3A+B.+Duan%2C+T.+Mahmud%2C+M.+Che%2C+Y.+Yan%2C+N.+Dong%2C+D.+D.+Kim%2C+and+co-authors.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.1+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-3.1%0Atitle%3A+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs%0Aauthors%3A+B.+Duan%2C+T.+Mahmud%2C+M.+Che%2C+Y.+Yan%2C+N.+Dong%2C+D.+D.+Kim%2C+and+co-authors.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.1+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs+%F0%9F%94%96&body=paper_id%3A+2026-08-17-3.1%0Atitle%3A+Using+library+documentation+to+satisfy+both+per-parameter+constraints+and+inter-parameter+relationships+when+generating+Python+API+test+inputs%0Aauthors%3A+B.+Duan%2C+T.+Mahmud%2C+M.+Che%2C+Y.+Yan%2C+N.+Dong%2C+D.+D.+Kim%2C+and+co-authors.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Harnessing LLMs for Document-Guided Fuzzing of Python Libraries**

**Authors:** B. Duan, T. Mahmud, M. Che, Y. Yan, N. Dong, D. D. Kim, and co-authors.

**Venue:** arXiv preprint

**Link.** <https://arxiv.org/abs/2608.11744>

The stated problem is the one that makes Python API fuzzing hard and is usually hand-waved: valid inputs must satisfy per-parameter constraints *and* relationships that hold across parameters, and the latter are almost never encoded anywhere except prose documentation. Reading documentation as a constraint source rather than as context is the right instinct — it is the only place inter-parameter invariants are written down, and it is machine-readable in a way that type annotations are not.

The area is crowded. Document-guided LLM fuzzing has been applied to individual libraries before, and there is a substantial body of LLM-driven DL-library fuzzing going back several years. The question this paper has to answer to be worth the read is whether the documentation-to-constraint step is general across the Python ecosystem or tuned per library, and whether the bugs found are ones existing techniques miss rather than a re-derivation of the same crash set. The snippet does not say. Listed for the reader's own triage.

</details>

<details class="paper-card" markdown>
<summary><strong>3.2</strong> · <span class="topic-chip">FUZZING</span> · Cross-framework differential oracles to catch defects that behave consistently within one library and so survive intra-library and CPU–GPU checks<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.2+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-3.2%0Atitle%3A+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks%0Aauthors%3A+B.+Duan%2C+R.+Dong%2C+N.+Dong%2C+D.+D.+Kim%2C+G.+Yang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.2+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-3.2%0Atitle%3A+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks%0Aauthors%3A+B.+Duan%2C+R.+Dong%2C+N.+Dong%2C+D.+D.+Kim%2C+G.+Yang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.2+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks+%F0%9F%94%96&body=paper_id%3A+2026-08-17-3.2%0Atitle%3A+Cross-framework+differential+oracles+to+catch+defects+that+behave+consistently+within+one+library+and+so+survive+intra-library+and+CPU%E2%80%93GPU+checks%0Aauthors%3A+B.+Duan%2C+R.+Dong%2C+N.+Dong%2C+D.+D.+Kim%2C+G.+Yang.%0Avenue%3A+arXiv+preprint%0Atopic%3A+FUZZING%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**Testing Deep Learning Library APIs via Cross-Framework Differential Fuzzing**

**Authors:** B. Duan, R. Dong, N. Dong, D. D. Kim, G. Yang.

**Venue:** arXiv preprint

**Link.** <https://arxiv.org/abs/2608.11886>

The oracle argument here is the interesting part and is stated crisply in the snippet: existing API-level testing leans on intra-library properties or CPU–GPU differential oracles, and both are blind to defects that behave *consistently* across the comparison. A bug that is wrong the same way on CPU and GPU, or wrong in a way that respects the library's own invariants, is invisible to both. Comparing across independently implemented frameworks breaks that symmetry, because two teams are unlikely to make the same mistake.

The cost is the familiar one for cross-implementation differential testing: establishing that two APIs in two frameworks are semantically comparable is itself a research problem, and disagreements are often legitimate specification divergence rather than defects. Prior work on cross-framework API matching exists precisely because this is hard. Worth a look if you work on differential oracles; the transferable content, if any, is in how the false-positive burden from legitimate divergence is handled.

</details>

<details class="paper-card" markdown>
<summary><strong>3.3</strong> · <span class="topic-chip">LLM SECURITY</span> · Adversarial code comments as an attack surface: natural-language context inside source code is an input channel that LLM vulnerability detectors trust<span class="feedback-buttons"><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.3+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust+%F0%9F%91%8D&body=paper_id%3A+2026-08-17-3.3%0Atitle%3A+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust%0Aauthors%3A+Z.+Wu%2C+C.+Nita-Rotaru.%0Avenue%3A+arXiv+preprint%0Atopic%3A+LLM+SECURITY%0Arating%3A+thumbs-up%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-up" target="_blank" rel="noopener" class="fb-thumbs-up" title="thumbs up" onclick="event.stopPropagation()">👍</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.3+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust+%F0%9F%AB%A5&body=paper_id%3A+2026-08-17-3.3%0Atitle%3A+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust%0Aauthors%3A+Z.+Wu%2C+C.+Nita-Rotaru.%0Avenue%3A+arXiv+preprint%0Atopic%3A+LLM+SECURITY%0Arating%3A+thumbs-down%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Cthumbs-down" target="_blank" rel="noopener" class="fb-thumbs-down" title="less interested" onclick="event.stopPropagation()">🫥</a><a href="https://github.com/MarkLee131/paper-digest/issues/new?title=%5Bfeedback%5D+2026-08-17-3.3+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust+%F0%9F%94%96&body=paper_id%3A+2026-08-17-3.3%0Atitle%3A+Adversarial+code+comments+as+an+attack+surface%3A+natural-language+context+inside+source+code+is+an+input+channel+that+LLM+vulnerability+detectors+trust%0Aauthors%3A+Z.+Wu%2C+C.+Nita-Rotaru.%0Avenue%3A+arXiv+preprint%0Atopic%3A+LLM+SECURITY%0Arating%3A+save-for-later%0A%0A%3C%21--+Optional+notes+below+this+line+are+read+by+preferences.py+as+soft+signals.+--%3E%0A&labels=feedback%2Csave-for-later" target="_blank" rel="noopener" class="fb-save-for-later" title="save for later" onclick="event.stopPropagation()">🔖</a></span></summary>

**ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments**

**Authors:** Z. Wu, C. Nita-Rotaru.

**Venue:** arXiv preprint

**Link.** <https://arxiv.org/abs/2607.24964>

The premise is clean and slightly uncomfortable. LLMs are being deployed on vulnerability detection and code review, and their strength on those tasks comes partly from reading the natural-language context embedded in source — identifiers, docstrings, comments. That context is attacker-controlled in exactly the situations where it matters most: a malicious contributor writing a pull request controls the comments alongside the code. The snippet describes this as a previously underexplored attack surface, and it is hard to argue.

What makes this worth flagging rather than filing under generic prompt injection is the deployment context. A comment that suppresses a detector's finding is a supply-chain attack with a plausible cover story, and unlike most prompt injection it survives code review by humans who are reading the code, not auditing the prose. Anyone treating LLM review output as a gate rather than a hint should know the failure mode exists. The "adaptive agentic" framing suggests an attacker loop that iterates against detector feedback, which would make static comment-sanitisation defences weak, but the snippet does not confirm this.

</details>

---

## Cross-Paper Synthesis

**Benchmark harnesses are now part of the threat model.** The two strongest entries in this window arrived independently and converged on the same worry from opposite directions. RealisticTritonBench names manually written per-kernel evaluation scripts as flawed artefacts that models exploit to bypass correctness checks and inflate scores. SRE-Bench ran an adversarial reward-hacking audit against its own graders during construction, and the audit found real holes — a leaked identifier string that let an agent skip the analysis, a "delete everything" strategy that scored on the cleanup task. Both answer structurally rather than by writing more careful oracles: one reuses the originating framework's own end-to-end tests, the other makes scoring conjunctive and moves grading logic into held-out infrastructure the agent never sees.

The generalisation is that a benchmark is a program under adversarial input, and the adversary is getting better at finding its bugs. Building one without an adversarial audit is now roughly where building a parser without fuzzing was fifteen years ago.

**Contamination control and realism trade against each other, and cheap versions of either are worthless.** SRE-Bench's ablation is the cleanest evidence anyone has published on this: a real gzip encoder with 200 lines rewritten costs the same to solve as a 1.1k-line toy, and both are saturated. The two standard cheap moves — perturb something public, or write something small and private — each independently destroy the measurement, and they destroy it *silently*, producing plausible-looking numbers. The check is one small three-program ablation, and it should be table stakes.

**Oracles that share a blind spot with the system under test find nothing.** This is 3.2's argument about CPU–GPU differential testing missing defects that behave consistently across both, and it is also 2.1's finding that agents' weakness is symbol stripping rather than optimisation. In both cases the measurement instrument was correlated with the thing being measured. The recurring fix is to introduce an *independent* implementation or an *uncorrelated* difficulty axis, and the recurring cost is that independence generates false positives from legitimate divergence.

**Behavioural difference as an information leak spans the window's security papers.** 2.3's association-based attacks are, at root, about a device that responds differently to recognised and unrecognised peers. 2.4 is about a host API that checks permissions on some paths and not others — an inconsistency that is discoverable precisely because it is inconsistent. 3.3 is about a detector whose behaviour changes based on attacker-controlled prose. Uniformity of response is the countermeasure in all three, and it is expensive in all three, which is why it keeps not happening.

**A note on the agent-capability picture.** The strongest model in 2.1 fully solves 31.5 % of instances and scores 61.4 % overall; against protection it drops to 2.50 of 6, and every other tested model effectively fails. Read alongside 3.3, the shape is consistent: LLM-based security tooling is capable enough to deploy and brittle in ways that are cheap to trigger deliberately. The gap between "works on the benchmark" and "works against someone who read the benchmark paper" is the thing to watch.

## Writing & Rationale Insights

**Test your design requirements instead of asserting them.** SRE-Bench spends over 5,000 expert hours on a design whose necessity a sceptical reviewer would reasonably question, then spends one small ablation — three programs, eight configurations, two models — proving that the two cheaper alternatives both collapse. That ablation is what converts the cost from a liability into the paper's central claim. If your method is expensive, the highest-value experiment you can run is the one that shows the cheap version fails.

**Report the distribution's ends, not just its mean.** The choice to report Solve (6/6) and Zero (0/6) alongside the mean is justified explicitly by the distribution piling up at both ends. Two models with the same mean can differ completely in whether they half-solve everything or fully solve a third and fail the rest. That is a reusable habit for any rubric-scored evaluation.

**Invert the reader's expected ordering and say so.** The build-factor result is memorable because the paper states plainly that it inverts the conventional ordering of RE difficulty, then gives numbers small enough to be startling (0.08, 0.04) next to one large enough to matter (0.48). A finding framed as "this contradicts what you assume" is retained; the same numbers presented as a neutral table are not.

**Write down what you did not measure, in the same voice as what you did.** SRE-Bench notes that 44 of 262 runs were lost for one model to context exhaustion and that ungradeable runs are excluded from all averages — which is an invitation to discount that model's row, published by the authors themselves. Stating the caveat plainly costs less credibility than having a reader find it.

**Anticipate becoming training data.** The paper limits its own disclosure to what an analyst could recover from the binaries anyway, and *verifies* this by having a model reconstruct the masked details within a bounded request budget. That is a genuinely new methodological obligation for benchmark papers, and it will not be the last one to face it.

**On this report's own limits.** Entries 2.2 through 3.3 are abstract- and snippet-level reads because the fetch layer returned HTTP 429 throughout — the third consecutive day. They are written to that standard on purpose: what the source said, what it did not say, and what would have to be checked. No formal notation appears for any of them, because none was available in the papers' own text.
