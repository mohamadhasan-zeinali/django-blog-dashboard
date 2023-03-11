from django.shortcuts import render
from reviews.models import Article_model
from rest_framework.generics import ListAPIView ,CreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import MainSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect 
from rest_framework.reverse import reverse
# read
class ListArticle(ListAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer

#create 
class CreateArticle(CreateAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return HttpResponseRedirect(redirect_to='/api/')


# update 
class UpdateArticle(RetrieveUpdateDestroyAPIView):
    queryset = Article_model.objects.all()
    serializer_class = MainSerializer
    permission_classes = [IsAuthenticated]