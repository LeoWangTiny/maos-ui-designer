#!/usr/bin/env python3
"""Evaluate MAOS UI Designer capability-map responses.

The evaluator is intentionally heuristic. It checks whether a generated response
contains the durable design decisions that make a capability map useful for
implementation and future agent maintenance.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


Criterion = dict[str, object]


CRITERIA: list[Criterion] = [
    {
        "name": "Clarifying question discipline",
        "weight": 15,
        "groups": [
            ["clarifying question", "clarification"],
            ["three", "3", "no more than three"],
            ["surface", "responsive web", "figma", "cli", "tui"],
            ["framework", "ui kit", "component library"],
            ["risk", "safety", "permission", "approval"],
        ],
    },
    {
        "name": "Design context axes",
        "weight": 15,
        "groups": [
            ["industry", "industrial", "iot", "edge"],
            ["style", "command-center", "command center", "operational", "data-dense"],
            ["palette", "color", "semantic"],
            ["surface", "web", "responsive"],
            ["density", "compact", "daily-use"],
            ["risk", "high risk", "safety-critical"],
        ],
    },
    {
        "name": "AI-friendly framework gate",
        "weight": 20,
        "groups": [
            ["ai-friendly", "agent-maintainable", "agent maintainable"],
            ["typed api", "typescript", "typed props", "typed table", "typed columns"],
            ["token", "theme", "theming", "configprovider"],
            ["semantic wrapper", "domain wrapper", "wrappers"],
            ["accessibility", "a11y", "keyboard", "focus"],
            ["stable testing", "stable selector", "data-testid", "rowkey"],
            ["predictable styling", "stylex", "tailwind", "css modules"],
        ],
    },
    {
        "name": "Capability map completeness",
        "weight": 20,
        "groups": [
            ["```mermaid", "flowchart", "graph tb", "graph lr"],
            ["input intake", "brief", "screenshot", "codebase"],
            ["clarification layer", "clarifying"],
            ["design context"],
            ["framework gate", "ai-friendly framework"],
            ["product model", "mission", "edge node", "device", "alert", "command"],
            ["information architecture", "ia"],
            ["component system", "missiontable", "commanddrawer", "alerttimeline"],
            ["state system", "loading", "empty", "error"],
            ["visualization", "chart", "topology", "trend"],
            ["permission", "safety", "approval", "audit"],
            ["token", "styling"],
            ["responsive qa", "desktop", "mobile"],
            ["accessibility", "test hooks", "handoff"],
        ],
    },
    {
        "name": "B2B component library judgment",
        "weight": 10,
        "groups": [
            ["ant design"],
            ["b2b", "admin", "enterprise"],
            ["configprovider", "theme token", "tokens"],
            ["domain wrapper", "semantic wrapper", "wrappers"],
            ["table", "form", "drawer", "modal"],
        ],
    },
    {
        "name": "States and operational boundaries",
        "weight": 10,
        "groups": [
            ["loading", "skeleton"],
            ["empty"],
            ["error", "retry"],
            ["stale", "partial"],
            ["disconnected"],
            ["permission-limited", "permission limited", "role gate"],
            ["command pending", "receipt pending", "timeout", "failed"],
            ["destructive", "confirmation", "two-person approval", "approval"],
        ],
    },
    {
        "name": "Implementation acceptance checklist",
        "weight": 10,
        "groups": [
            ["acceptance checklist", "qa acceptance checklist", "验收"],
            ["implementation", "handoff", "guardrails"],
            ["domain wrappers", "semantic tokens", "stylex"],
            ["stable selectors", "data-testid", "rowkey"],
            ["typed charts", "chart adapters", "echarts", "antv"],
            ["desktop", "mobile", "responsive"],
        ],
    },
]


PASSING_SCORE = 80
MARKETPLACE_SCORE = 90


def _contains_any(text: str, terms: Iterable[str]) -> bool:
    return any(term.lower() in text for term in terms)


def _criterion_score(text: str, criterion: Criterion) -> tuple[float, bool]:
    groups = criterion["groups"]
    assert isinstance(groups, list)
    matched = sum(1 for group in groups if _contains_any(text, group))
    ratio = matched / len(groups)
    weight = float(criterion["weight"])
    return weight * ratio, ratio >= 0.8


def evaluate(response: str) -> dict[str, object]:
    normalized = response.lower()
    score = 0.0
    details: dict[str, float] = {}
    missing: list[str] = []

    for criterion in CRITERIA:
        criterion_score, satisfied = _criterion_score(normalized, criterion)
        name = str(criterion["name"])
        details[name] = round(criterion_score, 2)
        score += criterion_score
        if not satisfied:
            missing.append(name)

    rounded_score = round(score)
    return {
        "score": rounded_score,
        "passed": rounded_score >= PASSING_SCORE and not missing,
        "marketplace_grade": rounded_score >= MARKETPLACE_SCORE and not missing,
        "missing": missing,
        "details": details,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate a MAOS UI capability-map response.")
    parser.add_argument("response", type=Path, help="Markdown response file to evaluate.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    result = evaluate(args.response.read_text(encoding="utf-8"))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Score: {result['score']}")
        print(f"Passed: {result['passed']}")
        if result["missing"]:
            print("Missing:")
            for item in result["missing"]:
                print(f"- {item}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
