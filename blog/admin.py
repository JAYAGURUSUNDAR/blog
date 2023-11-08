from django.contrib import admin

from .models import BlogPost, CreateBlogForm, User

admin.site.register(BlogPost)
admin.site.register(User)