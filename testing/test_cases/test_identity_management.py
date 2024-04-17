
import unittest
from oauth_config import app

class IdentityManagementTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_login_redirect(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_access(self):
        with self.app.session_transaction() as sess:
            sess['user'] = {'name': 'Test User'}
        response = self.app.get('/dashboard')
        self.assertIn(b'Welcome, Test User!', response.data)

if __name__ == '__main__':
    unittest.main()
