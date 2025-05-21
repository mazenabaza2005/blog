from django.contrib import admin
from django.utils.html import format_html

from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at', 'updated_at', 'published_at', 'category', 'get_tags')
    list_filter = ('published_at', 'created_at', 'author')
    search_fields = ('title', 'slug', 'content', 'author__username')
    ordering = ('-created_at',)
    readonly_fields = ('cover_image_preview',)

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="200" height="auto">', obj.cover_image.url)
        return '-'

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])


    cover_image_preview.short_description = "Preview image"
    get_tags.short_description = "Tags"

