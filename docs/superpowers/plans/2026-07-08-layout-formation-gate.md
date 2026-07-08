# Layout Formation Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Teach MAOS UI Designer to confirm the page layout formation before visual design or component detail work.

**Architecture:** Add a reusable layout formation reference, connect it to the MAOS skill workflow, and extend the UI comparison evaluator so artifacts must show formation choice, primary/secondary regions, rejected alternatives, and responsive collapse behavior.

**Tech Stack:** Codex skill Markdown, Python unittest, static HTML/CSS comparison fixtures.

## Global Constraints

- Keep the skill marketable and concise; put detailed formation catalog in `references/layout-formation.md`.
- Layout formation is a behavior-shaping contract, not a decorative style list.
- The evaluator must fail keyword-rich artifacts that do not declare a real formation.

---

### Task 1: Test The Missing Gate

**Files:**
- Modify: `tests/test_ui_comparison_evaluator.py`
- Create: `tests/test_maos_skill_contract.py`

- [x] **Step 1: Write failing tests**

Tests assert that the skill requires layout formation before visual design and that evaluator details include `Layout formation confirmation`.

- [x] **Step 2: Run tests to verify failure**

Run: `python -m unittest tests.test_maos_skill_contract tests.test_ui_comparison_evaluator -v`

Expected: FAIL because the skill and evaluator do not yet contain the formation gate.

### Task 2: Add The Skill Reference

**Files:**
- Create: `plugins/maos-ui-designer/skills/maos-ui-designer/references/layout-formation.md`
- Modify: `plugins/maos-ui-designer/skills/maos-ui-designer/SKILL.md`

- [x] **Step 1: Add formation catalog**

Document List + Detail, Workbench, Dashboard + Drilldown, Wizard / Stepper, Canvas + Inspector, and Terminal/TUI Pane.

- [x] **Step 2: Connect main workflow**

Add layout formation as a required gate after product modeling and before visual design.

### Task 3: Upgrade Evaluator And Fixtures

**Files:**
- Modify: `scripts/evaluate_ui_comparison.py`
- Modify: `tests/fixtures/ui_comparison_maos_fixture.md`
- Modify: `docs/comparison/edge-command-ui/maos-ui-designer/*.md`
- Modify: `docs/comparison/edge-command-ui/maos-ui-designer/prototype.html`

- [x] **Step 1: Add formation criterion**

Add `Layout formation confirmation` with checks for selected formation, primary object, primary/secondary regions, rejected formations, and responsive collapse.

- [x] **Step 2: Recompute evaluation results**

Run all three UI comparison evaluations and update JSON/README.

### Task 4: Verify And Publish

- [x] **Step 1: Run full tests**

Run: `python -m unittest discover -s tests -v`

- [x] **Step 2: Validate plugin and skill**

Run local plugin/skill checks.

- [x] **Step 3: Commit and push**

Commit the changes and push `main`.
