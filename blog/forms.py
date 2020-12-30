from django import forms
from django.contrib.auth import get_user_model

from .models import Category, Post

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, required=True, strip=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
#     text = forms.CharField(required=True)
#     image = forms.ImageField(required=False)
#     author = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=True)
#
#     def save(self):
#         data = self.cleaned_data
#         print(data)
#         post = Post.objects.create(
#             title=data['title'], category_id=data['category'],
#             text=data['text'], author=data['author']
#         )


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image')
        # exclude = ('created_at', 'updated_at')


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'image')
