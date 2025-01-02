from django.urls import path 
from . import views 


urlpatterns =[
    path('', views.index, name='cart.index'),
    path('<int:id>/add/', views.add, name='cart.add'),
    path('clear/', views.clear, name='cart.clear'),
    path('purchase/', views.purchase, name='cart.purchase'),
    
    
   #NOTE -  path('remove/<int:movie_id>', views.remove_from_cart, name='cart.remove_from_cart'),
    #NOTE - path('show', views.show_cart, name='cart.show_cart'),
]