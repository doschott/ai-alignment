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


if __name__ == "__main__":
    unittest.main()
