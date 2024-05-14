from django.contrib import admin
from .models import Post, Contact, Comment, Category


class PostInline(admin.TabularInline):
    model = Post
    extra = 1
    fields = ('id', 'title')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'is_solved', 'created_at')
    list_display_links = ('id', 'full_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    list_display = ('id', 'title', 'author', 'image', 'views_count', 'is_published', 'created_at')
    list_display_links = ('id', 'title', 'author', 'image')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # inlines = (CommentInline,)
    list_display = ('id', 'name', 'email', 'is_published', 'created_at')
    list_display_links = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)

# admin.site.register(Post, PostAdmin)
# admin.site.register(Cotact, ContactAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Category)
