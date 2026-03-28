# Draft Manuscript For Malaria Journal

## Working Note

This is a journal-specific draft for repository use. Before submission, authors should finalize authorship metadata, expand the literature framing if desired, and export the file to the journal's preferred editable format with line and page numbering.

## Title

Registry-first operational scan of completed, results-posted Africa-site malaria randomized trials: identifying lean transfer templates for future trial delivery

## Abstract

### Background

African clinical trial programs need examples of malaria randomized controlled trials that were completed, publicly reported, and operationally simpler to run. Prior descriptive work on malaria RCTs in Africa found that many studies were medium-sized and single-centre, and recent malaria priority-setting work in sub-Saharan Africa has stressed the need for operational evidence to guide strategy and implementation. We therefore aimed to identify completed, results-posted Africa-site malaria randomized trials that resemble lean transfer templates for future African RCT delivery.

### Methods

We performed a registry-first cross-sectional analysis using the ClinicalTrials.gov API. We included completed interventional studies with randomized allocation, posted results, the focus term `malaria`, and at least one African study site. The primary estimand was the proportion of benchmark studies meeting a predefined transfer shortlist: enrollment `<=500`, location count `<=10`, country count `<=2`, and prospective registration. These cut points were used as pragmatic screening rules to favor medium-sized, lower-footprint studies rather than as validated cost thresholds. We summarized trial timing, sponsor class, country distribution, and malaria-specific deep-dive signals from the results section and leadership heuristic, and performed simple threshold sensitivity analyses.

### Results

The benchmark contained `80` completed, results-posted Africa-site studies, of which `27` met the primary shortlist, giving a proportion of `0.34` with `95% confidence interval 0.24 to 0.45`. Under a stricter rule (`<=300` participants, `<=5` sites, `1` country), the proportion was `0.18`; under a more lenient rule (`<=750`, `<=15`, `<=3`), it was `0.41`. Median enrollment was `424.0`, median trial duration was `619.0` days, and median results-reporting lag was `719.5` days. Kenya, Uganda, Mali, Burkina Faso, and Ghana were the most represented countries. In the malaria deep dive, `32/80` studies had structured primary analyses, `22/80` had primary p-values, and `28/80` had primary effect estimates or confidence intervals. No study was confidently classified as locally sponsor-led from registry metadata alone.

### Conclusions

A substantial minority of completed, results-posted Africa-site malaria randomized trials already resemble lean operational templates, especially prospectively registered single-country studies with moderate enrollment and simpler geographic footprints. Malaria appears to provide a practical starting point for African RCT program design, but the estimate depends on pragmatic shortlist rules, and registry metadata cannot directly measure true cost, effectiveness, or local intellectual leadership.

## Keywords

malaria; randomized controlled trials; Africa; ClinicalTrials.gov; operational research; registry analysis; trial delivery

## Background

African clinical trial programs need designs that can be implemented with lower operational burden while still completing study delivery and public reporting. A practical way to look for such designs is to examine trials that already ran in African settings and ask which ones combined smaller geographic footprints, moderate enrollment, prospective registration, and posted results. Malaria is a strong candidate domain for this exercise because it is both operationally important across Africa and well represented in ClinicalTrials.gov. Recent malaria priority-setting work in sub-Saharan Africa emphasized that policy, strategy, and operational decisions should be guided by high-quality evidence, including operational research that can close implementation gaps.[1]

This repository began as a four-topic registry scan comparing malaria, HIV, hypertension, and maternal health. Malaria produced the largest Africa transfer shortlist and the broadest spread across African countries, making it the strongest first topic for a journal-specific manuscript. The current paper therefore narrows to completed, results-posted Africa-site malaria randomized trials and asks how often these benchmark studies resemble operationally lean transfer templates for future African RCT programs.

The goal is deliberately operational rather than causal. We are not estimating treatment effectiveness across malaria interventions, and we do not claim to measure true cost. Instead, we use public registry signals to identify study designs that appear lighter to run and therefore more plausible as transfer templates for future African RCT delivery. This framing is also consistent with older descriptive work showing that many African malaria RCTs were medium-sized and single-centre, which provides a practical anchor for a moderate-footprint shortlist rather than a search for only very small pilot studies.[2]

## Methods

### Study design

We conducted a registry-first cross-sectional analysis of ClinicalTrials.gov study records using the public API. The analysis focused on malaria studies with randomized allocation, completed status, posted results, and at least one African site. The repository snapshot used for this manuscript was generated on 28 March 2026. The resulting benchmark should be interpreted as a registry-based sample of completed, results-posted studies rather than as a census of all African malaria RCTs.

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

We defined a pragmatic transfer shortlist to identify studies with simpler operating footprints. Trials entered the shortlist if they had enrollment `<=500`, location count `<=10`, country count `<=2`, and prospective registration, defined as study submission on or before study start. These thresholds were chosen as transparent screening rules rather than validated cost cut points. The enrollment threshold was intended to retain moderate-sized trials, which aligns with earlier descriptive evidence that African malaria RCTs were often in the `100-500` participant range.[2] The site and country thresholds were chosen to favor operationally simpler study footprints. Prospective registration was included to prioritize designs that more credibly support transparent future reuse.

### Malaria deep dive

We added a malaria-specific layer that examined whether the registry results section contained structured primary analyses, primary p-values, and primary effect estimates or confidence intervals. We also applied a cautious leadership heuristic using sponsor names, investigator affiliations, and African site institutions. These leadership labels were treated as heuristic descriptors rather than definitive claims about intellectual ownership or funding control.

### Statistical analysis

The primary estimand was the proportion of Africa-site benchmark trials meeting the transfer shortlist. We summarized this proportion with a Wilson 95% confidence interval. Other results are descriptive and include medians, country concentration, sponsor mix, and deep-dive signal coverage. To assess the dependence of the main result on the chosen shortlist rule, we also calculated simple sensitivity analyses using a stricter rule (`<=300` participants, `<=5` sites, `1` country), a more lenient rule (`<=750`, `<=15`, `<=3`), and a version of the primary rule that dropped prospective-registration filtering.

### Generative AI use

A generative AI assistant was used during repository preparation to help draft and organize manuscript-support files. All numerical claims and journal-guideline details were checked against saved repository outputs and official journal instructions by the human authors.

## Results

### Benchmark size and shortlist yield

The Africa-site malaria benchmark contained `80` completed, results-posted randomized studies. Of these, `27` met the predefined transfer shortlist criteria, giving a shortlist proportion of `0.34` with `95% confidence interval 0.24 to 0.45`.

### Sensitivity to shortlist definition

The main signal was directionally stable but quantitatively sensitive to the shortlist rule. Under the stricter rule, `14/80` studies met criteria, corresponding to `0.18` with `95% confidence interval 0.11 to 0.27`. Under the more lenient rule, `33/80` studies met criteria, corresponding to `0.41` with `95% confidence interval 0.31 to 0.52`. When the primary footprint thresholds were kept but prospective registration was not required, `35/80` studies met criteria, corresponding to `0.44` with `95% confidence interval 0.33 to 0.55`. These checks show that the benchmark does identify a recurring lower-footprint subgroup, but the exact proportion depends materially on the operational definition used.

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

This registry-first analysis suggests that a substantial minority of completed, results-posted Africa-site malaria randomized trials already resemble lean operational templates for future African RCT programs. The strongest recurring pattern was not very small pilot work or highly centralized multicountry infrastructure. Instead, the shortlist was dominated by prospectively registered, single-country or near-single-country studies with moderate enrollment and relatively simple geographic footprints. That pattern is broadly compatible with the historical descriptive malaria trial literature, which reported many African malaria RCTs as medium-sized and single-centre.[2]

For African trial systems, that pattern is important because it points toward a realistic design envelope. A future low-burden RCT program does not need to begin by reproducing the largest multicountry networks. It can start with narrower operational footprints that have already been demonstrated in malaria, then expand selectively as delivery capacity strengthens.

The deep dive changes the interpretation in one important way. Registry metadata did not support confident identification of clearly locally sponsor-led studies, even though it did reveal a group of mixed local-site and external-sponsor studies. That means the present dataset is better at identifying feasible delivery templates than at adjudicating African intellectual leadership. In practical terms, malaria offers a useful delivery model first, but not yet a clean sponsor-ownership model.

The paper has several limitations. First, registry-visible proxies are not direct measures of true budget, procurement cost, staffing burden, or real-world program efficiency. Second, linked publication coverage was incomplete, which weakens any inference about publication speed beyond results posting, a broader issue that has also been documented in ClinicalTrials.gov-linked publication analyses.[3,4] Third, sponsor and leadership classifications were heuristic and should not be treated as definitive claims about authorship equity or financing control. Fourth, ClinicalTrials.gov is not a complete census of all African malaria trials, so the benchmark may overrepresent studies tied to registries, sponsors, or sites with stronger reporting infrastructure. Fifth, the exact shortlist proportion is sensitive to the chosen thresholds, so the rule should be interpreted as a practical screening heuristic rather than an optimized definition of low-cost trial delivery.

Despite those limits, the analysis still provides a practical operational signal. Malaria emerged as the strongest topic from the broader four-domain scan, and within malaria there is a clear subset of African trials that look more transferable to lower-footprint future RCT programs.

## Conclusions

A meaningful minority of completed, results-posted Africa-site malaria randomized trials on ClinicalTrials.gov met a pragmatic shortlist for lean delivery, with `27` of `80` benchmark studies satisfying the primary footprint and registration criteria. The most promising templates were prospectively registered studies with moderate enrollment and simpler country and site footprints. Malaria therefore appears to be a practical starting point for designing faster and potentially lower-burden African RCT programs, while future work should strengthen direct cost measurement, effectiveness linkage, attribution of local intellectual leadership, and threshold calibration.

## List Of Abbreviations

- API: application programming interface
- CI: confidence interval
- RCT: randomized controlled trial

## Declarations

### Ethics approval and consent to participate

Not applicable. This study analyzed publicly available registry records and did not involve direct contact with human participants or access to identifiable individual-level data.

### Consent for publication

Not applicable.

### Availability of data and materials

All data analyzed in this study are derived from publicly accessible ClinicalTrials.gov records and are included in this repository as processed CSV and markdown outputs. The main analysis files are available in `data/`, and the code used to generate the benchmark and deep-dive outputs is available in `code/`. The public repository URL is `https://github.com/mahmood726-cyber/malaria-e156`.

### Competing interests

`[To be completed by authors. If none, use: "The authors declare that they have no competing interests."]`

### Funding

`[To be completed by authors. State all funding sources and any funder role in design, analysis, interpretation, writing, or publication decisions.]`

### Authors' contributions

`[To be completed by authors using initials, consistent with journal policy.]`

### Acknowledgements

`[Optional. Add non-author contributors, institutional support, or writing or editorial support if applicable.]`

### Authors' information

`[Optional. Add concise background information only if it materially helps readers interpret the work.]`

## References

1. Tine R, Herrera S, Badji MA, et al. Defining operational research priorities to improve malaria control and elimination in sub-Saharan Africa: results from a country-driven research prioritization setting process. Malar J. 2023;22(1):219. doi:10.1186/s12936-023-04654-8.
2. Lutje V, Gerritsen A, Siegfried N. Randomized controlled trials of malaria intervention trials in Africa, 1948 to 2007: a descriptive analysis. Malar J. 2011;10:61. doi:10.1186/1475-2875-10-61.
3. Ross JS, Tse T, Zarin DA, Xu H, Zhou L, Krumholz HM. Publication of NIH funded trials registered in ClinicalTrials.gov: cross sectional analysis. BMJ. 2012;344:d7292. doi:10.1136/bmj.d7292.
4. Shi X, Du J. Constructing a finer-grained representation of clinical trial results from ClinicalTrials.gov. Sci Data. 2024;11:41. doi:10.1038/s41597-023-02869-7.
5. ClinicalTrials.gov. About the ClinicalTrials.gov API. https://clinicaltrials.gov/data-api/api. Accessed 28 Mar 2026.
6. ClinicalTrials.gov. Study data structure. https://clinicaltrials.gov/data-about-studies/study-data-structure. Accessed 28 Mar 2026.
7. ClinicalTrials.gov. Constructing complex search queries. https://clinicaltrials.gov/find-studies/constructing-complex-search-queries. Accessed 28 Mar 2026.
8. National Library of Medicine. E-utilities and API basics. https://www.nlm.nih.gov/dataguide/eutilities/what_is_eutilities.html. Accessed 28 Mar 2026.
