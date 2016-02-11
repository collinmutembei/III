from django.test import TestCase


class APIViewTestCase(TestCase):
    def test_landing_page_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'BLST')

    def test_dashboard_view(self):
        resp = self.client.get('/dashboard/')
        self.assertEqual(resp.status_code, 200)

    def test_inexistent_view(self):
        resp = self.client.get('/kjgduyv/')
        self.assertEqual(resp.status_code, 404)
