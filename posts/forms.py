from django import forms

from posts.models import Post, PostTags


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'category', 'cover_image', 'tags']


# class PostTagForm(forms.ModelForm):
#     class Meta:
#         model = PostTags
#         fields = ['post', 'tag', 'added_by']