from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # Используем функцию  re_path  для определения URL-шаблона.
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
# В данном коде,  as_asgi()  используется для преобразования класса  ChatConsumer
# в ASGI-совместимый обработчик. Это позволяет Django использовать  ChatConsumer  для
# обработки входящих вебсокет-сообщений и взаимодействия с клиентом в режиме реального времени.
