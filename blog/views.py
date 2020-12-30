from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Post
from .forms import AddPostForm, UpdatePostForm


def categories_list(request):
    categories = Category.objects.all()
    return render(
        request, 'blog/index.html', {'categories': categories}
    )


def posts_list(request):
    print(request.GET)
    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category_id=category)
    else:
        posts = Post.objects.all()
    return render(
        request, 'blog/posts_list.html', {'posts': posts}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request, 'blog/post_detail.html', {'post': post}
    )


def add_post(request):
    if request.POST:
        post_form = AddPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            return redirect(post.get_absolute_url())
    else:
        post_form = AddPostForm()
    return render(request, 'blog/add_post.html', {'post_form': post_form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_form = UpdatePostForm(request.POST or None, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect(post.get_absolute_url())
    return render(request, 'blog/update_post.html', {
        'post_form': post_form,
        'post': post
    })


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    return render(request, 'blog/delete_post.html')