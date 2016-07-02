from django.contrib import admin

# Register your models here.
from .models import Area


class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'level')
admin.site.register(Area, AreaAdmin)
