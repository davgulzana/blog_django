from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Category, Post
from .forms import AddPostForm, UpdatePostForm


class CategoriesListView(ListView):
    model = Category
    template_name = 'blog/index.html'
    context_object_name = 'categories'


class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class ViewsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return self.object.get_absolute_url()


class AddPostView(LoginRequiredMixin, ViewsMixin, CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = AddPostForm

    def form_valid(self, form):
        user = self.request.user
        post = form.save(commit=False)
        post.user = user
        post.save()
        return redirect(post.get_absolute_url())


class UpdatePostView(ViewsMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdatePostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home-page')
