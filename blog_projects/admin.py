from django.contrib import admin

# Register your models here.

from .models import BlogPost, Description

admin.site.register(BlogPost)
admin.site.register(Description)


