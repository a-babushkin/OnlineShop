from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CategoryCreateView, CategoryDeleteView,
                           CategoryDetailView, CategoryListView,
                           CategoryUpdateView, ContactView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path(
        "category/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("", ProductListView.as_view(), name="product_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
