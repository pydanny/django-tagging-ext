from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^autocomplete/(?P<app_label>\w+)/(?P<model>\w+)/$", "tagging_ext.views.autocomplete",
            name="tagging_ext_autocomplete"),
    url(r"^autocomplete/$", "tagging_ext.views.autocomplete", name="tagging_ext_autocomplete"),
)
