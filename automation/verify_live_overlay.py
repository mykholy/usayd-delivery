#!/usr/bin/env python3
"""Validate the live overlay; read-only, no network, no Jira writes."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTO = ROOT / "automation"
SOURCE = ROOT / "source_original/usayd-academy-codex-package"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


state = read_json(AUTO / "LIVE_DELIVERY_STATE.json")
mapping = read_json(AUTO / "jira-issue-map.json")["mappings"]
issues = state["issues"]
assert len({i["jira"] for i in issues}) == len(issues), "duplicate Jira keys"
assert len({i["stable_id"] for i in issues}) == len(issues), "duplicate stable IDs"
for issue in issues:
    item = mapping[issue["stable_id"]]
    assert item["jira_key"] == issue["jira"]
    assert item["status"] == issue["status"], issue["jira"]
for sprint, groups in state["sprint_counts"].items():
    rows = [i for i in issues if i["sprint"] == sprint]
    for key, subset in (
        ("all", rows),
        ("non_flutter", [i for i in rows if i["scope"] == "non-flutter"]),
        ("flutter_read_only", [i for i in rows if i["scope"] == "flutter-read-only"]),
    ):
        counts = Counter(i["status"] for i in subset)
        assert groups[key]["total"] == len(subset), (sprint, key)
        assert all(groups[key].get(status, 0) == count for status, count in counts.items())
        assert sum(v for k, v in groups[key].items() if k != "total") == len(subset)
assert read_json(AUTO / "jira-sync-queue.json") == [], "stale queue must not be replayed"
for pr in state["api_prs_18_to_30"]:
    assert bool(pr["merge_commit"]) == pr["merged"], pr["number"]
with (ROOT / "coverage/READY_SOURCE_SHA256.csv").open(encoding="utf-8-sig", newline="") as f:
    manifest = {r["Relative_Path"] for r in csv.DictReader(f)}
index = SOURCE / "03_screens/SCREEN_SPECS_INDEX.md"
ids = [line.split("`")[1] for line in index.read_text(encoding="utf-8").splitlines() if line.startswith("| `UX-")]
assert len(ids) == len(set(ids)) == 169
catalog = (ROOT / "management/SCREEN_DESIGN_CATALOG.md").read_text(encoding="utf-8")
for screen in ids:
    for path in (
        f"03_screens/screens/{screen}.md",
        f"01_design/canvas/{screen}.dc.html",
        f"01_design/html/ar/{screen}.html",
        f"01_design/html/en/{screen}.html",
    ):
        assert path in manifest and (SOURCE / path).is_file(), path
        assert f"../source_original/usayd-academy-codex-package/{path}" in catalog, path
print(f"PASS: {len(issues)} mapped live issues, {len(ids)} screens × 4 source links, consistent counts and empty replay queue.")
