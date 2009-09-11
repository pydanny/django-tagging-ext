""" various tagging_ext template tags """

from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("tagging_ext/includes.html")
def wysiwyg_setup(protocol="http"):
    """
Create the <style> and <script> tags needed to initialize the rich text editor.
 
Create a local tagging_ext/includes.html template if you don't want to use Yahoo's CDN
"""
    return {"protocol": protocol}