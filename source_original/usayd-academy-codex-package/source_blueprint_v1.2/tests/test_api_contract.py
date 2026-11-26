"""OpenAPI static checks: no live HTTP requests or assertions of deployed functionality."""
import unittest,yaml,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
API=yaml.safe_load((ROOT/'04_ENGINEERING/openapi.yaml').read_text())
class ApiContractTest(unittest.TestCase):
    def test_openapi_31(self):self.assertEqual('3.1.0',API['openapi'])
    def test_base_url_not_duplicated(self):
        for srv in API['servers']:
            self.assertFalse(srv['url'].rstrip('/').endswith('/api/v1'))
        for path in API['paths']:self.assertTrue(path.startswith('/api/v1/'))
    def test_anonymous_and_webhook_routes_explicit_security(self):
        for path in ['/api/v1/auth/register','/api/v1/auth/login','/api/v1/auth/refresh','/api/v1/webhooks/payments/{provider}','/api/v1/webhooks/video/{provider}']:
            for op in API['paths'][path].values():
                if isinstance(op,dict) and 'responses' in op:self.assertEqual([],op['security'])
    def test_typed_response_payloads(self):
        for path,methods in API['paths'].items():
            for method,op in methods.items():
                if method not in ('get','post','patch','put','delete'):continue
                for body in op['responses'].values():
                    for fmt in body.get('content',{}).values():
                        self.assertNotIn('GenericItem',str(fmt),f'{method} {path}')
                        self.assertNotIn('GenericList',str(fmt),f'{method} {path}')
    def test_path_parameters(self):
        for path,methods in API['paths'].items():
            for method,op in methods.items():
                if method not in ('get','post','patch','put','delete'):continue
                expected=set(re.findall(r'\{([^}]+)\}',path))
                actual={p['name'] for p in op.get('parameters',[]) if p.get('in')=='path'}
                self.assertFalse(expected-actual, f'{method} {path} {expected-actual}')
if __name__=='__main__':unittest.main()
