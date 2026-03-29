#!/usr/bin/env python3
"""Deep-dive malaria Africa-site trials for signal extraction and leadership heuristics."""

from __future__ import annotations

import csv
import json
import re
import statistics
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECT_RAW_DIR = ROOT / "data" / "raw" / "malaria"
REPO_RAW_DIR = ROOT / "data" / "raw" / "malaria"
PROJECT_PROCESSED_DIR = ROOT / "data" / "processed" / "malaria"
REPO_DATA_DIR = ROOT / "data"

AFRICAN_COUNTRIES = {
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "Congo", "Cote d'Ivoire", "Democratic Republic of the Congo", "Djibouti",
    "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon",
    "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
    "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania",
    "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria",
    "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles",
    "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan",
    "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    "Côte d’Ivoire", "Côte d'Ivoire",
}
EXTERNAL_SPONSOR_CLASSES = {"INDUSTRY", "FED", "NIH", "NETWORK"}
MALARIA_RELEVANCE_TERMS = ("malaria", "plasmodium", "falciparum", "vivax")


def normalize(text: str | None) -> str:
    if not text:
        return ""
    lowered = text.lower()
    lowered = lowered.replace("&", " and ")
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    return " ".join(lowered.split())


def text_match(a: str, b: str) -> bool:
    na = normalize(a)
    nb = normalize(b)
    if not na or not nb:
        return False
    if min(len(na), len(nb)) < 8:
        return False
    return na in nb or nb in na


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def resolve_layout() -> tuple[Path, Path, Path, Path]:
    if PROJECT_PROCESSED_DIR.exists():
        return (
            PROJECT_RAW_DIR,
            PROJECT_PROCESSED_DIR,
            PROJECT_PROCESSED_DIR / "africa_benchmark.csv",
            PROJECT_PROCESSED_DIR / "africa_transfer_shortlist.csv",
        )
    return (
        REPO_RAW_DIR,
        REPO_DATA_DIR,
        REPO_DATA_DIR / "africa_benchmark.csv",
        REPO_DATA_DIR / "africa_transfer_shortlist.csv",
    )


def load_studies() -> dict[str, dict[str, Any]]:
    by_nct: dict[str, dict[str, Any]] = {}
    raw_dir, _, _, _ = resolve_layout()
    for path in sorted(raw_dir.glob("africa_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for study in payload.get("studies", []):
            nct_id = study.get("protocolSection", {}).get("identificationModule", {}).get("nctId")
            if nct_id:
                by_nct[nct_id] = study
    return by_nct


def parse_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def parse_pvalue(value: Any) -> float | None:
    if value in (None, ""):
        return None
    text = str(value).strip().lower()
    text = text.replace("p", "").replace("=", "").strip()
    if text.startswith("<"):
        parsed = parse_float(text[1:].strip())
        return parsed if parsed is not None else None
    if text.startswith(">"):
        parsed = parse_float(text[1:].strip())
        return parsed if parsed is not None else None
    return parse_float(text)


def study_topic_text(study: dict[str, Any], include_descriptions: bool = False) -> str:
    protocol = study.get("protocolSection", {})
    ident = protocol.get("identificationModule", {})
    conditions = protocol.get("conditionsModule", {})
    text_parts = [
        ident.get("briefTitle", ""),
        ident.get("officialTitle", ""),
        " ".join(conditions.get("conditions") or []),
        " ".join(conditions.get("keywords") or []),
    ]
    if include_descriptions:
        descriptions = protocol.get("descriptionModule", {})
        text_parts.extend([
            descriptions.get("briefSummary", ""),
            descriptions.get("detailedDescription", ""),
        ])
    return normalize(" ".join(text_parts))


def is_malaria_relevant(study: dict[str, Any]) -> bool:
    text = study_topic_text(study, include_descriptions=False)
    return any(term in text for term in MALARIA_RELEVANCE_TERMS)


def extract_signal_fields(study: dict[str, Any]) -> dict[str, Any]:
    outcomes = ((study.get("resultsSection", {}).get("outcomeMeasuresModule") or {}).get("outcomeMeasures") or [])
    primary = [outcome for outcome in outcomes if outcome.get("type") == "PRIMARY"]
    analyses: list[dict[str, Any]] = []
    for outcome in primary:
        for analysis in outcome.get("analyses") or []:
            enriched = dict(analysis)
            enriched["_outcome_title"] = outcome.get("title", "")
            analyses.append(enriched)

    pvalues = [parse_pvalue(analysis.get("pValue")) for analysis in analyses]
    pvalues = [value for value in pvalues if value is not None]
    effect_values = [analysis for analysis in analyses if analysis.get("paramValue") not in (None, "")]
    cis = [
        analysis
        for analysis in analyses
        if analysis.get("ciLowerLimit") not in (None, "") and analysis.get("ciUpperLimit") not in (None, "")
    ]
    significant = [value for value in pvalues if value <= 0.05]

    best_analysis = None
    if analyses:
        best_analysis = next((analysis for analysis in analyses if parse_pvalue(analysis.get("pValue")) is not None and parse_pvalue(analysis.get("pValue")) <= 0.05), None)
        if best_analysis is None:
            best_analysis = next((analysis for analysis in analyses if analysis.get("paramValue") not in (None, "")), None)
        if best_analysis is None:
            best_analysis = analyses[0]

    if significant and (effect_values or cis):
        bucket = "effect_estimate_with_significance"
    elif significant:
        bucket = "significant_pvalue_only"
    elif effect_values or cis:
        bucket = "effect_estimate_no_significance"
    elif analyses:
        bucket = "analysis_reported_no_numeric_signal"
    else:
        bucket = "no_primary_analysis_structured"

    return {
        "primary_outcome_count": len(primary),
        "primary_analysis_count": len(analyses),
        "primary_pvalue_count": len(pvalues),
        "primary_significant_pvalue_count": len(significant),
        "primary_effect_value_count": len(effect_values),
        "primary_ci_count": len(cis),
        "best_primary_pvalue": min(pvalues) if pvalues else None,
        "best_primary_outcome_title": (best_analysis or {}).get("_outcome_title", ""),
        "best_primary_method": (best_analysis or {}).get("statisticalMethod", ""),
        "best_primary_param_type": (best_analysis or {}).get("paramType", ""),
        "best_primary_param_value": (best_analysis or {}).get("paramValue", ""),
        "best_primary_ci_lower": (best_analysis or {}).get("ciLowerLimit", ""),
        "best_primary_ci_upper": (best_analysis or {}).get("ciUpperLimit", ""),
        "best_primary_pvalue_raw": (best_analysis or {}).get("pValue", ""),
        "primary_signal_bucket": bucket,
        "has_adverse_events_module": bool((study.get("resultsSection") or {}).get("adverseEventsModule")),
    }


def leadership_bucket(study: dict[str, Any]) -> dict[str, Any]:
    protocol = study.get("protocolSection", {})
    sponsor_module = protocol.get("sponsorCollaboratorsModule", {})
    contacts = protocol.get("contactsLocationsModule", {})
    sponsor_name = sponsor_module.get("leadSponsor", {}).get("name", "")
    sponsor_class = sponsor_module.get("leadSponsor", {}).get("class", "")
    responsible_aff = sponsor_module.get("responsibleParty", {}).get("investigatorAffiliation", "")
    officials = contacts.get("overallOfficials") or []
    official_affiliations = [official.get("affiliation", "") for official in officials if official.get("affiliation")]

    african_locations = [
        location for location in contacts.get("locations", [])
        if location.get("country") in AFRICAN_COUNTRIES
    ]
    facilities = [location.get("facility", "") for location in african_locations if location.get("facility")]
    countries = [location.get("country", "") for location in african_locations if location.get("country")]

    local_reasons: list[str] = []
    sponsor_local_reasons: list[str] = []
    investigator_local_reasons: list[str] = []
    sponsor_texts = [("lead sponsor", sponsor_name)]
    investigator_texts = [("responsible party affiliation", responsible_aff)]
    investigator_texts.extend((f"overall official affiliation {index + 1}", value) for index, value in enumerate(official_affiliations))

    for label, text in sponsor_texts + investigator_texts:
        if not text:
            continue
        matched_current = False
        for country in sorted(set(countries)):
            if text_match(text, country):
                reason = f"{label} mentions African country `{country}`"
                local_reasons.append(reason)
                if label == "lead sponsor":
                    sponsor_local_reasons.append(reason)
                else:
                    investigator_local_reasons.append(reason)
                matched_current = True
                break
        if matched_current:
            continue
        for facility in facilities:
            if text_match(text, facility):
                reason = f"{label} matches African site facility `{facility}`"
                local_reasons.append(reason)
                if label == "lead sponsor":
                    sponsor_local_reasons.append(reason)
                else:
                    investigator_local_reasons.append(reason)
                break

    explicit_affiliation_text = [text for _, text in sponsor_texts + investigator_texts if text]
    sponsor_has_named_institution = bool(sponsor_name)
    sponsor_has_local_match = bool(sponsor_local_reasons)
    investigator_has_local_match = bool(investigator_local_reasons)

    if sponsor_has_local_match:
        bucket = "likely_locally_led"
        confidence = "medium"
        reason = sponsor_local_reasons[0]
    elif investigator_has_local_match and (sponsor_class in EXTERNAL_SPONSOR_CLASSES or sponsor_has_named_institution):
        bucket = "mixed_local_site_with_external_sponsor"
        confidence = "medium"
        if sponsor_class in EXTERNAL_SPONSOR_CLASSES:
            reason = f"{investigator_local_reasons[0]}; sponsor class is `{sponsor_class}`"
        else:
            reason = f"{investigator_local_reasons[0]}; named sponsor `{sponsor_name}` does not match African site institutions"
    elif sponsor_class in EXTERNAL_SPONSOR_CLASSES:
        bucket = "likely_externally_run"
        confidence = "medium"
        reason = f"lead sponsor class is `{sponsor_class}` and no local-affiliation match was found"
    elif explicit_affiliation_text:
        bucket = "likely_externally_run"
        confidence = "low"
        reason = "named sponsor or investigator affiliation is present, but it does not match African site institutions"
    else:
        bucket = "unclear"
        confidence = "low"
        reason = "registry fields do not give enough affiliation evidence"

    return {
        "lead_sponsor_name": sponsor_name,
        "leadership_bucket": bucket,
        "leadership_confidence": confidence,
        "leadership_reason": reason,
        "responsible_party_affiliation": responsible_aff,
        "overall_official_affiliations": " | ".join(official_affiliations),
    }


def score_priority(row: dict[str, Any]) -> float:
    base = parse_float(row.get("overall_efficiency_score")) or 0.0
    lead_bonus = {
        "likely_locally_led": 12.0,
        "mixed_local_site_with_external_sponsor": 6.0,
        "unclear": 2.0,
        "likely_externally_run": 0.0,
    }.get(str(row.get("leadership_bucket")), 0.0)
    signal_bonus = {
        "effect_estimate_with_significance": 10.0,
        "significant_pvalue_only": 7.0,
        "effect_estimate_no_significance": 5.0,
        "analysis_reported_no_numeric_signal": 2.0,
        "no_primary_analysis_structured": 0.0,
    }.get(str(row.get("primary_signal_bucket")), 0.0)
    result_bonus = 4.0 if str(row.get("has_result_reference")) == "True" else 0.0
    return round(base + lead_bonus + signal_bonus + result_bonus, 2)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def format_counter(counter: Counter[str], limit: int = 5) -> str:
    if not counter:
        return "none"
    return ", ".join(f"{name} ({count})" for name, count in counter.most_common(limit))


def main() -> None:
    _, processed_dir, africa_benchmark, africa_shortlist = resolve_layout()
    benchmark_rows = read_csv(africa_benchmark)
    shortlist_ids = {row["nct_id"] for row in read_csv(africa_shortlist)}
    studies = load_studies()

    enriched: list[dict[str, Any]] = []
    for row in benchmark_rows:
        study = studies.get(row["nct_id"])
        if not study:
            continue
        merged: dict[str, Any] = dict(row)
        merged.update(extract_signal_fields(study))
        merged.update(leadership_bucket(study))
        merged["in_transfer_shortlist"] = row["nct_id"] in shortlist_ids
        merged["followup_priority_score"] = score_priority(merged)
        enriched.append(merged)

    enriched.sort(key=lambda row: float(row["followup_priority_score"]), reverse=True)

    local_or_mixed = [
        row for row in enriched
        if row["leadership_bucket"] in {"likely_locally_led", "mixed_local_site_with_external_sponsor"}
    ]
    local_or_mixed.sort(key=lambda row: float(row["followup_priority_score"]), reverse=True)

    locally_led_only = [row for row in enriched if row["leadership_bucket"] == "likely_locally_led"]
    locally_led_only.sort(key=lambda row: float(row["followup_priority_score"]), reverse=True)

    relevant_ids = {nct_id for nct_id, study in studies.items() if is_malaria_relevant(study)}
    relevant_enriched = [row for row in enriched if row["nct_id"] in relevant_ids]
    relevant_local_or_mixed = [row for row in local_or_mixed if row["nct_id"] in relevant_ids]
    relevant_locally_led_only = [row for row in locally_led_only if row["nct_id"] in relevant_ids]

    write_csv(processed_dir / "malaria_deep_dive.csv", relevant_enriched)
    write_csv(processed_dir / "malaria_local_or_mixed_priority.csv", relevant_local_or_mixed)
    write_csv(processed_dir / "malaria_locally_led_priority.csv", relevant_locally_led_only)

    lead_counts = Counter(str(row["leadership_bucket"]) for row in relevant_enriched)
    shortlist_rows = [row for row in enriched if row["in_transfer_shortlist"]]
    relevant_shortlist_rows = [row for row in shortlist_rows if row["nct_id"] in relevant_ids]
    shortlist_lead_counts = Counter(str(row["leadership_bucket"]) for row in relevant_shortlist_rows)
    signal_counts = Counter(str(row["primary_signal_bucket"]) for row in relevant_enriched)

    local_country_counts: Counter[str] = Counter()
    for row in relevant_local_or_mixed[:20]:
        for country in str(row.get("africa_countries", "")).split("|"):
            country = country.strip()
            if country:
                local_country_counts.update([country])

    top_local_lines = []
    for row in relevant_locally_led_only[:10]:
        top_local_lines.append(
            f"- {row['nct_id']}: {row['brief_title']} | {row['africa_countries']} | "
            f"priority {row['followup_priority_score']} | signal {row['primary_signal_bucket']}"
        )

    top_mixed_lines = []
    for row in relevant_local_or_mixed[:10]:
        top_mixed_lines.append(
            f"- {row['nct_id']}: {row['brief_title']} | {row['leadership_bucket']} | "
            f"{row['africa_countries']} | priority {row['followup_priority_score']}"
        )

    summary = [
        "# Malaria Deep Dive",
        "",
        "This malaria-first layer adds two analytical layers on top of the existing benchmark and applies a topical validation pass to remove obvious off-topic registry hits:",
        "",
        "- structured primary-outcome signal extraction from `resultsSection`",
        "- a cautious leadership heuristic using sponsor names, investigator affiliations, and African site institutions",
        "",
        "## Coverage",
        "",
        f"- Registry benchmark studies loaded: {len(enriched)}",
        f"- Malaria-relevant studies after topical validation: {len(relevant_enriched)}",
        f"- Transfer shortlist studies after topical validation: {len(relevant_shortlist_rows)}",
        f"- Studies with structured primary analyses: {sum(int(row['primary_analysis_count']) > 0 for row in relevant_enriched)}",
        f"- Studies with primary p-values: {sum(int(row['primary_pvalue_count']) > 0 for row in relevant_enriched)}",
        f"- Studies with primary effect estimates or CIs: {sum((int(row['primary_effect_value_count']) > 0) or (int(row['primary_ci_count']) > 0) for row in relevant_enriched)}",
        "",
        "## Leadership Heuristic",
        "",
        f"- All studies: {format_counter(lead_counts)}",
        f"- Transfer shortlist only: {format_counter(shortlist_lead_counts)}",
        "",
        "These leadership labels are heuristics, not definitive authorship or funding adjudications.",
        "",
        "## Primary Signal Buckets",
        "",
        f"- {format_counter(signal_counts)}",
        "",
        "## What Looks Most Transferable",
        "",
        "- The strongest malaria pattern remains single-country, often single-site trials with moderate enrollment.",
        f"- Countries most represented among the top topical-validated local-or-mixed candidates: {format_counter(local_country_counts)}",
        "- Mixed local-site participation may be more operationally informative than clearly external sponsor-led studies, but the leadership split remains heuristic.",
        "",
        "## Top Likely Local Candidates",
        "",
    ]
    summary.extend(top_local_lines if top_local_lines else ["- none identified"])
    summary.extend([
        "",
        "## Top Local-Or-Mixed Candidates",
        "",
    ])
    summary.extend(top_mixed_lines if top_mixed_lines else ["- none identified"])
    summary.extend([
        "",
        "## Caveat",
        "",
        "A statistically significant primary result is not the same as real-world effectiveness, the leadership split is an inference from registry metadata, and the deep-dive layer excludes obvious off-topic registry hits from the displayed candidate set.",
    ])
    (processed_dir / "malaria_deep_dive_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
