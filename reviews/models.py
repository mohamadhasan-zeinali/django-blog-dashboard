from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields  import RichTextField

from django.urls import reverse

from django.contrib.auth.models import User

from django.utils.html import format_html

class Category(models.Model):
    title=models.CharField(max_length=100, verbose_name="title")
    slug=models.CharField(max_length=50,verbose_name="url")
    description=models.CharField(max_length=500, verbose_name="desciption")
    status=models.BooleanField(default=True ,verbose_name="status")

    class Meta:
            verbose_name="category "
            verbose_name_plural="categorys"

    def __str__(self):
        return self.title 
class Article_model(models.Model):
    STATUS_CHOICES=(
        (   ' P ' , 'PUBLISH'),
        (    ' d ' , 'DRAFT'),
        
        ('x' , 'blog')
    )
    auther=models.ForeignKey(User, null=True, on_delete=models.SET_NULL,verbose_name="auther",related_name='articles')
    title=models.CharField(max_length=100 ,  verbose_name="title" )
    slug=models.SlugField(max_length=50, verbose_name="url")
    category=models.ManyToManyField(Category,verbose_name="category",related_name="articles")
    #description=models.TextField(max_length=500, verbose_name="description")
    description =RichTextField(blank="True", null="True")
    description =RichTextUploadingField(blank="True", null="True")
    thumbnail=models.ImageField(upload_to="images",verbose_name="picture-url")
    date=models.DateTimeField(auto_now_add=timezone.now)
    status=models.CharField(max_length=3,choices=STATUS_CHOICES , verbose_name="status")
    

    class Meta:
            verbose_name="Article "
            verbose_name_plural="Articles"


    def  thumbnail_tag(self) :
        return format_html("<img src='{}' width=200>".format(self.thumbnail.url) )
    thumbnail_tag.short_description="picture"

    #convert field many to many  TO  string
    def category_to_str(self):
        return ", " .join([category.title for category in self.category.all()])
    category_to_str.short_description="category"

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("account:home")