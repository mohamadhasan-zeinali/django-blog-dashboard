from .models import *

from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

#category
class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status = True)
    permission_classes = [IsAuthenticated]


#blog
class BlogViewset(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Article_model.objects.all()

