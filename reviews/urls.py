from django.urls import path ,re_path
from .views import Article,Detail ,ArticlePreview,category

app_name="blog"
urlpatterns = [
    
    path('', Article, name="blog"),
    path('blog/<slug:slug>',Detail, name="detail"),
    #demo page
    path('preview/<slug:slug>',ArticlePreview,name="preview"),
    path('category/<slug:slug>',category, name="category"),
    path('category/<slug:slug>/page/<int:page>',category, name="category"),

  

   
]


