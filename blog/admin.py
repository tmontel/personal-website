from django.contrib import admin
from django.db import models
from .models import Blog
from tinymce.widgets import TinyMCE


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Blog, BlogAdmin)
