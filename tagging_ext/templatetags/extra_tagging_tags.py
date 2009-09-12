""" Here for compatability with Pinax's tag_app """

from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("pinax/tag_list.html")
def show_tags_for(obj):
    
    response = {
        "obj": obj,
        "MEDIA_URL": settings.MEDIA_URL,
    }
    
    # Support for static media if supported
    if hasattr(settings, "STATIC_URL"):
        response['STATIC_URL'] = settings.STATIC_URL
    
    return response

@register.inclusion_tag("pinax/tag_count_list.html")
def show_tag_counts(tag_counts):
    return {"tag_counts": tag_counts}