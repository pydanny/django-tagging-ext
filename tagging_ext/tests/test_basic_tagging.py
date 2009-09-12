"""
Tests basic django-tagging-ext functions

"""

from django.test import TestCase
from django.test.client import Client

from tagging.models import Tag
from tagging_ext.models import SynonymTag, TaggedItem
from tagging_ext.helpers import *

class TestSynonyms(TestCase):
    
    def setUp(self):
        self.tag_wisdom = Tag(name="Wisdom")
        self.tag_wisdom.save()
        self.tag_quote = Tag(name="Quote")
        self.tag_quote.save()
        self.stag_quotation = SynonymTag(name="Quotation",synonym=self.tag_quote)
        self.stag_quotation.save()
        SynonymTag.objects.create(name="Knowledge",synonym=self.tag_wisdom)
        self.stag_quotes = SynonymTag(name="Quotes",synonym=self.stag_quotation)
        self.stag_quotes.save()
 
    def tearDown(self):
        pass

    def test_synonym_creation(self):
        self.assertEquals( 5, Tag.objects.count())

    def test_synonym_helper(self):
        # import pdb; pdb.set_trace()
        self.assertEquals( self.tag_quote, synonym( "Quote" ))
        self.assertEquals( self.tag_quote, synonym( "Quotation" ))
        self.assertEquals( self.tag_quote, synonym( "Quotes" ))
