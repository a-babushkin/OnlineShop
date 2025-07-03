from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from catalog.views import ContactView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view()),
    path("admin/", admin.site.urls),
    path("catalog/contacts/", ContactView.as_view(), name="contacts"),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("blog/", include("blog.urls", namespace="blog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
