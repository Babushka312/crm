from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListApiView, PostCreateApiView, PostDetailApiView, PostUpdateApiView, PostDeleteApiView

urlpatterns = [
    path('list/', PostListApiView.as_view(), name='list'),
    path('create/', PostCreateApiView.as_view(), name='create'),
    path('update/<int:id>', PostUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>', PostDeleteApiView.as_view(), name='delete'),
    path('detail/<int:id>', PostDetailApiView.as_view(), name='detail'),
]

