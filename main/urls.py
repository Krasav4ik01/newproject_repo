from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('index1/', views.addpage, name='index1'),
    path('reg/', views.reg, name='reg'),

    path('index/', views.index),
   
   
    path('test/', views.test, name='test'),
   

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)