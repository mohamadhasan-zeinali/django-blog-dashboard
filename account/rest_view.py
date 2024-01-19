from rest_framework import viewsets
from . serializers import *
from reviews.models import *
from rest_framework.permissions import IsAuthenticated
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article_model.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]