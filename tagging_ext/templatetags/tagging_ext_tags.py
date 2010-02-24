from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def tag_autocomplete_js(format_string=None):
    """format_string should be ``app_label model counts``
    
    renders 'tagging_ext/tag_autocomplete_js.html"""
    if format_string:
        context_list = format_string.split(' ')
        context = {
            'app_label':context_list[0],'model':context_list[1], 'counts':context_list[2]
        }
    else:
        context = {}
    return render_to_string('tagging_ext/tagging_autocomplete_js.html', context)



@register.inclusion_tag("tagging_ext/tag_list.html")
def show_tags_for(obj):
        
    response = {
        "obj": obj,
        "MEDIA_URL": settings.MEDIA_URL,
    }
    
    # Support for static media if supported
    if hasattr(settings, "STATIC_URL"):
        response['STATIC_URL'] = settings.STATIC_URL
    
    return response

@register.inclusion_tag("tagging_ext/tag_count_list.html")
def show_tag_counts(tag_counts):
    return {"tag_counts": tag_counts}