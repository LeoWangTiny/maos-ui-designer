#!/usr/bin/env python3
"""Evaluate edge-command UI comparison artifacts.

This scores a static page design artifact, not the runtime correctness of a
frontend app. The rubric rewards product-specific B2B UI structure,
AI-friendly maintainability, operational states, and responsive/test hooks.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


Criterion = dict[str, object]


CRITERIA: list[Criterion] = [
    {
        "name": "Product-specific B2B workflow",
        "weight": 18,
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
        "weight": 16,
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
        "weight": 20,
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
        "weight": 14,
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
        "weight": 18,
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
        "weight": 8,
        "groups": [
            ["compact", "dense", "daily-use", "daily use"],
            ["neutral", "semantic", "warning", "danger", "success"],
            ["not landing", "no hero", "real product surface"],
            ["alignment", "stable dimensions", "responsive"],
        ],
    },
    {
        "name": "Responsive and screenshot readiness",
        "weight": 6,
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


def evaluate_artifact(markdown: str, html: str) -> dict[str, object]:
    text = f"{markdown}\n{html}".lower()
    total = 0.0
    details: dict[str, float] = {}
    missing: list[str] = []

    for criterion in CRITERIA:
        score, satisfied = _score_criterion(text, criterion)
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
