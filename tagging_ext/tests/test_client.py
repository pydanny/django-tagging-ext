#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Tests client django-tagging-ext view

"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from tagging_ext.tests.models import BlogPost

class TestClient(TestCase):
    fixtures = ['auth.json']
    urls = 'tagging_ext.tests.urls'

    def setUp(self):
        self.logged_in = self.client.login(username="test", password="test")

        bp = BlogPost.objects.create(
            body="I am a body", tags="fun django")
        bp_chars = BlogPost.objects.create(
            body="I am a post tagged with Japanese and French characters",
            tags="fun django 日本語 français",
        )

    def test_login(self):
        self.assert_(self.logged_in)

    def test_ascii_tags(self):
        autocomplete = reverse('tagging_ext_autocomplete')

        response = self.client.get(autocomplete, {'q': 'dj'})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'django')

        response = self.client.get(autocomplete, {'q': 'f'})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'fun')

    def test_unicode_tag(self):
        autocomplete = reverse('tagging_ext_autocomplete')

        response = self.client.get(autocomplete, {'q': '日'})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '日本語')

        response = self.client.get(autocomplete, {'q': 'f'})
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'français')
