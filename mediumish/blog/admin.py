from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_created', 'time_to_read', 'get_image')
    list_filter = ('date_created', 'is_published',)
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_created'

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" with="50" height="50">')
        return ' - '


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')
    search_fields = ('title',)
