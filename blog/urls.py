from django.urls import path
from .views import categories_list, posts_list, post_detail


urlpatterns = [
    path('', categories_list, name='home-page'),
    path('posts/', posts_list, name='posts-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
]