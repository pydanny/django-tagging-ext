"""
Tests client django-tagging-ext view

"""

from django.test import TestCase
from django.test.client import Client

class TestClient(TestCase):
    #fixtures = ['auth.json', 'blog.json']
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_tags(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)
