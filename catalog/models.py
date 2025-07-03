from django.db import models


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
        related_name="categories",
        verbose_name="категория",
    )
    price = models.FloatField(verbose_name="цена за покупку")
    created_at = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="дата последнего изменения", auto_now=True
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]
