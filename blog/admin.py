from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('item', 'slug', 'status', 'created_on')
    search_fields = ('item', 'description')
    prepopulated_fields = {'slug': ('item',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('description',)
