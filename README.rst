=======================================
django-tagging-ext (Django Tagging EXT)
=======================================

`django-tagging`_ gives you tagging. Django Tagging EXT gives you enhanced
displays of tags. It is `Django`_ neutral but when combined with `Pinax`_ 
gives you some extra view capabilities based off some of the Pinax core 
applications.

Future releases of Django Tagging EXT will include these features:

 * Tag synonyms (blog can be related to blogs)
 * More comprehensive tests
 * Tag dispatching so you can control tagging more tightly. For example, limiting tags to just one model.
 * Sphinx based docs folder

Dependencies
~~~~~~~~~~~~

django-tagging

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

Pinax 0.7

Installation
~~~~~~~~~~~~

Tagged release::

    pip install django-tagging-est
    
Development version::

    pip install -e git://github.com/pydanny/django-tagging-ext.git#egg=django-tagging-ext
    
Add to your Django settings.py file::

    INSTALLED_APPS = (
        ...
        'tagging_ext',
    )
    

View rendering via root url_conf
=================================

In the project url_conf (urls.py)::

    # django-tagging-ext url definitions
    from blog.models import Post
    from bookmarks.models import BookmarkInstance
    from photos.models import Image
    from tagging.models import TaggedItem

    tagged_models = (
      dict(title="Blog Posts",
        query=lambda tag : TaggedItem.objects.get_by_model(Post, tag).filter(status=2),
      ),
      dict(title="Bookmarks",
        query=lambda tag : TaggedItem.objects.get_by_model(BookmarkInstance, tag),
      ),
      dict(title="Photos",
        query=lambda tag: TaggedItem.objects.get_by_model(Image, tag).filter(safetylevel=1),
      ),
    )

    tagging_ext_kwargs = {
      'tagged_models':tagged_models,
      # You can add your own special template to be the default
      #'default_template':'custom_templates/special.html'
    }

    urlpatterns += patterns('',
      url(r'^tags/(?P<tag>.+)/(?P<model>.+)$', 'tagging_ext.views.tag_by_model', 
            kwargs=tagging_ext_kwargs, name='tagging_ext_tag_by_model'),
      url(r'^tags/(?P<tag>.+)/$', 'tagging_ext.views.tag', 
            kwargs=tagging_ext_kwargs, name='tagging_ext_tag'),
      url(r'^tags/$', 'tagging_ext.views.index', name='tagging_ext_index'),  
    )
    
View rendering in Pinax via root url_conf
==========================================

In the pinax project url_conf (urls.py) we use the custom_template field to 
explicitly tell Django Tagging EXT to fetch views customized for use in 
Pinax::

    # django-tagging-ext url definitions
    from blog.models import Post
    from bookmarks.models import BookmarkInstance
    from photos.models import Image
    from tagging.models import TaggedItem

    tagged_models = (
      dict(title="Blog Posts",
        query=lambda tag : TaggedItem.objects.get_by_model(Post, tag).filter(status=2),
        content_template="pinax_tagging_ext/blogs.html",
      ),
      dict(title="Bookmarks",
        query=lambda tag : TaggedItem.objects.get_by_model(BookmarkInstance, tag),
        content_template="pinax_tagging_ext/bookmarks.html",        
      ),
      dict(title="Photos",
        query=lambda tag: TaggedItem.objects.get_by_model(Image, tag).filter(safetylevel=1),
        content_template="pinax_tagging_ext/photos.html",    
      ),
    )

    tagging_ext_kwargs = {
      'tagged_models':tagged_models,
      # You can add your own special template to be the default
      #'default_template':'custom_templates/special.html'
    }

    urlpatterns += patterns('',
      url(r'^tags/(?P<tag>.+)/(?P<model>.+)$', 'tagging_ext.views.tag_by_model',
            kwargs=tagging_ext_kwargs, name='tagging_ext_tag_by_model'),
      url(r'^tags/(?P<tag>.+)/$', 'tagging_ext.views.tag', 
            kwargs=tagging_ext_kwargs, name='tagging_ext_tag'),
      url(r'^tags/$', 'tagging_ext.views.index', name='tagging_ext_index'),  
    )


.. _`django-tagging`: http://code.google.com/p/django-tagging
.. _`Django`: http://djangoproject.com
.. _`Pinax`: http://pinaxproject.com


