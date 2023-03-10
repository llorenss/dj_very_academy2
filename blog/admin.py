from django.contrib import admin
# from django.contrib.admin import ModelAdmin

from blog.models import Category, Post

# @admin.register(models.Post)
# class AuthorAdmin(ModelAdmin):
#     list_diplay = (
#         "title",
#         "id",
#         "status",
#         "slug",
#         "author",
#     )
#     prepopulated_fields = {
#         "slug": ("title",),
#     }


# class PostAdmin(ModelAdmin):
#     list_diplay = (
#         "title",
#         "id",
#         "status",
#         "slug",
#         "author",
#     )
#     prepopulated_fields = {
#         "slug": ("title",),
#     }


# admin.site.register(Post, PostAdmin)
@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Category)
