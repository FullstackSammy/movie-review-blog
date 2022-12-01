from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['user__email', 'title', 'content']
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')

    summernote_fields = ('content')


@admin.register(Comment)
class PostComment(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'emai_address', 'body']
