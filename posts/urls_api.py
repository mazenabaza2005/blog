from django.urls import path

from posts.views_api import PostListAPIView  
from . import views
app_name = 'posts' 

urlpatterns = [
    
    path('', PostListAPIView.as_view(), name='list'),
]