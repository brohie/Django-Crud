from django.contrib import admin

from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created','author')

admin.site.register(Post, PostAdmin)