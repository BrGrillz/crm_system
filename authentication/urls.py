from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CreateUserAPIView, UsersListAPIView, UserChangeAPIView


urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name='Create new user'),
    path('login/', TokenObtainPairView.as_view(), name='auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('list/', UsersListAPIView.as_view(), name='User list'),
    path('manage/<int:pk>/', UserChangeAPIView.as_view(), name='User manage'),
]
