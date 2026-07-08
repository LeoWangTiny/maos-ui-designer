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
| `control-no-skill` | Generic dashboard with no explicit UI skill | 41 | fail | Too generic; misses layout formation, AI-friendly structure, module coherence, and responsive layout discipline |
| `generic-design-skill` | General design-system page output | 52 | fail | Better product framing, still misses formation selection, structural layout gates, and selected-object workflow coherence |
| `maos-ui-designer` | MAOS workflow with B2B, industrial IoT, AI-friendly UI, and command safety constraints | 99 | marketplace | Passes layout formation, structural layout, module coherence, responsive overflow, and workflow-depth gates |

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

## Layout Verification

The MAOS prototype was also checked in a real browser for page-level overflow:

```text
desktop htmlClient=1440 htmlScroll=1440 bodyClient=1440 bodyScroll=1440
mobile  htmlClient=390  htmlScroll=390  bodyClient=390  bodyScroll=390
```

The mobile mission table is allowed to scroll inside `.table-scroll`; the page itself must not scroll horizontally.

## Rubric

The evaluator scores eleven dimensions. The first seven check product and implementation coverage; the last four are structural gates that prevent keyword-only artifacts from passing:

- Product-specific B2B workflow: 11
- Information architecture and page coverage: 10
- AI-friendly implementation structure: 11
- B2B component realism: 8
- Operational state coverage: 10
- Visual maturity and density: 5
- Responsive and screenshot readiness: 3
- Layout formation confirmation: 12
- Layout integrity and alignment: 10
- Module coherence and product model: 10
- Responsive behavior and overflow control: 10

## Findings

The control output looks clean, but it behaves like a generic dashboard: it lacks a layout formation decision, a real command approval model, stable implementation hooks, selected-object context, and responsive layout controls.

The generic design-skill output improves product framing and design-system consistency, but it still treats the product as a normal operations dashboard instead of a high-risk selected-mission workflow. It does not provide enough structural evidence for formation choice, alignment, module coherence, or mobile overflow control.

The `maos-ui-designer` output now explicitly chooses a selected-mission workbench formation: mission queue, edge node health, alert triage, evidence, and command approval all share one `data-context`. It names domain components, defines state boundaries, uses Ant Design-style B2B primitives through domain wrappers, adds StyleX/token guidance, includes stable selectors, rejects weaker formations, and models permission-limited command approval with responsive overflow guards.

## Next Comparison Extensions

- Add `maos-ui-designer + figma-generate-design` for editable design-file output.
- Add `maos-ui-designer + figma-generate-diagram` for architecture/flow diagram pairing.
- Add a real React + Ant Design implementation pass and compare DOM/testability directly.
