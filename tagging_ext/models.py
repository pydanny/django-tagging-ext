from django.db import models

from tagging.models import Tag
from tagging.models import TaggedItem as TagTaggedItem

class SynonymTag(Tag):
    """
    A tag which is treated as a synonym of another tag.

    To keep things simple, a tag can only have a synonym that itself
    has no synonym. 
    """
 
    synonym = models.ForeignKey(Tag,related_name="synonym")

    def __init__(self,*args,**kwargs):
        if "synonym" in kwargs:
            syn = kwargs.pop("synonym")
        else:
            syn = None
        super(SynonymTag, self).__init__(*args,**kwargs)
        if syn:
            if syn.__class__.__name__ == "Tag":
                self.synonym = syn
            else:
                self.synonym = syn.synonym

    def __unicode__(self):
        return "%s (treated as %s)" % (self.name, self.synonym.name)

class TaggedItem(TagTaggedItem):
    """
    Holds the relationship between a tag and the item being tagged.
    """
    synonym_tag = models.ForeignKey(SynonymTag, null=True, default=None)

    def __init__(self,*args,**kwargs):
        super(TaggedItem, self).__init__(*args,**kwargs)
        while syn.__class__.__name__ != "Tag":
            self.synonymm_tag = self.tag
            self.tag = self.synonym_tag.synonym

    def __unicode__(self):
        if self.synonym_tag != None:
            return u'%s (synonym: %s) [%s]' % (self.object, self.tag, self.synonym)
        else:
            return super(TaggedItem, self).__unicode__()

