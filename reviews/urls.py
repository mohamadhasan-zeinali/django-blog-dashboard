from django.urls import path ,re_path, include
from .views import Article,Detail ,ArticlePreview,category
from .rest_views import *
from rest_framework.routers import DefaultRouter
app_name="blog"
urlpatterns = [
    path('', Article, name="blog"),
    path('blog/<slug:slug>',Detail, name="detail"),
    #demo page
    path('preview/<slug:slug>',ArticlePreview,name="preview"),
    path('category/<slug:slug>',category, name="category"),
    path('category/<slug:slug>/page/<int:page>',category, name="category"),
]
router = DefaultRouter()
router.register('category', CategoryViewset, basename='category')

urlpatterns +=[
    path('api/', include(router.urls))
]




