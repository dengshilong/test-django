#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Area(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name=u'上级区域', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'area'
        verbose_name = verbose_name_plural = (u'省/市/区(县)')

    def __unicode__(self):
        return self.name


@receiver(post_delete, sender=Area)
@receiver(post_save, sender=Area)
def delete_cache(sender, **kwargs):
    #清除cache
    obj = kwargs['instance']
    if obj.parent is None:
        key = "city_list_0"
    else:
        key = "city_list_%s" % obj.parent_id
    cache.delete(key)
