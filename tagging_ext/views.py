"""
django-tagging-ext views.py

"""

from sys import stderr

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db.models import get_model
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify

from django.contrib.contenttypes.models import ContentType

from tagging.models import Tag # use these to check for tag content

def get_model_counts(tagged_models, tag):
    """ This does a model count so the side bar looks nice.
    """
    model_counts = []
    for model in tagged_models:
        model['count'] = model['query'](tag).count()
        if model['count']:
            model_counts.append(model)
                 
    return model_counts
    
def check_results(results):
    if not results:
        raise Http404('No available items to display for this tag.')
    
    
def index(request, template_name="tagging_ext/index.html", min_size=0,limit=10):
    """
        min_size: Smallest size count accepted for a tag
        order_by: asc or desc by count
        limit: maximum number of tags to display 
        
        TODO: convert the hand-written query to an ORM call. Right now I know
                this works with Sqlite3 and PostGreSQL.
    """
    query = """
        SELECT tag_item.tag_id as tag_id, COUNT(tag_item.tag_id) as counter 
        FROM tagging_taggeditem as tag_item 
        GROUP BY tag_id
        HAVING COUNT(tag_item.tag_id) > %s
        ORDER BY counter desc
        LIMIT %s
    """

    cursor = connection.cursor()
    cursor.execute(query, [min_size, limit])
    
    results = []
    
    for row in cursor.fetchall():
        try:
            tag=Tag.objects.get(id=row[0])
        except ObjectDoesNotExist:
            continue
            
        if ' ' in tag.name:
            continue
        
        record = dict(
            tag=tag,
            count=row[1]
        )
        results.append(record)    
        
    dictionary = {
        'tags':results
    
    }
    

    return render_to_response(template_name, dictionary,
        context_instance=RequestContext(request))      
    

def tag(request, tag='', template_name="tagging_ext/tag.html", tagged_models=(), default_template=None):
    
    # does the tag actually exist?
    tag = get_object_or_404(Tag, name=tag)
            
    dictionary = { 
        'tag': tag,
        'model_counts': get_model_counts(tagged_models,tag)
    }
    
    return render_to_response(template_name, dictionary,
        context_instance=RequestContext(request))

def tag_by_model(request, tag, model,
                    template_name="tagging_ext/tag_by_model.html",
                    tagged_models=(),
                    default_content_template='tagging_ext/default_template.html'):

    # does the tag actually exist?
    tag = get_object_or_404(Tag, name=tag)
    
    model_counts = get_model_counts(tagged_models, tag)
    
    results = None
    for item in model_counts:
        
        # If the model being displayed is the same as what is being looped          
        if model == slugify(item.get('title', '')):
            
            # Fetch the lambda function which runs the ORM query
            query = item.get('query', None)
            
            if query:
                
                # get the results
                results = query(tag)
                
                # Toss 404 if the results are empty
                check_results(results)                
                
                # And if there is a custom_template, use that.
                # otherwise use the default template
                content_template = item.get('content_template', default_content_template)
                break
    
    # Toss 404 if the results are 0.
    check_results(results)                        
    
    dictionary = { 
        'tag': tag,
        'model': model,
        'model_counts': model_counts,
        'content_template': content_template,
        'results': results
    }
    
    return render_to_response(template_name, dictionary,
        context_instance=RequestContext(request))

def autocomplete(request, app_label=None, model=None):
    """returns ``\\n`` delimited strings in the form <tag>||(#)

    GET params are ``q``, ``limit``, ``counts``, ``q`` is what the user
    has typed, ``limit`` defaults to 10, and ``counts`` can be "model", "all"
    or, if absent, will default to all - ie a site-wide count.
    """

    # get the relevent model if applicable
    if app_label and model:
        try:
            model = ContentType.objects.get(app_label=app_label, model=model)
        except:
            raise Http404
    else:
        model = None
    
    if not request.GET.has_key("q"):
        raise Http404
    else:
        q = request.GET["q"]
    
    # counts can be 'all', 'model' or 'None'
    counts = request.GET.get("counts", "all")
    limit = request.GET.get("limit", 10)
    
    if model:
        tags = Tag.objects.filter(
            items__content_type = model,
            name__istartswith = q
        ).distinct()[:limit]
    else:
        tags = Tag.objects.filter(
            name__istartswith = q
        ).distinct()[:limit]

    if counts == "all":
        l = sorted(list(tags),
            lambda x, y: cmp(y.items.all().count(), x.items.all().count())
        )
        tag_list = "\n".join([ '%s||(%s)' % (tag.name, tag.items.all().count() ) for tag in l if tag])

    elif counts == "model":
        if model:
            l = sorted(list(tags),
                lambda x, y:
                    cmp(y.items.filter(content_type=model).count(), x.items.filter(content_type=model).count())
            )
            tag_list = "\n".join(
                ["%s||(%s)" % (tag.name, tag.items.filter(content_type=model).count()) for tag in l if tag]
            )
        else:
            raise Exception(
                'You asked for a model with GET but did not pass one to the url'
            )
    else:
        tag_list = "\n".join([tag.name for tag in tags if tag])
    return HttpResponse(tag_list)
