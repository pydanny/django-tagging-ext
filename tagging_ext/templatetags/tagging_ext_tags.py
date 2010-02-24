from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def tag_autocomplete_js(format_string=None):
    """format_string should be ``app_label model counts``
    
    renders 'tagging_utils/tag_autocomplete_js.html"""
    if format_string:
        context_list = format_string.split(' ')
        context = {
            'app_label':context_list[0],'model':context_list[1], 'counts':context_list[2]
        }
    else:
        context = {}
    return render_to_string('tagging_utils/tagging_autocomplete_js.html', context)

