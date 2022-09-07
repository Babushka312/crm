from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from blog.views import PostSerializer
from account.views import (
    MyObtainPairView,
    RegisterView,
    UserListApiView,
    UserDetailApiView
)

urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user'),
    path('detail/<int:id>', UserDetailApiView.as_view(), name='detail'),
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]