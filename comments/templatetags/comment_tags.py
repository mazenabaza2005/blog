from django import template

from comments.forms import CommentForm
from comments.models import Comment

register = template.Library()

@register.inclusion_tag('comment_section.html', takes_context=True)
def render_comment(context, post):
    request = context['request']
    form = CommentForm()
    # for editing
    # edit_form = CommentForm(instance=Comment.objects.get(id=1))
    comments = post.comments.all().order_by('-created_at')
    return {
        'form': form,
        # 'edit_form': edit_form,
        'comments': comments,
        'post': post,
        'request': request,
    }