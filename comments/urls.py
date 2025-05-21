from django.urls import path

from comments.views import rate_post, delete_comment

app_name = 'comments'

urlpatterns = [
    path('create/', rate_post, name='rate'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]