from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=13)
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="users/avatars/", null=True, blank=True
    )


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")
    icon = models.FileField(verbose_name="Иконка", upload_to="categories/icons/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
