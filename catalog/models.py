from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """Описание модели Категорий"""

    title = models.CharField(max_length=250, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["title"]


class Product(models.Model):
    """Описание модели Товара"""

    title = models.CharField(max_length=250, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(verbose_name="изображение", upload_to="uploads/")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category",
        verbose_name="категория",
    )
    price = models.FloatField(verbose_name="цена за покупку")
    is_published = models.BooleanField(verbose_name="статус публикации", default=False)
    created_at = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="дата последнего изменения", auto_now=True
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Владелец",
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
