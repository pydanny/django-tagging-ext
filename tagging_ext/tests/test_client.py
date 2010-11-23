#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Tests client django-tagging-ext view

"""

from django.test import TestCase
from django.test.client import Client

class TestClient(TestCase):
    fixtures = ['auth.json', 'blog.json']
    
    def setUp(self):
        self.logged_in = self.client.login(username="test", password="test")
    
    def tearDown(self):
        pass

    def test_login(self):
        self.assert_(self.logged_in)
    
    def test_ascii_tags(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'django')
        self.assertContains(response, 'fun')

    def test_unicode_tag(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '日本語')
        self.assertContains(response, 'français')
