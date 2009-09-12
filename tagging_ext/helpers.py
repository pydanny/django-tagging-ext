from tagging.models import Tag
from tagging_ext.models import SynonymTag

def synonym( name ):
    """
    Return the ultimate tag associated with a given name.
       (i.e., track down synonyms)
    """
    try:
        tag = Tag.objects.get(name=name)
    except:
        return None
    try:
        stag = tag.synonymtag
    except:
        return tag
    return stag.synonym

def synonym_tags( name ):
    """
    Return tag objects that are synonyms with the given name.
    """
    stag = synonym( name )
    return SynonymTag.objects.filter(synonym=stag)

def synonyms( name ):
    """
    Return an array of synonym tag names
    """
    stags = synonym_tags( name )
    results = []
    for tag in stags:
        results.append( tag.name )
    return results

