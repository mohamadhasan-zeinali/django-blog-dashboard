from .models import *
from rest_framework import serializers
# category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'