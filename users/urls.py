from django.urls import path
from .views import RegisterUserView, UpdateUserView, ListUserView, LoginView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('users/', ListUserView.as_view(), name='list_users'),
    path('users/<uuid:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
]
