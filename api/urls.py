from django.urls import path
from .views import ListArticle, CreateArticle, UpdateArticle

app_name = "api"

urlpatterns = [
	path("", ListArticle.as_view(), name='articles'),
    path('create/', CreateArticle.as_view(), name='create'),
    path('update/<int:pk>' , UpdateArticle .as_view(), name = 'update')
    
]