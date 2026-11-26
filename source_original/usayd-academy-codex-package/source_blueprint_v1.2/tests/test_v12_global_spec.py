"""V1.2 documentation validation; not implementation tests."""
import unittest,csv,yaml,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def loadrows(p):
 with (ROOT/p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
class V12SpecTests(unittest.TestCase):
 def test_multinational_requirements_have_story_jira_tests(self):
  req=loadrows('02_REQUIREMENTS/functional_requirements.csv');jira=loadrows('06_DELIVERY_JIRA/Jira_Import.csv');tests=loadrows('07_QUALITY_SECURITY/test_cases.csv')
  rids={r['ID'] for r in req};sids={j['Requirement ID'] for j in jira if j['Issue Type']=='Story'};tids={t['Requirement ID'] for t in tests}
  self.assertTrue(rids<=sids);self.assertTrue(rids<=tids);self.assertGreaterEqual(len(req),200)
  for mod in ['GEO','TIME','I18N','VPC','SUP','ENG']:
   self.assertTrue(any(x['Module']==mod for x in req))
 def test_api_global_surface_typed(self):
  o=yaml.safe_load((ROOT/'04_ENGINEERING/openapi.yaml').read_text())
  for p in ['/api/v1/public/markets','/api/v1/me/preferences','/api/v1/me/checkout-quotes','/api/v1/admin/video-routing-policies/{policyId}/dry-run','/api/v1/admin/supervisor-assignments','/api/v1/admin/price-books']:
   self.assertIn(p,o['paths'])
  self.assertEqual([],o['paths']['/api/v1/public/markets']['get']['security'])
  schemas=o['components']['schemas']; self.assertIn('CheckoutQuote',schemas)
  self.assertIn('amount_minor',schemas['CurrencyMoney']['properties'])
  self.assertIn('timezone_id',schemas['Preference']['properties'])
  self.assertIn('scope_ids',schemas['SupervisorGrantCreate']['properties'])
 def test_ux_and_flows_present(self):
  screens=loadrows('05_UI_UX/screen_inventory.csv');self.assertGreaterEqual(len(screens),160)
  self.assertEqual(len({s['Screen ID'] for s in screens}),len(screens))
  flow=list((ROOT/'12_USER_JOURNEYS/diagrams').glob('*.mmd'));self.assertGreaterEqual(len(flow),24)
  self.assertTrue(all(f.read_text().startswith(('flowchart TD','sequenceDiagram')) for f in flow))
 def test_e2e_scenarios_cover_domains(self):
  sc=loadrows('14_RELEASE_QA/INTERNATIONAL_E2E_SCENARIOS.csv');self.assertGreaterEqual(len(sc),50)
  self.assertEqual(len({s['Scenario ID'] for s in sc}),len(sc))
  for domain in ['GEO','TIME','VPC','SUP','I18N','ENG']:
   self.assertIn(domain,{s['Domain'] for s in sc})
 def test_spec_does_not_claim_app_is_live(self):
  r=(ROOT/'00_START_HERE/FINAL_HANDOFF_v1.2.md').read_text()
  self.assertIn('not yet a deployed/production-certified product',r)
 def test_reference_sources_exist_in_doc(self):
  s=(ROOT/'11_PLATFORM_ADMIN/VIDEO_PROVIDER_CONSOLE.md').read_text()
  self.assertIn('Jan 15 2027',s)
if __name__=='__main__':unittest.main()
