from django.urls import include, path
from . import views
from .views import PostListView, PostDetailsView, PostCreateView, PostUpdateView, PostDeleteView


app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view()  , name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug:slug>/', PostDetailsView.as_view(), name='details'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug:slug>/comment/', include('comments.urls', namespace='comments')),
    path('posts/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]