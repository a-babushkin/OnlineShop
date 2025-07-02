from django.urls import path

from .apps import BlogConfig
from .views import (BlogRecordCreateView, BlogRecordDeleteView,
                    BlogRecordDetailView, BlogRecordListView,
                    BlogRecordUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path("blog_record/", BlogRecordListView.as_view(), name="blog_record_list"),
    path("blog_record/<int:pk>/", BlogRecordDetailView.as_view(), name="blog_record_detail", ),
    path("blog_record/create/", BlogRecordCreateView.as_view(), name="blog_record_create"),
    path("blog_record/<int:pk>/edit/", BlogRecordUpdateView.as_view(), name="blog_record_edit", ),
    path("blog_record/<int:pk>/delete/", BlogRecordDeleteView.as_view(), name="blog_record_delete", ),
]
