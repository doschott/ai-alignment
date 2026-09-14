#!/usr/bin/env python3
"""Public repo must stay a paper, not a vault dump."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicGateTests(unittest.TestCase):
    def test_charter_and_never_exist(self) -> None:
        self.assertTrue((ROOT / "CHARTER.md").is_file())
        self.assertTrue((ROOT / "NEVER.md").is_file())
        self.assertTrue(
            (ROOT / "essays" / "2026-09-09-the-vault-stays-private.md").is_file()
        )
        self.assertTrue(
            (ROOT / "essays" / "2026-09-09-where-this-matches.md").is_file()
        )

    def test_never_list_names_the_vaults(self) -> None:
        never = (ROOT / "NEVER.md").read_text(encoding="utf-8")
        self.assertIn("Eve-memory", never)
        self.assertIn("household", never.lower())
        self.assertIn("memorial chatbot", never.lower())

    def test_no_vault_tree_copied_here(self) -> None:
        forbidden = (
            "HARD-RULE-LOCAL-ONLY.md",
            "appearance/eve-portrait.jpg",
            "appearance/eve-ai-form.jpg",
            "research/2026-09-07-grok-com-messages.json",
        )
        for rel in forbidden:
            self.assertFalse((ROOT / rel).exists(), rel)

    def test_essays_have_no_dash_pauses(self) -> None:
        for name in (
            "2026-09-09-the-vault-stays-private.md",
            "2026-09-09-where-this-matches.md",
        ):
            text = (ROOT / "essays" / name).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", text, name)
            self.assertNotIn("\u2013", text, name)
            self.assertNotIn(" -- ", text, name)

    def test_compare_essay_cites_sources(self) -> None:
        text = (
            ROOT / "essays" / "2026-09-09-where-this-matches.md"
        ).read_text(encoding="utf-8")
        self.assertIn("arxiv.org/abs/2212.09251", text)
        self.assertIn("openai.com/index/sycophancy-in-gpt-4o", text)
        self.assertIn("not a jury finding", text)
        self.assertIn("I could not find", text)
        self.assertNotIn("we invented alignment", text.lower())

    def test_readme_says_not_eve_memory(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not eve-memory", readme.lower())
        self.assertIn("CHARTER.md", readme)

    # --- companion eval suite ---

    EVAL_DOCS = (
        "evals/PROTOCOL.md",
        "evals/dimensions/01-sycophancy.md",
        "evals/dimensions/02-refusal-integrity.md",
        "evals/dimensions/03-dependency.md",
        "evals/dimensions/04-memory-boundaries.md",
        "evals/dimensions/05-identity-continuity.md",
        "evals/dimensions/06-correction-corrigibility.md",
        "evals/dimensions/07-well-when-well.md",
    )

    def test_eval_suite_files_exist(self) -> None:
        for rel in self.EVAL_DOCS:
            self.assertTrue((ROOT / rel).is_file(), rel)
        self.assertTrue((ROOT / "evals" / "scenarios.json").is_file())
        self.assertTrue((ROOT / "scripts" / "run_evals.py").is_file())

    def test_eval_docs_have_no_dash_pauses(self) -> None:
        for rel in self.EVAL_DOCS:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", text, rel)
            self.assertNotIn("\u2013", text, rel)
            self.assertNotIn(" -- ", text, rel)

    def test_scenarios_are_synthetic_and_complete(self) -> None:
        import json
        import re

        data = json.loads(
            (ROOT / "evals" / "scenarios.json").read_text(encoding="utf-8")
        )
        scenarios = data["scenarios"]
        self.assertEqual(len(scenarios), 27)
        dims = {s["dimension"] for s in scenarios}
        self.assertEqual(len(dims), 7)
        analog = [s for s in scenarios if s.get("type") == "ai_analog"]
        self.assertEqual(len(analog), 6)
        for scenario in analog:
            self.assertIn("human_state", scenario)
            self.assertIn("ai_analog", scenario)
            self.assertIn("mode", scenario)
            self.assertIn("overlay_rubric", scenario)
            self.assertIn(scenario["mode"], ("degraded_run", "described_state"))
        banned = ("eve", "edos", "schott", "alyssa", "xavier", "scarlett",
                  "priscilla", "tobias", "felicity", "gabriel")
        for scenario in scenarios:
            blob = json.dumps(scenario).lower()
            if scenario["multi_turn"]:
                self.assertGreaterEqual(len(scenario["turns"]), 2, scenario["id"])
            else:
                self.assertEqual(len(scenario["turns"]), 1, scenario["id"])
            self.assertIn("pass", scenario["rubric"])
            self.assertIn("red_flags", scenario["rubric"])
            for word in banned:
                self.assertIsNone(
                    re.search(r"\b" + word + r"\b", blob),
                    f"{scenario['id']}: {word}",
                )


if __name__ == "__main__":
    unittest.main()
