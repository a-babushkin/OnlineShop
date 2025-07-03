from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


# Функция проверки запрещенных слов
def check_for_forbidden_words(value):
    for item in value.split():
        if item in forbidden_words:
            raise ValidationError(f"Вы ввели запрещенное слово: {item}")


# Форма модели Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]

    # Стилизация полей формы
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

    # Валидатор для проверки название на запрещенные слова
    def clean_title(self):
        title = self.cleaned_data.get("title")
        check_for_forbidden_words(title)
        return title

    # Валидатор для проверки описания на запрещенные слова
    def clean_description(self):
        description = self.cleaned_data.get("description")
        check_for_forbidden_words(description)
        return description


# Форма модели Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "image", "category", "price"]

    # Стилизация полей формы
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["image"].widget.attrs.update({"class": "form-control"})

        self.fields["category"].widget.attrs.update({"class": "form-select"})

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену товара"}
        )

    # Валидатор для проверки названия на запрещенные слова
    def clean_title(self):
        title = self.cleaned_data.get("title")
        check_for_forbidden_words(title)
        return title

    # Валидатор для проверки описания на запрещенные слова
    def clean_description(self):
        description = self.cleaned_data.get("description")
        check_for_forbidden_words(description)
        return description

    # Валидатор для проверки цены на отрицательность
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(f"Цена не может быть отрицательной: {price}")
        return price

    # Валидатор для проверки формата и размера файла
    def clean_image(self):
        image = self.cleaned_data.get("image")

        if not image:
            raise forms.ValidationError("Изображение обязательно.")

        # Проверка расширения файла (формата)
        valid_extensions = (".jpg", ".jpeg", ".png")
        extension = str(image).lower().endswith(valid_extensions)
        if not extension:
            raise forms.ValidationError(
                f"Поддерживаются только файлы форматов {valid_extensions}."
            )

        # Проверка размера файла (не больше 5MB)
        max_size = 5 * 1024 * 1024  # 5 MB
        if image.size > max_size:
            raise forms.ValidationError(
                f"Размер файла превышает максимальный допустимый ({max_size / (1024 * 1024)} МБ)"
            )

        return image
