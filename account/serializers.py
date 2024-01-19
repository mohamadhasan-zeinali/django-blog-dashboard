from rest_framework import  serializers
from reviews.models import *

class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='account:article-detail')
    class Meta:
        model = Article_model
        fields = ['url', 'id', 'auther', 'title', 'slug', 'category', 'description', 'thumbnail', 'status']


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='account:category-detail')
    class Meta:
        model = Category
        fields = ['url', 'id', 'title', 'description', 'slug', 'status']