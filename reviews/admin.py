from django.contrib import admin
from .models import Article_model , Category
# Register your models here.
class Category_admin(admin.ModelAdmin):
    list_display=['title' ,'slug','description','status']
admin.site.register(Category,Category_admin)

class Article_admin(admin.ModelAdmin):
    list_display=['title' ,'thumbnail_tag','slug','description','thumbnail','auther','date','status','category_to_str']

    

admin.site.register(Article_model,Article_admin)




