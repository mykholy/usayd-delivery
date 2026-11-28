import unittest
from unittest.mock import patch

import jira_sync


def row(key, repo="", parent="", kind="Task", summary="", labels=""):
    return {"External_ID": key, "Repository": repo, "Parent_External_ID": parent,
            "Issue Type": kind, "Summary": summary, "Labels": labels}


class ImportScopeTests(unittest.TestCase):
    def test_actual_package_scope(self):
        included, excluded = jira_sync.full_stack_items(
            jira_sync.rows("JIRA_IMPORT_EPICS.csv"), jira_sync.rows("JIRA_IMPORT_WORK_ITEMS.csv"))
        self.assertEqual(len(included), 682)
        self.assertEqual(len(excluded), 58)
        self.assertEqual(sum(r["Issue Type"] == "Epic" for r in excluded), 1)
        self.assertEqual(sum(r["Repository"] == "flutter" for r in excluded), 57)
        self.assertTrue(all(r["Repository"] != "flutter" for r in included))

    def test_exclusion_signals(self):
        e = row("USYD-E-FLUTTER", kind="Epic")
        tasks = [row("a", "flutter"), row("b", "api", parent=e["External_ID"]),
                 row("c", "api", labels="flutter"), row("d", "api", summary="[FLUTTER] test")]
        included, excluded = jira_sync.full_stack_items([e], tasks)
        self.assertEqual(included, [])
        self.assertEqual(len(excluded), 5)

    def test_unknown_scope_and_duplicate_fail(self):
        with self.assertRaisesRegex(ValueError, "Unknown repository"):
            jira_sync.full_stack_items([], [row("a", "unknown")])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            jira_sync.full_stack_items([], [row("a", "api"), row("a", "web")])

    def test_missing_parent_fails(self):
        with self.assertRaisesRegex(ValueError, "Parent outside"):
            jira_sync.full_stack_items([], [row("a", "api", "absent")])

    def test_valid_parent_first_chain_preserved(self):
        epic = row("E", kind="Epic")
        parent = row("P", "api", "E")
        child = row("C", "api", "P")
        included, excluded = jira_sync.full_stack_items([epic], [parent, child])
        self.assertEqual([r["External_ID"] for r in included], ["E", "P", "C"])
        self.assertEqual(excluded, [])

    def test_child_before_parent_rejected(self):
        epic = row("E", kind="Epic")
        with self.assertRaisesRegex(ValueError, "Parent must precede child"):
            jira_sync.full_stack_items([epic], [row("C", "api", "P"), row("P", "api", "E")])

    def test_self_reference_and_cycle_rejected(self):
        for tasks in ([row("P", "api", "P")],
                      [row("A", "api", "B"), row("B", "api", "A")]):
            with self.subTest(tasks=tasks), self.assertRaisesRegex(ValueError, "cycle"):
                jira_sync.full_stack_items([], tasks)

    def test_invalid_order_rejected_before_network_in_all_modes(self):
        for mode in ("--plan-only", "--dry-run", "--apply"):
            with self.subTest(mode=mode), patch("sys.argv", ["jira_sync.py", mode]), \
                    patch.object(jira_sync, "rows", side_effect=[
                        [row("E", kind="Epic")],
                        [row("C", "api", "P"), row("P", "api", "E")]]), \
                    patch.object(jira_sync, "api") as api:
                with self.assertRaisesRegex(ValueError, "Parent must precede child"):
                    jira_sync.main()
                api.assert_not_called()

    def test_offline_plan_never_calls_jira(self):
        with patch("sys.argv", ["jira_sync.py", "--plan-only"]), patch.object(jira_sync, "api") as api:
            jira_sync.main()
            api.assert_not_called()

    def test_no_implicit_apply(self):
        with patch("sys.argv", ["jira_sync.py"]), patch.object(jira_sync, "api") as api:
            with self.assertRaises(SystemExit):
                jira_sync.main()
            api.assert_not_called()


if __name__ == "__main__":
    unittest.main()
