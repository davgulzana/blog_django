from django.urls import path

from .views import categories_list, posts_list, \
    post_detail, add_post, update_post, delete_post
from .class_views import CategoriesListView, PostsListView, \
    PostDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', CategoriesListView.as_view(), name='home-page'),
    path('posts/', PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add/', AddPostView.as_view(), name='add-post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
]