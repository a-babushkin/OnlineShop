from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'description', 'image', 'price', 'category']
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'description', 'image', 'price', 'category']
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        response_message = f"Пользователь: {name}, с телефоном: {phone}. Сообщение: {message}"
        return HttpResponse(response_message)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Дополните контекст дополнительными данными, если потребуется
        return context


def contacts(request):
    """Контроллер страницы Контакты"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")
    return render(request, 'contacts.html')
