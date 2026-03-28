# Draft Manuscript For Malaria Journal

## Working Note

This is a journal-specific draft for repository use. Before submission, authors should finalize authorship metadata, expand the literature framing if desired, and export the file to the journal's preferred editable format with line and page numbering.

## Title

Registry-first operational scan of Africa-site malaria randomized trials: identifying lean transfer templates for faster trial delivery

## Abstract

Use the structured abstract in `submission/ABSTRACT.md`.

## Keywords

malaria; randomized controlled trials; Africa; ClinicalTrials.gov; operational research; registry analysis; trial delivery

## Background

African clinical trial programs need designs that can be implemented with lower operational burden while still completing study delivery and public reporting. A practical way to look for such designs is to examine trials that already ran in African settings and ask which ones combined smaller geographic footprints, moderate enrollment, prospective registration, and posted results. Malaria is a strong candidate domain for this exercise because it is both operationally important across Africa and well represented in ClinicalTrials.gov.

This repository began as a four-topic registry scan comparing malaria, HIV, hypertension, and maternal health. Malaria produced the largest Africa transfer shortlist and the broadest spread across African countries, making it the strongest first topic for a journal-specific manuscript. The current paper therefore narrows to malaria and asks how often Africa-site malaria randomized trials resemble operationally lean transfer templates for future African RCT programs.

The goal is deliberately operational rather than causal. We are not estimating treatment effectiveness across malaria interventions, and we do not claim to measure true cost. Instead, we use public registry signals to identify study designs that appear lighter to run and therefore more plausible as transfer templates for future African RCT delivery.

## Methods

### Study design

We conducted a registry-first cross-sectional analysis of ClinicalTrials.gov study records using the public API. The analysis focused on malaria studies with randomized allocation, completed status, posted results, and at least one African site. The repository snapshot used for this manuscript was generated on 28 March 2026.

### Data source and query logic

The base query required `INTERVENTIONAL` studies, `RANDOMIZED` allocation, `COMPLETED` overall status, and non-missing `ResultsFirstPostDate`. The topic term `malaria` was then added. Africa-site studies were identified through study-location countries matching a predefined African country list in the analysis code. The public API fields were extracted from the protocol section and, for the deep dive, from the results section.

### Eligibility criteria

Studies were included in the Africa-site benchmark if they met all of the following criteria:

- interventional study type
- randomized allocation
- completed status
- posted results on ClinicalTrials.gov
- at least one African study site

### Variables

We extracted enrollment, number of locations, number of countries, lead sponsor class, intervention type, start date, primary completion date, results first-post date, and linked publication identifiers. We computed trial duration as the interval from study start to primary completion and results-reporting lag as the interval from primary completion to first posted results. We also queried PubMed through NCBI E-utilities to estimate publication linkage where result-linked PubMed identifiers were present.

### Transfer shortlist

We defined a pragmatic transfer shortlist to identify studies with simpler operating footprints. Trials entered the shortlist if they had enrollment `<=500`, location count `<=10`, country count `<=2`, and prospective registration, defined as study submission on or before study start.

### Malaria deep dive

We added a malaria-specific layer that examined whether the registry results section contained structured primary analyses, primary p-values, and primary effect estimates or confidence intervals. We also applied a cautious leadership heuristic using sponsor names, investigator affiliations, and African site institutions. These leadership labels were treated as heuristic descriptors rather than definitive claims about intellectual ownership or funding control.

### Statistical analysis

The primary estimand was the proportion of Africa-site benchmark trials meeting the transfer shortlist. We summarized this proportion with a Wilson 95% confidence interval. Other results are descriptive and include medians, country concentration, sponsor mix, and deep-dive signal coverage.

### Generative AI use

A generative AI assistant was used during repository preparation to help draft and organize manuscript-support files. All numerical claims and journal-guideline details were checked against saved repository outputs and official journal instructions by the human authors.

## Results

### Benchmark size and shortlist yield

The Africa-site malaria benchmark contained `80` completed, results-posted randomized studies. Of these, `27` met the predefined transfer shortlist criteria, giving a shortlist proportion of `0.34` with `95% confidence interval 0.24 to 0.45`.

### Operational profile of the benchmark

Median enrollment across the Africa-site benchmark was `424.0` participants. Median trial duration was `619.0` days, and median results-reporting lag was `719.5` days. The most represented Africa-site countries were Kenya (`22` studies), Uganda (`18`), Mali (`17`), Burkina Faso (`16`), and Ghana (`11`). The top sponsor classes in the shortlist were `OTHER` (`14`), `INDUSTRY` (`7`), `NIH` (`4`), and `FED` (`2`).

Table 1 summarizes the main operational benchmark signals.

| Metric | Value |
| --- | --- |
| Africa-site benchmark studies | 80 |
| Transfer shortlist studies | 27 |
| Shortlist proportion | 0.34 |
| 95% confidence interval | 0.24 to 0.45 |
| Median enrollment | 424.0 |
| Median trial duration, days | 619.0 |
| Median results-reporting lag, days | 719.5 |
| Most represented countries | Kenya, Uganda, Mali, Burkina Faso, Ghana |

### Deep-dive outcome and leadership coverage

Within the same `80`-study malaria benchmark, `32` studies had structured primary analyses, `22` had primary p-values, and `28` had primary effect estimates or confidence intervals in the results section. The registry-based leadership heuristic classified `69` studies as likely externally run and `11` as mixed local-site with external sponsor. No study was confidently classified as locally sponsor-led from registry metadata alone. Among the `27` shortlist studies, `5` were in the mixed local-site with external-sponsor group.

The top mixed local-site candidates included studies in Tanzania, Mali, Ghana, South Africa, and Uganda. This pattern suggests that the most transferable malaria templates in the current registry sample may reflect African site-led delivery within externally sponsored studies rather than clearly Africa-owned sponsor leadership.

Table 2 summarizes the deep-dive coverage.

| Deep-dive metric | Value |
| --- | --- |
| Studies with structured primary analyses | 32 |
| Studies with primary p-values | 22 |
| Studies with effect estimates or confidence intervals | 28 |
| Likely externally run | 69 |
| Mixed local-site with external sponsor | 11 |
| Clearly locally sponsor-led | 0 |

## Discussion

This registry-first analysis suggests that a substantial minority of Africa-site malaria randomized trials already resemble lean operational templates for future African RCT programs. The strongest recurring pattern was not very small pilot work or highly centralized multicountry infrastructure. Instead, the shortlist was dominated by prospectively registered, single-country or near-single-country studies with moderate enrollment and relatively simple geographic footprints.

For African trial systems, that pattern is important because it points toward a realistic design envelope. A future low-burden RCT program does not need to begin by reproducing the largest multicountry networks. It can start with narrower operational footprints that have already been demonstrated in malaria, then expand selectively as delivery capacity strengthens.

The deep dive changes the interpretation in one important way. Registry metadata did not support confident identification of clearly locally sponsor-led studies, even though it did reveal a group of mixed local-site and external-sponsor studies. That means the present dataset is better at identifying feasible delivery templates than at adjudicating African intellectual leadership. In practical terms, malaria offers a useful delivery model first, but not yet a clean sponsor-ownership model.

The paper has several limitations. First, registry-visible proxies are not direct measures of true budget, procurement cost, staffing burden, or real-world program efficiency. Second, linked publication coverage was incomplete, which weakens any inference about publication speed beyond results posting. Third, sponsor and leadership classifications were heuristic and should not be treated as definitive claims about authorship equity or financing control. Fourth, ClinicalTrials.gov is not a complete census of all African malaria trials, so the benchmark may overrepresent studies tied to registries, sponsors, or sites with stronger reporting infrastructure.

Despite those limits, the analysis still provides a practical operational signal. Malaria emerged as the strongest topic from the broader four-domain scan, and within malaria there is a clear subset of African trials that look more transferable to lower-footprint future RCT programs.

## Conclusions

A meaningful minority of Africa-site malaria randomized trials on ClinicalTrials.gov meet a pragmatic shortlist for lean delivery, with `27` of `80` benchmark studies satisfying pre-specified footprint and registration criteria. The most promising templates are prospectively registered studies with moderate enrollment and simpler country and site footprints. Malaria therefore appears to be a practical starting point for designing faster and potentially lower-burden African RCT programs, while future work should strengthen direct cost measurement, effectiveness linkage, and attribution of local intellectual leadership.

## List Of Abbreviations

- API: application programming interface
- CI: confidence interval
- RCT: randomized controlled trial

## Declarations

Use the text in `submission/DECLARATIONS.md`, replacing placeholders before submission.

## References

1. ClinicalTrials.gov. About the ClinicalTrials.gov API. https://clinicaltrials.gov/data-api/api. Accessed 28 Mar 2026.
2. ClinicalTrials.gov. Study data structure. https://clinicaltrials.gov/data-about-studies/study-data-structure. Accessed 28 Mar 2026.
3. ClinicalTrials.gov. Constructing complex search queries. https://clinicaltrials.gov/find-studies/constructing-complex-search-queries. Accessed 28 Mar 2026.
4. National Library of Medicine. E-utilities and API basics. https://www.nlm.nih.gov/dataguide/eutilities/what_is_eutilities.html. Accessed 28 Mar 2026.
