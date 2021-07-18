from django.urls import path ,re_path
from .views import Article,Detail ,ArticlePreview,category

app_name="blog"
urlpatterns = [
    
    path('', Article, name="blog"),
    path('blog/<slug:slug>',Detail, name="detail"),
    path('preview/<slug:slug>',ArticlePreview,name="preview"),#برای صفحه پیش نمایش
    path('category/<slug:slug>',category, name="category"),
    path('category/<slug:slug>/page/<int:page>',category, name="category"),

    #### url persian
    #re_path(r'(?v<slug>[-\w]+)')

   
]


