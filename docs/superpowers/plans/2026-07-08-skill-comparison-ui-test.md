# Skill Comparison UI Test Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repeatable comparison test that shows how `maos-ui-designer` performs against a no-skill control and a generic design-skill baseline on a realistic edge-command B2B UI task.

**Architecture:** The comparison is static and repository-native: each skill run has its own prompt, design brief, screen spec, prototype HTML, evaluation JSON, and screenshots. A Python evaluator scores the artifacts with weighted rules for product maturity, AI-friendly structure, B2B realism, state coverage, and responsive readiness.

**Tech Stack:** Markdown fixtures, static HTML/CSS prototypes, Python standard library evaluator/tests, Playwright/browser screenshots through bundled runtime where available.

## Global Constraints

- Do not add package dependencies.
- Keep prototypes static and browser-openable from the filesystem.
- Compare the same business scenario for both groups.
- First version includes `control-no-skill`, `generic-design-skill`, and `maos-ui-designer`.
- Preserve existing capability-map tests.
- Use stable selectors and artifact paths so future agents can extend the comparison.

---

### Task 1: Add Comparison Evaluator Contract

**Files:**
- Create: `tests/test_ui_comparison_evaluator.py`
- Create: `tests/fixtures/ui_comparison_control_fixture.md`
- Create: `tests/fixtures/ui_comparison_maos_fixture.md`
- Create: `scripts/evaluate_ui_comparison.py`

**Interfaces:**
- Produces: `evaluate_artifact(markdown: str, html: str) -> dict[str, object]`
- Produces: `compare(control: dict[str, object], maos: dict[str, object]) -> dict[str, object]`
- The result dict includes `score`, `passed`, `grade`, `missing`, and `details`.

- [ ] **Step 1: Write failing tests**

Test that the MAOS fixture scores at least 90, the control fixture scores below MAOS, and MAOS wins the comparison.

- [ ] **Step 2: Run tests to verify RED**

Run: `python -m unittest discover -s tests -v`

Expected: tests fail because `scripts/evaluate_ui_comparison.py` does not exist.

- [ ] **Step 3: Implement evaluator**

Implement the weighted rubric in `scripts/evaluate_ui_comparison.py` with no external dependencies.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python -m unittest discover -s tests -v`

Expected: all existing tests and new comparison tests pass.

### Task 2: Generate Comparison Artifacts

**Files:**
- Create directory: `docs/comparison/edge-command-ui/control-no-skill/`
- Create directory: `docs/comparison/edge-command-ui/generic-design-skill/`
- Create directory: `docs/comparison/edge-command-ui/maos-ui-designer/`
- Create: `prompt.md`, `design-brief.md`, `screen-spec.md`, `prototype.html`, `evaluation.json` for each group.

**Interfaces:**
- Each group has a static `prototype.html`.
- Each group includes `data-eval-*` attributes used by the evaluator and browser checks.

- [ ] **Step 1: Create shared scenario prompt**

The prompt asks for three screens: command center overview, alert triage, and command approval.

- [ ] **Step 2: Create control artifacts**

The control artifacts intentionally represent a plausible generic dashboard output without MAOS-specific discipline.

- [ ] **Step 3: Create generic design-skill artifacts**

The generic design-skill artifacts represent a general design-system page that improves layout but does not add MAOS-specific industrial workflow or AI-friendly implementation discipline.

- [ ] **Step 4: Create MAOS artifacts**

The MAOS artifacts apply industrial IoT context, AI-friendly gate, Ant Design-style B2B structure, semantic tokens, product components, states, and QA hooks.

- [ ] **Step 5: Score all groups**

Run: `python scripts/evaluate_ui_comparison.py docs/comparison/edge-command-ui/control-no-skill --json > docs/comparison/edge-command-ui/control-no-skill/evaluation.json`

Run: `python scripts/evaluate_ui_comparison.py docs/comparison/edge-command-ui/generic-design-skill --json > docs/comparison/edge-command-ui/generic-design-skill/evaluation.json`

Run: `python scripts/evaluate_ui_comparison.py docs/comparison/edge-command-ui/maos-ui-designer --json > docs/comparison/edge-command-ui/maos-ui-designer/evaluation.json`

### Task 3: Capture Screenshots

**Files:**
- Generated locally during validation: desktop and mobile screenshots for each `prototype.html`
- Do not commit screenshot binaries unless a future marketplace policy requires visual thumbnails.

**Interfaces:**
- Screenshots are generated from each `prototype.html`.

- [ ] **Step 1: Check browser automation availability**

Run Node/Playwright availability checks using bundled runtime first.

- [ ] **Step 2: Capture desktop and mobile screenshots**

Use desktop viewport `1440x1000` and mobile viewport `390x844`.

- [ ] **Step 3: Verify screenshots render and are non-empty**

Run file-size checks for the generated screenshot outputs before deleting or excluding them from the committed marketplace package.

### Task 4: Document And Publish Results

**Files:**
- Modify: `README.md`
- Create: `docs/comparison/edge-command-ui/README.md`

**Interfaces:**
- README links to comparison artifacts and summarizes both scores.

- [ ] **Step 1: Add comparison summary**

Include commands, paths, and score table.

- [ ] **Step 2: Run final verification**

Run evaluator tests, capability-map tests, comparison scoring, and remote git status checks.

- [ ] **Step 3: Commit and push**

Commit message: `Add MAOS UI skill comparison test`
