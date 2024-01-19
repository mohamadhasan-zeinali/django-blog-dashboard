from rest_framework import viewsets
from .serializers import *
from reviews.models import Article_model
from rest_framework.permissions import IsAuthenticated
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article_model.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]