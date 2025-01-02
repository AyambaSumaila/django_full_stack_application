from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name='homeapp.index'),
    path('about', views.about, name='about'),
    
    
]
