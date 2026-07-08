# MAOS UI Designer

MAOS UI Designer is a Codex plugin that provides an AI-friendly product UI design workflow for frontend, SaaS, admin, mobile, CLI/TUI, Figma, and design-system work.

It helps Codex clarify product context, select agent-maintainable frontend frameworks and UI component libraries, define design tokens and StyleX/Tailwind/UI-kit choices, and verify polished app screens.

## Install

Add this repository as a Codex plugin marketplace, then install:

```powershell
codex plugin marketplace add https://github.com/LeoWangTiny/maos-ui-designer
codex plugin add maos-ui-designer@maos
```

## Use

```text
Use $maos-ui-designer to clarify the product context, choose an AI-friendly UI framework, and design or review this interface.
```

## Tests

Run the MAOS capability-map golden test:

```powershell
python -m unittest discover -s tests -v
```

Score a generated response:

```powershell
python scripts/evaluate_capability_map.py path\to\response.md --json
```

See `docs/tests/maos-capability-map-golden-test.md` for the full rubric.

### Latest Evaluation

The full-coverage generated sample is available at:

- `docs/examples/maos-capability-map-full-coverage.md`

Evaluation command:

```powershell
python scripts/evaluate_capability_map.py docs\examples\maos-capability-map-full-coverage.md --json
```

Latest result:

```text
score: 100
passed: true
marketplace_grade: true
missing: []
```

Dimension scores:

```text
Clarifying question discipline: 15/15
Design context axes: 15/15
AI-friendly framework gate: 20/20
Capability map completeness: 20/20
B2B component library judgment: 10/10
States and operational boundaries: 10/10
Implementation acceptance checklist: 10/10
```

## Developer

- Developer: zxztai
- Website: https://maos.zxztai.com
