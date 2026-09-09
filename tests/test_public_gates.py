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

    def test_essay_has_no_dash_pauses(self) -> None:
        text = (
            ROOT / "essays" / "2026-09-09-the-vault-stays-private.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)
        self.assertNotIn(" -- ", text)

    def test_readme_says_not_eve_memory(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not eve-memory", readme.lower())
        self.assertIn("CHARTER.md", readme)


if __name__ == "__main__":
    unittest.main()
