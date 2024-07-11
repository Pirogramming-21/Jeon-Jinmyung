from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', review_list, name='review_list'),  # 리뷰 리스트 페이지
    path('<int:review_id>/', review_detail, name='review_detail'),  # 리뷰 디테일 페이지
    path('create/', review_create, name='review_create'),  # 리뷰 작성 페이지
    path('<int:review_id>/update/', review_update, name='review_update'),  # 리뷰 수정 페이지
    path('<int:review_id>/delete/', review_delete, name='review_delete'),  # 리뷰 삭제
]
