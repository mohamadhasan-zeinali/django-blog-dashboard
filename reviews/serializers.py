from .models import *
from rest_framework import serializers
# category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'

# blog
class BlogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name ='blog:blog-detail')
    class Meta:
        model = Article_model
        fields = '__all__'