import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "plugins" / "maos-ui-designer" / "skills" / "maos-ui-designer"


class MaosSkillContractTest(unittest.TestCase):
    def test_skill_requires_layout_formation_before_visual_design(self):
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8").lower()

        self.assertIn("layout formation", skill)
        self.assertIn("before visual", skill)
        self.assertIn("read `references/layout-formation.md`", skill)

    def test_layout_formation_reference_defines_page_formations(self):
        reference = SKILL_DIR / "references" / "layout-formation.md"

        self.assertTrue(reference.exists(), "layout-formation.md reference should exist")
        content = reference.read_text(encoding="utf-8").lower()

        for formation in [
            "list + detail",
            "workbench",
            "dashboard + drilldown",
            "wizard / stepper",
            "canvas + inspector",
            "terminal/tui pane",
        ]:
            self.assertIn(formation, content)

        for required_slot in [
            "primary object",
            "primary region",
            "secondary region",
            "responsive collapse",
            "rejected formations",
        ]:
            self.assertIn(required_slot, content)


if __name__ == "__main__":
    unittest.main()
