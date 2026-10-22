#!/usr/bin/env python3
"""draft-pr skill prose: preflight before body, one publish path.

Run: python3 -m unittest discover -s engine/skills/draft-pr/tests -v
"""
from __future__ import annotations

import os
import unittest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DraftPrOrder(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8") as handle:
            self.text = handle.read()

    def test_runs_make_pr_preflight_before_drafting_body(self):
        self.assertIn("Run its preflight classification before drafting any PR body", self.text)
        self.assertIn("commit-scoped", self.text)

    def test_choose_mergify_vs_gh_once_before_first_push(self):
        self.assertIn("Choose Mergify vs `gh` once", self.text)
        self.assertIn("before the first push", self.text)


class DraftPrAnimatedProof(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8") as handle:
            self.text = " ".join(handle.read().split())

    def test_animated_proof_is_for_a_state_transition_claim_not_a_draft(self):
        self.assertIn("Animated proof (gif, mp4, webm, or a walkthrough video) is for a PR whose claim is a state transition", self.text)
        self.assertIn("that is not a Draft, or for when the user asks for it", self.text)
        self.assertIn("Static screenshots cover everything else", self.text)
        self.assertNotIn("Static screenshots alone are not enough", self.text)

    def test_long_proof_step_is_announced_before_it_runs(self):
        self.assertIn("Any proof step that takes more than a minute", self.text)
        self.assertIn("is announced in one plan line before it runs", self.text)
        self.assertIn("Rule of Least Surprise", self.text)


if __name__ == "__main__":
    unittest.main()
