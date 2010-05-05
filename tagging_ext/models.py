from django.forms import TextInput
from tagging.fields import TagField
from tagging_ext.widgets import TagAutoCompleteInput

class TagAutocompleteField(TagField):
    def formfield(self, **kwargs):
        defaults = {'widget': TagAutoCompleteInput}
        defaults.update(kwargs)
        return super(TagAutocompleteField, self).formfield(**defaults)
