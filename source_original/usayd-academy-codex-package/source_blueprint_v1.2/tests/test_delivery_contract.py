"""Jira + user-flow integrity tests for document package."""
import unittest,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read_csv(relative):
    with (ROOT/relative).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
class DeliveryContractTest(unittest.TestCase):
    def test_jira_issue_ids_and_epic_parent(self):
        rows=read_csv('06_DELIVERY_JIRA/Jira_Import.csv');d={j['Issue ID']:j for j in rows}
        self.assertEqual(len(rows),len(d))
        for row in rows:
            if row['Parent ID']:
                self.assertIn(row['Parent ID'],d)
                self.assertEqual('Epic',d[row['Parent ID']]['Issue Type'])
    def test_all_functional_requirements_have_story(self):
        requirements={j['ID'] for j in read_csv('02_REQUIREMENTS/functional_requirements.csv')}
        stories={j['Requirement ID'] for j in read_csv('06_DELIVERY_JIRA/Jira_Import.csv') if j['Issue Type']=='Story'}
        self.assertEqual(requirements,stories)
    def test_critical_e2e_scenarios_present(self):
        text='\n'.join(f.read_text() for f in (ROOT/'07_QUALITY_SECURITY/gherkin').glob('*.feature'))
        for phrase in ['Concurrent last credit booking','Payment webhook replay','AI plan cannot auto publish','Minors private results','Contract effective date']:
            self.assertIn('Scenario: '+phrase,text)
if __name__=='__main__':unittest.main()
