from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'publish_time')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
