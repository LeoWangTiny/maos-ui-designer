# UI Comparison Layout Quality Fix Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the MAOS UI comparison test catch real layout, module-coherence, and responsive-quality failures instead of rewarding keyword-rich artifacts.

**Architecture:** Extend the existing static evaluator with structural HTML/CSS checks for alignment integrity, selected-object module coherence, and mobile overflow strategy. Rework the MAOS prototype into a selected-mission workbench where mission queue, node status, alert evidence, and command approval are aligned around one shared operational context.

**Tech Stack:** Python unittest evaluator, static HTML/CSS prototypes, Edge/Playwright-style screenshot validation.

## Global Constraints

- Keep the comparison repository lightweight; do not commit screenshot binaries.
- Preserve the three-run comparison shape: `control-no-skill`, `generic-design-skill`, and `maos-ui-designer`.
- Keep artifacts static and easy to inspect without a dev server.
- MAOS marketplace-grade output must pass structure checks, not only keyword coverage.

---

### Task 1: Add Layout Quality Regression Tests

**Files:**
- Modify: `tests/test_ui_comparison_evaluator.py`

**Interfaces:**
- Consumes: `evaluate_artifact(markdown: str, html: str) -> dict[str, object]`
- Consumes: `evaluate_directory(path: Path) -> dict[str, object]`
- Produces: regression expectations for layout integrity, module coherence, and responsive behavior.

- [x] **Step 1: Write failing tests**

Add tests proving that keyword-only artifacts fail structural quality, and that the committed MAOS prototype must expose the new hard criteria in `details`.

- [x] **Step 2: Run tests to verify failure**

Run: `python -m unittest tests.test_ui_comparison_evaluator -v`

Expected: FAIL because the evaluator does not yet expose layout/module/responsive hard criteria.

### Task 2: Upgrade Evaluator

**Files:**
- Modify: `scripts/evaluate_ui_comparison.py`
- Modify: `tests/fixtures/ui_comparison_maos_fixture.md`

**Interfaces:**
- Produces: new criteria names `Layout integrity and alignment`, `Module coherence and product model`, and `Responsive behavior and overflow control`.

- [x] **Step 1: Add structural checks**

Implement scoring based on HTML/CSS structure, shared selected-object context, explicit grid/colgroup constraints, and mobile overflow strategy.

- [x] **Step 2: Run tests to verify pass for fixtures**

Run: `python -m unittest tests.test_ui_comparison_evaluator -v`

Expected: PASS for MAOS fixture and expected failures for control fixture.

### Task 3: Rework MAOS Prototype

**Files:**
- Modify: `docs/comparison/edge-command-ui/maos-ui-designer/prototype.html`
- Modify: `docs/comparison/edge-command-ui/maos-ui-designer/design-brief.md`
- Modify: `docs/comparison/edge-command-ui/maos-ui-designer/screen-spec.md`

**Interfaces:**
- Produces: a selected-mission workbench with primary mission queue and contextual alert/evidence/approval panel.

- [x] **Step 1: Replace piled modules with one workbench grid**

Desktop: rail, topbar, posture summary, mission queue, context panel, and node strip align to the same grid.

- [x] **Step 2: Make mobile strategy explicit**

Mobile: no page-level horizontal overflow; task context appears before the table; only the mission table scrolls horizontally inside its container.

### Task 4: Re-score, Document, And Push

**Files:**
- Modify: `README.md`
- Modify: `docs/comparison/edge-command-ui/README.md`
- Modify: `docs/comparison/edge-command-ui/*/evaluation.json`

**Interfaces:**
- Produces: updated public comparison scores and verification notes.

- [x] **Step 1: Recompute all three evaluations**

Run evaluator for all three artifacts and update committed JSON.

- [x] **Step 2: Verify screenshots locally**

Generate desktop and mobile screenshots from the MAOS prototype, inspect alignment and overflow, then remove screenshot binaries before commit.

- [x] **Step 3: Run full verification and push**

Run: `python -m unittest discover -s tests -v`

Expected: all tests pass before committing and pushing to `main`.
