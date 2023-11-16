# path("admin/", admin.site.urls)  - это URL-шаблон
# для административного интерфейса Django.Когда пользователь переходит на URL-адрес
# admin/ , Django будет использовать  admin.site.urls  для обработки запроса.
from django.contrib import admin
from django.urls import path, include# path  используется для определения URL-шаблонов,
# а  include  - для включения других URL-конфигураций
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # для административного интерфейса Django.Когда пользователь переходит на URL-адрес
    # admin/ , Django будет использовать  admin.site.urls  для обработки запроса.
    #это URL-шаблон для приложения чата. Когда пользователь переходит на URL-адрес  chat/ ,
    # Django будет включать URL-конфигурацию из модуля  chat.urls  для обработки запроса.
    # Это позволяет определить дополнительные URL-шаблоны для функциональности чата.
    path("chat/", include("chat.urls")),
    path("user/", include("users.urls")),
]
