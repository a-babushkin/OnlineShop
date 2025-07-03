from django import forms
from django.core.exceptions import ValidationError

from .models import BlogRecord

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


# Форма модели BlogRecord
class BlogRecordForm(forms.ModelForm):
    class Meta:
        model = BlogRecord
        exclude = ["views_number", 'created_at']

    # Стилизация полей формы
    def __init__(self, *args, **kwargs):
        super(BlogRecordForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите текст"}
        )

        self.fields["image"].widget.attrs.update({"class": "form-control"})

        self.fields["is_published"].widget.attrs.update({"class": "form-check-input"})

        self.fields["published_date"].widget.attrs.update(
            {"class": "form-control", 'type': 'date', "placeholder": "Введите дату публикации"}
        )

    # Валидатор для проверки названия на запрещенные слова
    def clean_title(self):
        title = self.cleaned_data.get("title")
        check_for_forbidden_words(title)
        return title

    # Валидатор для проверки описания на запрещенные слова
    def clean_content(self):
        content = self.cleaned_data.get("content")
        check_for_forbidden_words(content)
        return content

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
