#coding:utf-8
from django.core.cache import cache
from .models import Area

def city_cache(province):
    """市"""
    key = 'city_list_%s' % province
    cities = cache.get(key)
    if cities is None:
        cities = list(Area.objects.filter(parent_id=province))
        cache.set(key, cities, 36000)
    return cities