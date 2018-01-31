from django.contrib import admin
from .models import Snippet
# Register your models here.
admin.site.site_header = '林轩'
admin.site.site_title = '博客后台管理系统'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['created', 'title', 'code', 'linenos', 'language', 'style']


admin.site.register(Snippet, SnippetAdmin)

