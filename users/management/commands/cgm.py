from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    """Команда для заполнения групп с настроенными правами"""
    def handle(self, *args, **options):
        # Создаем новую группу «Модератор продуктов»
        product_moderator = Group.objects.create(name="Модератор продуктов")
        # Получаем разрешения
        delete_product_permission = Permission.objects.get(codename="delete_product")
        can_unpublish_product_permission = Permission.objects.get(
            codename="can_unpublish_product"
        )
        # Назначаем разрешения группе
        product_moderator.permissions.add(
            delete_product_permission, can_unpublish_product_permission
        )
        # Создаем пользователя
        user = CustomUser.objects.create(email="exampl@mail.ru")
        user.set_password("12345")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
        # Добавляем пользователя в группу «Модератор продуктов»
        user.groups.add(product_moderator)
