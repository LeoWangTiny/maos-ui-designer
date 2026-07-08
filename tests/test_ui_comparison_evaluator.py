import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALUATOR_PATH = ROOT / "scripts" / "evaluate_ui_comparison.py"
FIXTURES = ROOT / "tests" / "fixtures"


def load_evaluator():
    spec = importlib.util.spec_from_file_location("evaluate_ui_comparison", EVALUATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class UIComparisonEvaluatorTest(unittest.TestCase):
    def test_maos_fixture_scores_as_marketplace_grade_page_design(self):
        evaluator = load_evaluator()
        fixture = (FIXTURES / "ui_comparison_maos_fixture.md").read_text(encoding="utf-8")

        result = evaluator.evaluate_artifact(fixture, fixture)

        self.assertGreaterEqual(result["score"], 90)
        self.assertEqual(result["grade"], "marketplace")
        self.assertEqual(result["missing"], [])

    def test_control_fixture_fails_maturity_threshold(self):
        evaluator = load_evaluator()
        fixture = (FIXTURES / "ui_comparison_control_fixture.md").read_text(encoding="utf-8")

        result = evaluator.evaluate_artifact(fixture, fixture)

        self.assertLess(result["score"], 70)
        self.assertIn("AI-friendly implementation structure", result["missing"])
        self.assertIn("Operational state coverage", result["missing"])

    def test_maos_beats_control_by_meaningful_margin(self):
        evaluator = load_evaluator()
        control = evaluator.evaluate_artifact(
            (FIXTURES / "ui_comparison_control_fixture.md").read_text(encoding="utf-8"),
            "",
        )
        maos = evaluator.evaluate_artifact(
            (FIXTURES / "ui_comparison_maos_fixture.md").read_text(encoding="utf-8"),
            "",
        )

        comparison = evaluator.compare(control, maos)

        self.assertEqual(comparison["winner"], "maos-ui-designer")
        self.assertGreaterEqual(comparison["score_delta"], 30)


if __name__ == "__main__":
    unittest.main()
