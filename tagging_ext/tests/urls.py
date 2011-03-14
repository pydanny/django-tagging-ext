from django.conf.urls.defaults import *


urlpatterns = patterns("",
    url(r"^tags/", include("tagging_ext.urls")),
)