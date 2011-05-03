from django.db import models

from tagging.fields import TagField

class BlogPost(models.Model):
    body = models.TextField()
    tags = TagField()
