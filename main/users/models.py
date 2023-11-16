from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)


class Group_chat(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото",
                              default='photos/2023/11/08/1.jpg')
    name = models.TextField(default="групповой чат")
    user2 = models.TextField(default='владелец')
    title2 = models.TextField(max_length=20, verbose_name="Название группового чата")
    title_group = models.TextField(verbose_name="Описание группового чата")


class GroupMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
