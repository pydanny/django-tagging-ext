from django import template
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class TagAutoCompleteInput(forms.TextInput):
    
    class Media:
        if hasattr(settings, 'STATIC_URL'):
            media_url = settings.STATIC_URL
        else:
            media_url = settings.MEDIA_URL

        css = {
            "all": (media_url + "pinax/css/jquery.autocomplete.css",)
        }
        js = (
            media_url + "pinax/js/jquery-1.3.2.min.js",
            media_url + "pinax/js/jquery.bgiframe.min.js",
            media_url + "pinax/js/jquery.ajaxQueue.js",
            media_url + "pinax/js/jquery.autocomplete.min.js"
        )
    
    def init(self, *args, **kwargs):
        if len(args) == 4:
            self.app_label = args[0]
            self.model = args[1]
            args = args[2:]
            super(TagAutoCompleteInput, self).__init__(*args, **kwargs)
        else:
            super(TagAutoCompleteInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        output = super(TagAutoCompleteInput, self).render(name, value, attrs)
        
        return output + mark_safe(u"""
            <script type="text/javascript">
                jQuery("#id_%s").autocomplete("%s", {
                    max: 10,
                    highlight: false,
                    multiple: true,
                    multipleSeparator: " ",
                    scroll: true,
                    scrollHeight: 300,
                    matchContains: true,
                    autoFill: true,
                    formatItem: function(data, i, n, value){
                        return data[0]+" "+data[2];
                    },
                    formatResult: function(data, value){
                        return value;
                    }
                });
            </script>""" % (
                name,
                reverse("tagging_ext_autocomplete", kwargs={
                    "app_label": self.app_label,
                    "model": self.model }
                        if 'app_label' in self.__dict__ else {}
                )
            )
        )
