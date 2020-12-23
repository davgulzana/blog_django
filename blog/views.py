from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def categories_list(request):
    categories = Category.objects.all()
    return render(
        request, 'blog/index.html', {'categories': categories}
    )


def posts_list(request):
    posts = Post.objects.all()
    return render(
        request, 'blog/posts_list.html', {'posts': posts}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request, 'blog/post_detail.html', {'post': post}
    )