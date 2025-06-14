from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from catalog.models import Product, Category


def home(request):
    """Контроллер Главной страницы"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product_details(request, pk):
    """Контроллер страницы полной информации о товаре"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)


def contacts(request):
    """Контроллер страницы Контакты"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")
    return render(request, 'contacts.html')


def add_product(request):
    """Контроллер страницы Добавления нового товара"""

    categories = Category.objects.all()
    context = {'categories': categories}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')
        category = request.POST.get('category')
        product = Product(
            title=title,
            description=description,
            image=image,
            price=price,
            created_at=created_at,
            updated_at=updated_at,
            category_id=category
        )
        product.save()
        return redirect('/catalog/home/')
    return render(request, 'add_product.html', context)
