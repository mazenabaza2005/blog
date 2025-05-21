# from django.urls import include, path
# app_name = 'api'
# urlpattern = [
#     path('posts/', include('posts.urls_api', namespace='posts')),
# ]


from django.urls import path, include
from posts.views_api import PostListAPIView, PostDetailAPIView

app_name = "api"

urlpatterns = [
    path('posts/', include('posts.urls_api', namespace='posts')),
    path('authn/', include('authn.urls_api', namespace='authn')),   
]
