from django.contrib import admin
from .models import Article_model , Category

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display=['title' ,'slug','description','status']

@admin.register(Article_model)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title' ,'thumbnail_tag','slug','description','thumbnail','auther','date','status','category_to_str']
    search_fields = ['title']





