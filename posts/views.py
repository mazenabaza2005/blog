from http.client import HTTPResponse

from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import autoescape
from django.views import View
from django.views.generic import ListView

# from comments.forms import CommentForm
from posts.forms import PostForm
from posts.models import Post, PostTags
from classifications.models import Category
from classifications.models import Tag
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.utils import timezone

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=False)


class PostDetailsView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return render(request, 'post_detail.html', context={'post': post})


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'form.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            tags = form.cleaned_data.get('tags', [])
            for tag in tags:
                PostTags.objects.create(post=post, tag=tag, added_by=request.user)
            form.save_m2m()
            print(f"Post author: {post.author}, User: {request.user} is Saved")
            return redirect('site:posts:list') # now it should redirect to the list after saving the post
        return render(request, 'form.html', context={'form': form})
    


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        if post.author != request.user:
            return HttpResponseForbidden()
        form = PostForm(instance=post)
        return render(request, 'form.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])

        if post.author != request.user:
            return HttpResponseForbidden()

        form = PostForm(instance=post, data=request.POST, files=request.FILES)

        if form.is_valid():
            tags = form.cleaned_data.get('tags', [])  # ✅ get selected tags
            updated_post = form.save(commit=False)    # ✅ create object but don't save yet
            updated_post.save(tags=tags)              # ✅ pass tags to your custom save()
            form.save_m2m()                           # ✅ save any many-to-many fields

            return redirect('site:posts:details', post.slug)

        return render(request, 'form.html', context={'form': form})
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('site:posts:list')  # Adjust to your homepage or posts list

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can delete
