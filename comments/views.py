from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from posts.models import Post
from comments.forms import CommentForm
from django.http import HttpResponseForbidden
from comments.models import Comment


@require_http_methods(['POST'])
@login_required
def rate_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

        return JsonResponse({
            'success': True,
            'comment_html': render_to_string('comment.html', {'comment': comment}, request=request)
        })
    return JsonResponse({'success': False, 'errors': form.errors})



@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user or request.user == comment.post.user:
        comment.delete()
    return redirect('site:posts:details', slug=comment.post.slug)
