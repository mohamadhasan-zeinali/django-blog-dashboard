
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User
from .models import Article_model,Category
from django.views.generic import ListView , DetailView

#for paginations
from django.core.paginator import Paginator




# Create your views here.

def Article(request):
    #paginator mnadare badan narashh bezar 
    context={
        #اسلایدر که شامل همه بلاگ ها است 
        "articles": Article_model.objects.all(),
        #بلاگ ها به غیر از اونایی که تو اسلاید هستند
        "article" : Article_model.objects.filter(status = 'x'),
        #دسته بندی ها 

    }
    return render(request , 'blog/index.html',context)

def Detail(request , slug):
    context={
        "detail":Article_model.objects.get(slug=slug)

    }
    return render(request, 'blog/single-page.html',context)
    
  


 
    #######  ویو برای دسته بندی ها 

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

# برای پیش نمایش مقالات در داشبورد
#class ArticlePreview(DetailView):
#    def get_object(self):
#        pk = self.kwargs.get('pk')
#        return get_object_or_404(Article_model, pk=pk)

def ArticlePreview(request , slug):
    
    context={
        "preview" : Article_model.objects.filter(status='d')
   }
    return render(request, 'blog/single-page.html',context )



class AutherList(ListView):
    def get_queryset(self):
        auther = get_object_or_404(User)