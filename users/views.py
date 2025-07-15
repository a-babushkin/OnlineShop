import os

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomAuthenticationForm, CustomUserCreationForm, ProfileForm
from .models import CustomUser


class RegisterView(CreateView):
    """Класс для регистрации нового пользователя"""
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")

    # Метод отправки письма после валидации формы
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        permission = Permission.objects.get(codename="delete_product")
        user.user_permissions.remove(permission)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    # Метод отправки приветственного письма
    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        from_email = os.getenv("EMAIL_HOST_USER")
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    """Класс входа пользователя в систему"""
    form_class = CustomAuthenticationForm
    template_name = "users/login.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = "users/profile_form.html"
    success_url = reverse_lazy("home")
