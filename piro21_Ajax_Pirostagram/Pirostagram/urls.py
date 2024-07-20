from django.urls import path
from . import views

app_name = 'Pirostagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    # path('post_detail/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
]
