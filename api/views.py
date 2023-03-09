from django.shortcuts import render
from reviews.models import Article_model
from rest_framework.generics import ListAPIView ,CreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import MainSerializer

# read
class ListArticle(ListAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer

#create 
class CreateArticle(CreateAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer

# update 
class UpdateArticle(RetrieveUpdateDestroyAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer