from django.urls import path


from . import views


# Создаем переменную  urlpatterns ,
# которая является списком URL-шаблонов для обработки HTTP-запросов.
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
 ]
