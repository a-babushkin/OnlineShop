from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_details, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('add_product/', add_product, name='add_product'),
    path('product_details/<int:pk>/', product_details, name='product_details')
]
