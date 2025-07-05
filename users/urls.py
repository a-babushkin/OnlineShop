from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView, UserUpdateView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
]
