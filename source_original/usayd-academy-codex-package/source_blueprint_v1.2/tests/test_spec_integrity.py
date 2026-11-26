"""Runnable tests for documentation integrity; NOT product implementation tests."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_blueprint import audit
class BlueprintIntegrityTest(unittest.TestCase):
    def test_spec_passes_core_integrity_audit(self):
        issues, stats=audit()
        self.assertEqual([],issues,'\n'.join(issues))
        self.assertGreaterEqual(stats['requirements'],148)
        self.assertGreaterEqual(stats['openapi_operations'],54)
        self.assertGreaterEqual(stats['gherkin_scenarios'],40)
    def test_no_fabricated_implementation_claims(self):
        readme=(ROOT/'README_AR.md').read_text()
        self.assertIn('ليست تطبيقًا منشورًا',readme)
        self.assertIn('AGENTS.md',readme)
    def test_no_secrets_committed_to_spec(self):
        # Only inspect implementation-related config files, NOT ordinary prose examples.
        suspicious=[]
        for f in ROOT.glob('**/.env'):
            suspicious.append(str(f.relative_to(ROOT)))
        self.assertEqual([],suspicious)
if __name__=='__main__':unittest.main()
