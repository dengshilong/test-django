#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Area(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name=u'上级区域', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'area'
        verbose_name = verbose_name_plural = (u'省/市/地区(县)')

    def __unicode__(self):
        return self.name
