#!/usr/bin/env python3
"""Evaluate edge-command UI comparison artifacts.

This scores a static page design artifact, not the runtime correctness of a
frontend app. The rubric rewards product-specific B2B UI structure,
AI-friendly maintainability, operational states, responsive/test hooks, and
static structural evidence that the page is aligned, coherent, and mobile-safe.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Callable, Iterable


Criterion = dict[str, object]
StructuralCheck = Callable[[str, str, str], bool]


KEYWORD_CRITERIA: list[Criterion] = [
    {
        "name": "Product-specific B2B workflow",
        "weight": 11,
        "groups": [
            ["edge command", "edge-command", "industrial", "iot"],
            ["command center", "command-center", "operations", "operational"],
            ["mission", "edge node", "device", "alert", "command", "receipt"],
            ["alert triage", "triage", "evidence", "escalation"],
            ["approval", "audit", "policy", "safety"],
        ],
    },
    {
        "name": "Information architecture and page coverage",
        "weight": 10,
        "groups": [
            ["command center overview", "commandcenteroverview", "overview"],
            ["alert triage", "alerttriage"],
            ["command approval", "commandapproval", "command drawer", "approval drawer"],
            ["filters", "tabs", "search", "sorting", "queue"],
            ["table", "timeline", "drawer", "detail", "panel"],
            ["primary action", "secondary action", "bulk", "acknowledge"],
        ],
    },
    {
        "name": "AI-friendly implementation structure",
        "weight": 11,
        "groups": [
            ["ai-friendly", "agent-maintainable", "agent maintainable"],
            ["semantic tokens", "tokens", "theme", "configprovider"],
            ["domain wrapper", "semantic wrapper", "wrappers"],
            ["typed api", "typescript", "typed columns", "typed props"],
            ["data-testid", "stable selector", "stable selectors", "rowkey", "row key"],
            ["accessibility", "keyboard", "focus", "labels"],
            ["stylex", "tailwind", "css modules", "predictable styling"],
        ],
    },
    {
        "name": "B2B component realism",
        "weight": 8,
        "groups": [
            ["ant design", "antd", "b2b", "admin"],
            ["table", "form", "drawer", "modal"],
            ["tag", "badge", "timeline", "tabs"],
            ["missiontable", "commanddrawer", "alerttimeline", "evidenceviewer"],
            ["echarts", "antv", "chart adapter", "chart"],
        ],
    },
    {
        "name": "Operational state coverage",
        "weight": 10,
        "groups": [
            ["loading", "skeleton"],
            ["empty"],
            ["error", "retry"],
            ["stale", "partial"],
            ["disconnected", "offline"],
            ["permission-limited", "permission limited", "role gate"],
            ["command pending", "receipt pending", "timeout"],
            ["failed"],
            ["destructive", "confirmation", "two-person approval", "approval"],
        ],
    },
    {
        "name": "Visual maturity and density",
        "weight": 5,
        "groups": [
            ["compact", "dense", "daily-use", "daily use"],
            ["neutral", "semantic", "warning", "danger", "success"],
            ["not landing", "no hero", "real product surface"],
            ["alignment", "stable dimensions", "responsive"],
        ],
    },
    {
        "name": "Responsive and screenshot readiness",
        "weight": 3,
        "groups": [
            ["desktop", "mobile", "tablet", "responsive"],
            ["screenshot", "viewport", "playwright"],
            ["data-eval", "data-testid"],
        ],
    },
]


PASSING_SCORE = 80
MARKETPLACE_SCORE = 90


def _contains_any(text: str, terms: Iterable[str]) -> bool:
    return any(term.lower() in text for term in terms)


def _score_criterion(text: str, criterion: Criterion) -> tuple[float, bool]:
    groups = criterion["groups"]
    assert isinstance(groups, list)
    matched = sum(1 for group in groups if _contains_any(text, group))
    ratio = matched / len(groups)
    weight = float(criterion["weight"])
    return weight * ratio, ratio >= 0.75


def _contains_all(text: str, terms: Iterable[str]) -> bool:
    return all(term.lower() in text for term in terms)


def _has_regex(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL) is not None


def _has_layout_shell(markdown: str, html: str, text: str) -> bool:
    return _contains_any(html, ['data-layout="command-workbench"', "workbench-grid"]) and _has_regex(
        html, r"grid-template-columns\s*:\s*[^;]*minmax"
    )


def _has_spacing_tokens(markdown: str, html: str, text: str) -> bool:
    return _contains_all(html, ["--space-", "--radius-", "--border"])


def _has_explicit_table_columns(markdown: str, html: str, text: str) -> bool:
    return "<colgroup" in html.lower() and _contains_any(html, ["data-column=", "col style", "col class"])


def _has_aligned_panel_roles(markdown: str, html: str, text: str) -> bool:
    return _contains_all(html, ['data-layout-role="primary"', 'data-layout-role="context"']) and _contains_any(
        html, ["section-head", "panel-head", "module-head"]
    )


def _has_stable_dynamic_dimensions(markdown: str, html: str, text: str) -> bool:
    return _contains_any(html, ["min-height:", "grid-auto-rows", "aspect-ratio"]) and _contains_any(
        html, ["minmax(0, 1fr)", "minmax(320px", "clamp("]
    )


def _has_layout_formation_declared(markdown: str, html: str, text: str) -> bool:
    return _contains_any(
        text,
        ["layout formation", "data-layout-formation", "formation gate", "page formation"],
    )


def _has_formation_choice(markdown: str, html: str, text: str) -> bool:
    return _contains_any(
        text,
        [
            "list + detail",
            "list-detail",
            "workbench",
            "dashboard + drilldown",
            "dashboard-drilldown",
            "wizard / stepper",
            "wizard",
            "stepper",
            "canvas + inspector",
            "canvas-inspector",
            "terminal/tui pane",
            "terminal pane",
            "tui pane",
        ],
    )


def _has_formation_regions(markdown: str, html: str, text: str) -> bool:
    return _contains_all(text, ["primary object", "primary region", "secondary region"]) or _contains_all(
        html,
        ['data-layout-role="primary"', 'data-layout-role="context"', "data-selected-mission"],
    )


def _has_formation_responsive_collapse(markdown: str, html: str, text: str) -> bool:
    return _contains_all(text, ["desktop", "tablet", "mobile"]) and _contains_any(
        text,
        ["responsive collapse", "collapse", "mobile-task-first", "mobile-context-first", "data-responsive-strategy"],
    )


def _has_rejected_formations(markdown: str, html: str, text: str) -> bool:
    return _contains_any(text, ["rejected formations", "rejected formation", "avoid formation"]) and _contains_any(
        text,
        ["not appropriate", "not use", "too linear", "hides", "avoid"],
    )


def _has_selected_object_context(markdown: str, html: str, text: str) -> bool:
    return _contains_any(html, ["data-selected-mission", "data-selected-object"]) and _has_regex(
        html, r'data-context\s*=\s*"mission:[^"]+"'
    )


def _has_shared_context_modules(markdown: str, html: str, text: str) -> bool:
    contexts = re.findall(r'data-context\s*=\s*"([^"]+)"', html, flags=re.IGNORECASE)
    return any(contexts.count(context) >= 3 for context in set(contexts))


def _has_module_purpose_metadata(markdown: str, html: str, text: str) -> bool:
    return html.lower().count("data-module-purpose=") >= 4


def _has_object_relationships(markdown: str, html: str, text: str) -> bool:
    return _contains_all(
        text,
        ["mission", "edge node", "alert", "evidence", "command approval", "receipt"],
    )


def _has_contextual_action_model(markdown: str, html: str, text: str) -> bool:
    return _contains_all(text, ["selected mission", "request approval", "block dispatch"]) and _contains_any(
        html, ["data-action-scope", "data-primary-action"]
    )


def _has_viewport_meta(markdown: str, html: str, text: str) -> bool:
    return "viewport" in html.lower() and "width=device-width" in html.lower()


def _has_multiple_breakpoints(markdown: str, html: str, text: str) -> bool:
    return len(re.findall(r"@media\s*\(max-width", html, flags=re.IGNORECASE)) >= 2


def _has_page_overflow_guard(markdown: str, html: str, text: str) -> bool:
    return _contains_any(html, ["overflow-x: hidden", "overflow-x:hidden"]) and _contains_any(
        html, ["max-width: 100%", "width: 100%"]
    )


def _has_internal_table_scroll(markdown: str, html: str, text: str) -> bool:
    return "table-scroll" in html.lower() and _has_regex(html, r"\.table-scroll[^{]*\{[^}]*overflow-x\s*:\s*auto")


def _has_mobile_strategy_metadata(markdown: str, html: str, text: str) -> bool:
    return _contains_any(html, ["data-responsive-strategy", "data-mobile-order"]) and _contains_any(
        html, ["mobile-task-first", "mobile-context-first", "mobile-stack"]
    )


STRUCTURAL_CRITERIA: list[dict[str, object]] = [
    {
        "name": "Layout formation confirmation",
        "weight": 12,
        "checks": [
            _has_layout_formation_declared,
            _has_formation_choice,
            _has_formation_regions,
            _has_formation_responsive_collapse,
            _has_rejected_formations,
        ],
    },
    {
        "name": "Layout integrity and alignment",
        "weight": 10,
        "checks": [
            _has_layout_shell,
            _has_spacing_tokens,
            _has_explicit_table_columns,
            _has_aligned_panel_roles,
            _has_stable_dynamic_dimensions,
        ],
    },
    {
        "name": "Module coherence and product model",
        "weight": 10,
        "checks": [
            _has_selected_object_context,
            _has_shared_context_modules,
            _has_module_purpose_metadata,
            _has_object_relationships,
            _has_contextual_action_model,
        ],
    },
    {
        "name": "Responsive behavior and overflow control",
        "weight": 10,
        "checks": [
            _has_viewport_meta,
            _has_multiple_breakpoints,
            _has_page_overflow_guard,
            _has_internal_table_scroll,
            _has_mobile_strategy_metadata,
        ],
    },
]


def _score_structural_criterion(markdown: str, html: str, text: str, criterion: Criterion) -> tuple[float, bool]:
    checks = criterion["checks"]
    assert isinstance(checks, list)
    matched = sum(1 for check in checks if check(markdown, html, text))
    ratio = matched / len(checks)
    weight = float(criterion["weight"])
    return weight * ratio, ratio >= 0.75


def evaluate_artifact(markdown: str, html: str) -> dict[str, object]:
    markdown_lower = markdown.lower()
    html_lower = html.lower()
    text = f"{markdown_lower}\n{html_lower}"
    total = 0.0
    details: dict[str, float] = {}
    missing: list[str] = []

    for criterion in KEYWORD_CRITERIA:
        score, satisfied = _score_criterion(text, criterion)
        name = str(criterion["name"])
        details[name] = round(score, 2)
        total += score
        if not satisfied:
            missing.append(name)

    for criterion in STRUCTURAL_CRITERIA:
        score, satisfied = _score_structural_criterion(markdown_lower, html_lower, text, criterion)
        name = str(criterion["name"])
        details[name] = round(score, 2)
        total += score
        if not satisfied:
            missing.append(name)

    rounded = round(total)
    if rounded >= MARKETPLACE_SCORE and not missing:
        grade = "marketplace"
    elif rounded >= PASSING_SCORE:
        grade = "pass"
    elif rounded >= 70:
        grade = "borderline"
    else:
        grade = "fail"

    return {
        "score": rounded,
        "passed": rounded >= PASSING_SCORE and not missing,
        "grade": grade,
        "missing": missing,
        "details": details,
    }


def compare(control: dict[str, object], maos: dict[str, object]) -> dict[str, object]:
    control_score = int(control["score"])
    maos_score = int(maos["score"])
    delta = maos_score - control_score
    winner = "maos-ui-designer" if delta > 0 else "control-no-skill" if delta < 0 else "tie"
    return {
        "winner": winner,
        "control_score": control_score,
        "maos_score": maos_score,
        "score_delta": delta,
    }


def _read_optional(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def evaluate_directory(path: Path) -> dict[str, object]:
    markdown = "\n".join(
        [
            _read_optional(path / "design-brief.md"),
            _read_optional(path / "screen-spec.md"),
        ]
    )
    html = _read_optional(path / "prototype.html")
    result = evaluate_artifact(markdown, html)
    result["artifact"] = path.name
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate an edge-command UI comparison artifact.")
    parser.add_argument("artifact_dir", type=Path, help="Directory containing prompt/design/spec/prototype files.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    args = parser.parse_args()

    result = evaluate_directory(args.artifact_dir)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Artifact: {result['artifact']}")
        print(f"Score: {result['score']}")
        print(f"Grade: {result['grade']}")
        if result["missing"]:
            print("Missing:")
            for item in result["missing"]:
                print(f"- {item}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
