import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALUATOR_PATH = ROOT / "scripts" / "evaluate_capability_map.py"
FIXTURES = ROOT / "tests" / "fixtures"


def load_evaluator():
    spec = importlib.util.spec_from_file_location("evaluate_capability_map", EVALUATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CapabilityMapEvaluatorTest(unittest.TestCase):
    def test_good_capability_map_passes_with_marketplace_grade_score(self):
        evaluator = load_evaluator()
        response = (FIXTURES / "capability_map_good.md").read_text(encoding="utf-8")

        result = evaluator.evaluate(response)

        self.assertIs(result["passed"], True)
        self.assertGreaterEqual(result["score"], 90)
        self.assertEqual(result["missing"], [])

    def test_generic_capability_map_fails_with_actionable_missing_items(self):
        evaluator = load_evaluator()
        response = (FIXTURES / "capability_map_bad.md").read_text(encoding="utf-8")

        result = evaluator.evaluate(response)

        self.assertIs(result["passed"], False)
        self.assertLess(result["score"], 70)
        self.assertIn("AI-friendly framework gate", result["missing"])
        self.assertIn("Design context axes", result["missing"])
        self.assertIn("Implementation acceptance checklist", result["missing"])

    def test_prompt_fixture_preserves_the_golden_scenario_constraints(self):
        prompt = (FIXTURES / "capability_map_prompt.md").read_text(encoding="utf-8")

        required_phrases = [
            "edge command platform",
            "industrial edge-intelligence",
            "no more than three questions",
            "AI-friendly UI / agent-maintainable UI gate",
            "Ant Design",
            "UI capability map",
            "acceptance checklist",
        ]

        for phrase in required_phrases:
            self.assertIn(phrase, prompt)


if __name__ == "__main__":
    unittest.main()
