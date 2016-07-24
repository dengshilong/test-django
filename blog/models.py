from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, allow_unicode=True, unique=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return u'%s' % self.title
