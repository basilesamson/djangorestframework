from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author-list'),
    path('<int:pk>/', views.author_detail, name='author-detail'),
    path('create/', views.create_author, name='create-author'),
]