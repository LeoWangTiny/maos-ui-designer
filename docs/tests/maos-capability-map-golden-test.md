# MAOS Capability Map Golden Test

This test checks whether `maos-ui-designer` can produce a professional UI capability map for a complex B2B edge-command platform.

It is not a visual snapshot test. It evaluates whether the response contains the product, framework, component, state, token, safety, and QA decisions needed to guide implementation.

## Files

- `tests/fixtures/capability_map_prompt.md`: the fixed prompt for the skill.
- `tests/fixtures/capability_map_good.md`: a marketplace-grade reference response.
- `tests/fixtures/capability_map_bad.md`: a generic response that must fail.
- `scripts/evaluate_capability_map.py`: the scoring evaluator.
- `tests/test_capability_map_evaluator.py`: regression tests for the evaluator and fixtures.

## Run

```powershell
python -m unittest discover -s tests -v
```

To score a generated response:

```powershell
python scripts/evaluate_capability_map.py path\to\response.md --json
```

## Passing Standard

- `80+`: acceptable capability-map response.
- `90+`: marketplace-grade response.
- `<70`: the response is too generic or misses required design workflow decisions.

The evaluator uses seven weighted dimensions:

- Clarifying question discipline: 15
- Design context axes: 15
- AI-friendly framework gate: 20
- Capability map completeness: 20
- B2B component library judgment: 10
- States and operational boundaries: 10
- Implementation acceptance checklist: 10

## What This Protects

The test rejects responses that only say "make a modern dashboard" or draw a generic input-design-output diagram.

A passing response must show:

- Industry, style, palette, surface, density, and risk choices.
- AI-friendly framework selection before library choice.
- Ant Design judgment for Web B2B/admin work, with domain wrappers and token constraints.
- A capability map with product-specific nodes.
- State coverage for loading, empty, error, stale, disconnected, permission-limited, command pending, failed, and destructive actions.
- Implementation guardrails and a QA checklist that can guide real frontend work.
