from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import CategoryForm, ProductForm
from catalog.models import Category, Product

"""Блок CRUD для Category"""


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("catalog:category_list")


"""Блок CRUD для Product"""


class ProductListView(ListView):
    model = Product

    # Метод проверки вхождения пользователя в группу Модератор продуктов
    def get_is_moderator(self):
        return self.request.user.groups.filter(name="Модератор продуктов").exists()

    # Метод переопределения исходного набора данных
    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.get_is_moderator():
            queryset = queryset.filter(is_published=True)

        return queryset

    # Метод установки дополнительного контекста
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_moderator"] = self.get_is_moderator()
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    # Метод корректности введённых данных формы
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    # Метод проверки, обладает ли текущий пользователь необходимым уровнем доступа
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.has_perm(
            "catalog.can_unpublish_product"
        )

    # Метод действий на случай неудачной проверки прав доступа
    def handle_no_permission(self):
        messages.error(self.request, _("У вас нет достаточных прав."))
        return HttpResponseForbidden()


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    # Метод проверки, обладает ли текущий пользователь необходимым уровнем доступа
    def test_func(self):
        obj = self.get_object()
        return (
            obj.owner == self.request.user
            or self.request.user.groups.filter(name="Модератор продуктов").exists()
        )

    # Метод действий на случай неудачной проверки прав доступа
    def handle_no_permission(self):
        messages.error(self.request, _("У вас нет достаточных прав."))
        return HttpResponseForbidden()


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = "contacts.html"

    # Метод обработки данных, отправленных через форму
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        response_message = (
            f"Пользователь: {name}, с телефоном: {phone}. Сообщение: {message}"
        )
        return HttpResponse(response_message)

    # Метод установки дополнительного контекста
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def contacts(request):
    """Контроллер страницы Контакты"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}"
        )
    return render(request, "contacts.html")
