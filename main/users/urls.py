from django.urls import path#views  для импорта функций представлений.
from . import views


urlpatterns = [
    path("signup", views.register_view, name='signup'),
    path("", views.login_view, name="login")
]
