# Lean Africa-site malaria RCTs as a transfer template

This repository packages a local E156 micro-paper, protocol draft, data extracts, and reproducibility files for a registry-first scan of Africa-site randomized trials.

## Research Question

The primary descriptive question is how often Africa-site trials in this topic meet a pragmatic shortlist for cheaper and faster delivery.

## Current Result

- Africa benchmark trials: `80`
- Transfer shortlist trials: `27`
- Shortlist proportion: `0.34` with Wilson 95% interval `0.24` to `0.45`
- Median trial duration days: `619.0`
- Median results-reporting lag days: `719.5`
- Most represented Africa-site countries: Kenya (22), Uganda (18), Mali (17), Burkina Faso (16), Ghana (11)

## Submission Track

- Primary target journal: `Malaria Journal` as a `Research` article
- Backup target journal: `Trials` if the manuscript is judged too methods-oriented for a malaria-only venue
- Journal-specific submission files live in `submission/`

## Layout

- `paper/`: E156 body, article JSON, validation record, and HTML bundle
- `protocol/`: submission-oriented protocol draft
- `data/`: copied topic outputs from the parent analysis project
- `code/`: local scripts needed to rerun validation and rebuild the bundle
- `.github/workflows/`: lightweight validation workflow for GitHub-hosted use
- `submission/`: journal-specific cover letter, abstract, title page, manuscript draft, declarations, and checklist
- `STATUS.md`: current completion state and remaining gaps

## Quick Start

Validate the E156 body:

```bash
python3 code/validate_e156.py --file paper/article.json --json-field body
```

Rebuild the HTML bundle:

```bash
python3 code/build_e156_bundle.py --input paper/article.json --output paper/index.html --template templates/e156_interactive_template.html
```

## Status

- Local E156 body validated
- Local HTML bundle generated
- Protocol tightened beyond the initial skeleton
- Local git repo initialized
- Public GitHub repository is live at `https://github.com/mahmood726-cyber/malaria-e156`
- Journal-specific submission package drafted for `Malaria Journal`
