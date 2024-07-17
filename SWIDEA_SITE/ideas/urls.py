# ideas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/register/', views.idea_register, name='idea_register'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('devtool/register/', views.devtool_register, name='devtool_register'),
    path('devtool/list/', views.devtool_list, name='devtool_list'),
    path('devtool/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtool/<int:pk>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtool/<int:pk>/delete/', views.devtool_delete, name='devtool_delete'),
    path('idea/<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
]
