from django.contrib import admin

from tagging_ext.models import SynonymTag, TaggedItem

admin.site.register(SynonymTag)
admin.site.register(TaggedItem)

