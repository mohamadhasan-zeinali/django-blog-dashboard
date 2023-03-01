
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User
from .models import Article_model,Category
from django.views.generic import ListView , DetailView

#for paginations
from django.core.paginator import Paginator


def Article(request):
    #paginator mnadare badan narashh bezar 
    context={
        #slider for all blog 
        "articles": Article_model.objects.all(),
        # just slider
        "article" : Article_model.objects.filter(status = 'x'),

    }
    return render(request , 'blog/index.html',context)

def Detail(request , slug):
    context={
        "detail":Article_model.objects.get(slug=slug)

    }
    return render(request, 'blog/single-page.html',context)
    
  


 
# category view
def category(request , slug , page=1):
    category= get_object_or_404(Category,  slug=slug,  status=True)
    article_list= category.articles.all()
    
    paginator = Paginator(article_list, 6)
    articles=paginator.get_page(page)
    context={
        "category":category,
        "articles" :articles
     

    }
    return render(request, 'blog/category.html',context)



def ArticlePreview(request , slug):
    
    context={
        "preview" : Article_model.objects.filter(status='d')
   }
    return render(request, 'blog/single-page.html',context )



class AutherList(ListView):
    def get_queryset(self):
        auther = get_object_or_404(User)