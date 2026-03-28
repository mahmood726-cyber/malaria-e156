# Protocol

## Title

Registry-first Africa-site malaria RCT transfer scan.

## Rationale

This protocol describes a descriptive ClinicalTrials.gov scan focused on completed randomized interventional studies with posted results in the malaria domain.

## Primary Objective

Estimate the proportion of Africa-site malaria trials that meet a pragmatic transfer shortlist for cheaper and faster delivery.

## Data Source

ClinicalTrials.gov API v2 with focus term `malaria` plus Africa-site location filtering.

## Eligibility

- Study type: interventional
- Allocation: randomized
- Status: completed
- Results: posted on ClinicalTrials.gov
- Geography: at least one African study site

## Primary Estimand

Shortlist proportion among Africa-site benchmark trials. In the current run this was 27/80 with Wilson 95% interval 0.24 to 0.45.

## Secondary Measures

- trial duration days
- results-reporting lag days
- publication-link coverage
- country concentration
- sponsor-class mix

## Analysis Plan

Use registry-visible proxies only. Do not infer true budget or true intervention effectiveness from the shortlist metric alone.

## Outputs

- `paper/article.json`
- `paper/index.html`
- `data/summary.md`
- `data/africa_benchmark.csv`
- `data/africa_transfer_shortlist.csv`

## Limitation

This protocol relies on registry metadata and does not directly measure cost, implementation feasibility, or African intellectual leadership.
