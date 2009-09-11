"""
Tests basic django-tagging-ext functions

"""

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.utils import simplejson

class TestSearchForms(TestCase):
    fixtures = ['auth.json','blog.json']
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def blah(self):
        pass
    