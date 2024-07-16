# ideas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/register/', views.idea_register, name='idea_register'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
]
