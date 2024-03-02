from django.contrib import admin
from .models import Post, Cotact, Comment, Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'is_solved', 'created_at')
    list_display_links = ('id', 'full_name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'image', 'views_count', 'is_published', 'created_at')
    list_display_links = ('id', 'title', 'author', 'image')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_published', 'created_at')
    list_display_links = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(Cotact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
