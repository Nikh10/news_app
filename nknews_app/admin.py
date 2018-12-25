from django.contrib import admin
from .models import Category, News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news','category',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)