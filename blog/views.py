from django.db.models import F
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogRecord


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        return BlogRecord.objects.filter(is_published=True)


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = ['title', 'content', 'image', 'is_published', 'views_number', 'published_date']
    success_url = reverse_lazy('blog:blog_record_list')


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.obj = super().get_object(queryset)
        self.obj.views_number += 1
        self.obj.save()
        return self.obj


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ['title', 'content', 'image', 'is_published', 'views_number', 'published_date']
    # template_name = 'blog_record_form.html'
    # success_url = reverse_lazy('blog:blog_record_detail')

    def get_success_url(self):
        return reverse_lazy('blog:blog_record_detail', kwargs={'pk': self.object.pk})

class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    # template_name = 'blog_record_delete.html'
    success_url = reverse_lazy('blog:blog_record_list')
