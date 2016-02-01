from django.test import TestCase


class APIViewTestCase(TestCase):
    def test_landing_page_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'BLST')
