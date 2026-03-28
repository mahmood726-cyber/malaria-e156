# Protocol

## Working Title

Registry-first Africa-site malaria randomized trials as a transfer template for cheaper and faster RCT delivery.

## Background and Rationale

Large differences in infrastructure, budget, and trial management capacity make it hard to identify RCT designs that can be transferred across African settings. This protocol uses ClinicalTrials.gov as a registry-first screening layer to identify Africa-site randomized trials that look operationally lean and comparatively fast.

## Primary Objective

Estimate the proportion of Africa-site malaria randomized trials that meet a pragmatic transfer shortlist defined by smaller enrollment, lower site and country footprint, prospective registration, and completed results posting.

## Study Design

Descriptive registry analysis using ClinicalTrials.gov API v2 records restricted to completed randomized interventional studies with posted results and at least one African site.

## Data Source and Search Logic

- Registry: ClinicalTrials.gov API v2
- Focus term: `malaria`
- Geography filter: at least one African site country
- Query frame: interventional, randomized, completed, and not missing results posting

## Eligibility Criteria

- Study type: interventional
- Allocation: randomized
- Overall status: completed
- Results: posted on ClinicalTrials.gov
- Geography: at least one African study site

## Primary Estimand

Shortlist proportion among Africa-site benchmark trials. In the current analysis this was `27/80` with Wilson 95% interval `0.24` to `0.45`.

## Secondary Measures

- median trial duration days
- median results-reporting lag days
- publication-link coverage and result-PMID coverage
- country concentration across Africa-site records
- sponsor-class concentration among shortlist studies

## Current Snapshot

- Benchmark trials: `80`
- Total enrolled participants across benchmark records: `222914`
- Median trial duration days: `619.0`
- Median results-reporting lag days: `719.5`
- Most represented Africa-site countries: Kenya (22), Uganda (18), Mali (17), Burkina Faso (16), Ghana (11)
- Shortlist sponsor mix: OTHER (14), INDUSTRY (7), NIH (4), FED (2)

## Analysis Plan

Use registry-visible proxies only. Compare Africa-site benchmarks against the topic-specific global benchmark. Treat the shortlist proportion as the lead operational signal and interpret duration, reporting lag, and sponsor mix as supporting markers rather than direct measures of cost or effectiveness.

## Governance and Limitations

This protocol does not estimate true budget, true implementation cost, or true clinical effectiveness. Registry metadata can understate local intellectual leadership, publication linkage is incomplete, and sponsor-country inference is imperfect.

## Outputs

- `paper/article.json`
- `paper/index.html`
- `paper/e156_body.md`
- `paper/validation.json`
- `data/summary.md`
- `data/africa_benchmark.csv`
- `data/africa_transfer_shortlist.csv`

## Versioning

Current protocol version: `0.1.0` dated `2026-03-28`.
