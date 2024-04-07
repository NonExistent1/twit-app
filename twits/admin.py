"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django.contrib import admin

from .models import Twit, Comment

class CommentInline(admin.TabularInline):
    """Inline for seeing comments related to the article"""
    model = Comment

class TwitAdmin(admin.ModelAdmin):
    """Custom Article Admin"""
    inlines = [
        CommentInline,
    ]

admin.site.register(Twit, TwitAdmin)
admin.site.register(Comment)
