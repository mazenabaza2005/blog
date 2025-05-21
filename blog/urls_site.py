from django.urls import include, path
from posts import views_api as views


app_name = 'site'
urlpatterns = [
    path('authn/',include('authn.urls',namespace='authn')),
    path('',include('posts.urls',namespace='posts')),


]