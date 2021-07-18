from typing import List
from django.db import models
from django.shortcuts import render
#تابع جنگو برای صفحاتی که فقط زمانی مشاهده شوند که لاگین کرده باشند برای فانکشن ویو
from django.contrib.auth.decorators import login_required
#برای  نمایش بر اساس کلاس بیس
from django.contrib.auth.mixins import LoginRequiredMixin
#CLASS BASE VIEW
from django.views.generic import ListView , CreateView,UpdateView , DeleteView
#  برای ویو ادیت 
from django.urls import reverse_lazy

#import model article
from reviews.models import Article_model
# Create your views here.
#@login_required
#def home(request):
#    context={
#        "query": Article_model.objects.all()
#    }
#    return render(request, 'registration/home.html')

#################class base view    ##################
class ArticleList(LoginRequiredMixin, ListView):
    queryset=Article_model.objects.all()
    template_name="registration/home.html"
# وی ساخت بلاگ
class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article_model
    fields = ['auther',"title","slug","category","description","thumbnail","date","status"]

    template_name= "registration/article-create-update.html"
#ویو ویرایش بلاگ
class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article_model
    fields = ['auther',"title","slug","category","description","thumbnail","date","status"]

    template_name= "registration/article-create-update.html"

# ویو برای دیلت مقاله 
class ArticleDelete(DeleteView):
    model = Article_model
    success_url = reverse_lazy('account:home')  # بعد از دیلت مقاله به این ادرس ریدارکت میشه
    template_name= "registration/article_model_confirm_delete.html" #   برای اینکه بعد از ریدایرکت بیاد بپرسه پاک کنم یا نه