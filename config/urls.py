
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    

]+static(settings.MEDIA_URL ,  document_root=settings.MEDIA_ROOT)


