# Edge Command UI Skill Comparison

This comparison tests how different prompting / skill modes handle the same realistic B2B edge-command UI task.

## Scenario

Design a Web B2B console for an industrial edge command platform. The UI should cover:

- Command Center Overview
- Alert Triage
- Command Approval Drawer

The target product includes edge nodes, missions, devices, alerts, command receipts, AI recommendations, permission limits, destructive actions, and audit replay.

## Compared Runs

| Run | Intent | Score | Grade | Result |
| --- | --- | ---: | --- | --- |
| `control-no-skill` | Generic dashboard with no explicit UI skill | 64 | fail | Too generic; misses AI-friendly structure and page workflow depth |
| `generic-design-skill` | General design-system page output | 79 | borderline | Better hierarchy, still misses MAOS-level safety, state, and implementation discipline |
| `maos-ui-designer` | MAOS workflow with B2B, industrial IoT, AI-friendly UI, and command safety constraints | 100 | marketplace | Passes every rubric dimension |

## Artifacts

Each run contains:

- `prompt.md`
- `design-brief.md`
- `screen-spec.md`
- `prototype.html`
- `evaluation.json`

Screenshots were generated during validation and can be recreated from each `prototype.html` with the commands below. They are not committed to keep the marketplace repository lightweight.

## Evaluation Command

```powershell
python scripts/evaluate_ui_comparison.py docs\comparison\edge-command-ui\control-no-skill --json
python scripts/evaluate_ui_comparison.py docs\comparison\edge-command-ui\generic-design-skill --json
python scripts/evaluate_ui_comparison.py docs\comparison\edge-command-ui\maos-ui-designer --json
```

## Screenshot Command

The screenshots were captured with Playwright using Microsoft Edge:

```powershell
pnpm dlx playwright screenshot --channel msedge --viewport-size=1440,1000 --full-page <file-url> screenshot-desktop.png
pnpm dlx playwright screenshot --channel msedge --viewport-size=390,844 --full-page <file-url> screenshot-mobile.png
```

The validation run used desktop viewport `1440x1000` and mobile viewport `390x844`.

## Rubric

The evaluator scores seven dimensions:

- Product-specific B2B workflow: 18
- Information architecture and page coverage: 16
- AI-friendly implementation structure: 20
- B2B component realism: 14
- Operational state coverage: 18
- Visual maturity and density: 8
- Responsive and screenshot readiness: 6

## Findings

The control output looks clean, but it behaves like a generic dashboard: it lacks a real command approval model, stable implementation hooks, and safety states.

The generic design-skill output improves layout and design-system consistency, but it still treats the product as a normal operations dashboard instead of a high-risk edge-command workflow.

The `maos-ui-designer` output produces a more implementation-ready interface: it names domain components, defines state boundaries, uses Ant Design-style B2B primitives through domain wrappers, adds StyleX/token guidance, includes stable selectors, and models permission-limited command approval.

## Next Comparison Extensions

- Add `maos-ui-designer + figma-generate-design` for editable design-file output.
- Add `maos-ui-designer + figma-generate-diagram` for architecture/flow diagram pairing.
- Add a real React + Ant Design implementation pass and compare DOM/testability directly.
