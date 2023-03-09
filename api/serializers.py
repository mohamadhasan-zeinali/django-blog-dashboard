from rest_framework import serializers
from reviews.models import Article_model

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_model
        fields = '__all__'