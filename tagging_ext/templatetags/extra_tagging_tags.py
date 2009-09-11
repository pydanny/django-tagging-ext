""" Here for backwards compatability with Pinax's old tag_app """

from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("pinax_legacy/tag_list.html")
def show_tags_for(obj):
    return {
        "obj": obj,
        "MEDIA_URL": settings.MEDIA_URL,
        "STATIC_URL": settings.STATIC_URL,
    }

@register.inclusion_tag("pinax_legacy/tag_count_list.html")
def show_tag_counts(tag_counts):
    return {"tag_counts": tag_counts}