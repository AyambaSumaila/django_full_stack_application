from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='movieapp.index'),
    path('<int:id>/', views.show, name='movieapp.show'),
    path('<int:id>/review/create/', views.create_review, name='movieapp.create_review'),
    
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movieapp.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movieapp.delete_review'),
]
