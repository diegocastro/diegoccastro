from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'language', 'published_date')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)