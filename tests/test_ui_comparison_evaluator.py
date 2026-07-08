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

    def test_keyword_only_artifact_fails_layout_quality_gate(self):
        evaluator = load_evaluator()
        keyword_rich_markdown = """
        edge command command center operations mission edge node device alert command receipt
        alert triage evidence escalation approval audit policy safety command center overview
        command approval filters tabs search sorting queue table timeline drawer detail panel
        primary action secondary action bulk acknowledge ai-friendly semantic tokens domain
        wrapper typed api typescript data-testid stable selectors accessibility keyboard focus
        stylex ant design table form drawer modal tag badge timeline tabs missiontable
        commanddrawer alerttimeline evidenceviewer echarts chart loading skeleton empty error
        retry stale partial disconnected offline permission-limited role gate command pending
        receipt pending timeout failed destructive confirmation two-person approval compact
        dense neutral semantic warning danger success not landing no hero real product surface
        alignment stable dimensions responsive desktop mobile tablet screenshot viewport data-eval
        """
        keyword_rich_html = """
        <html>
          <head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
          <body>
            <main>
              <section>Mission queue</section>
              <section>Node health matrix</section>
              <section>Alert triage</section>
              <aside>Command approval</aside>
            </main>
          </body>
        </html>
        """

        result = evaluator.evaluate_artifact(keyword_rich_markdown, keyword_rich_html)

        self.assertLess(result["score"], 90)
        self.assertIn("Layout integrity and alignment", result["missing"])
        self.assertIn("Layout formation confirmation", result["missing"])
        self.assertIn("Module coherence and product model", result["missing"])
        self.assertIn("Responsive behavior and overflow control", result["missing"])

    def test_committed_maos_prototype_passes_structural_quality_gates(self):
        evaluator = load_evaluator()
        artifact_dir = ROOT / "docs" / "comparison" / "edge-command-ui" / "maos-ui-designer"

        result = evaluator.evaluate_directory(artifact_dir)

        self.assertEqual(result["grade"], "marketplace")
        self.assertEqual(result["missing"], [])
        self.assertGreaterEqual(result["details"]["Layout formation confirmation"], 8)
        self.assertGreaterEqual(result["details"]["Layout integrity and alignment"], 9)
        self.assertGreaterEqual(result["details"]["Module coherence and product model"], 8)
        self.assertGreaterEqual(result["details"]["Responsive behavior and overflow control"], 5)


if __name__ == "__main__":
    unittest.main()
