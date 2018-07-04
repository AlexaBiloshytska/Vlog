import json

from django.test import TestCase

# Create your tests here.
from vlog.tests import Test_Vlog


class ApiArticles(Test_Vlog):
    def test_articles_list(self):
        client = self.client
        response = client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.dumps(response.data), 1)
