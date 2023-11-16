"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
# Создаем переменную  django_asgi_app , которая содержит ASGI-совместимое приложение Django,
# полученное с помощью функции  get_asgi_application() . Это позволяет инициализировать Django ASGI-приложение заранее,
# чтобы регистр приложений был заполнен перед импортом кода, который может импортировать модели ORM.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)  # Создаем переменную  application , которая является экземпляром класса  ProtocolTypeRouter .  ProtocolTypeRouter  используется для определения, какое приложение должно обрабатывать разные типы протоколов.
# В данном случае, у нас есть два типа протоколов: "http"и "websocket".
# Для протокола "http"мы используем  django_asgi_app , которое является ASGI-совместимым приложением Django.
# Для протокола "websocket" мы используем  AllowedHostsOriginValidator , который проверяет, что источник вебсокет-соединения находится в разрешенных хостах, и передаем в него  AuthMiddlewareStack , который обрабатывает аутентификацию пользователя, и  URLRouter  с  websocket_urlpatterns , который определяет URL-шаблоны для вебсокет-соединений.
