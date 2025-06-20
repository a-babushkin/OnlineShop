from datetime import timezone

from django.db import models

class BlogRecord(models.Model):
    """Описание модели записи блога"""
    title = models.CharField(max_length=250, verbose_name='наименование')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='изображение', upload_to='uploads/blog_img')
    is_published = models.BooleanField(verbose_name='признак публикации', default=False)
    views_number = models.IntegerField(verbose_name='количество просмотров',default=0)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published_date = models.DateTimeField(verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title} - {self.views_number}'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
        ordering = ['published_date']
