import datetime  # Импортируем модуль json для работы с данными в формате JSON
import json

from channels.generic.websocket import \
    AsyncWebsocketConsumer  # Импортируем базовый класс для WebSocket-потребителей из библиотеки Channels


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Извлекаем имя комнаты из URL-маршрута и сохраняем его в self.room_name
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # Формируем имя группы чата, к которой присоединятся клиенты
        self.room_group_name = f"chat_{self.room_name}"
        # Получаем имя пользователя из контекста, либо устанавливаем "Anonymous", если пользователь не аутентифицирован
        self.username = self.scope.get('user').username if self.scope.get('user') else 'Anonymous'

        # Добавляем соединение клиента к группе чата, чтобы можно было отправлять сообщения всем участникам группы
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Принимаем WebSocket-соединение
        await self.accept()
        # Отправляем клиенту приветственное сообщение с именем пользователя
        await self.send(text_data=json.dumps({"message": f"Welcome, {self.username}!"}))

    async def disconnect(self, close_code):
        # Удаляем соединение клиента из группы чата при отключении
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def get_current_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    async def receive(self, text_data=None, bytes_data=None):
        current_time = await self.get_current_time()
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        if not message == "":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "username": self.username,
                    "message": message,
                    "time": current_time,
                }
            )

    async def chat_message(self, event):
        username = event["username"]
        message = event["message"]
        time = event["time"]
        await self.send(text_data=json.dumps({
            "message": f"{username}: {message} {time}",
        }))
