from django.urls import path 
from . import views 

urlpatterns = [
    path('signup', views.signup, name='accountsapp.signup'),
    path('login/', views.login, name='accountsapp.login'),
    path('logout/', views.logout, name='accountsapp.logout'),
    path('orders/', views.orders, name='accountsapp.orders'),
    
    
    
]
