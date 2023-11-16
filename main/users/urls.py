from django.urls import path

from . import views
from .forms import GroupADD

# views  для импорта функций представлений.

urlpatterns = [
    path("signup/", views.register_view, name='signup'),
    path("", views.login_view, name="login"),
    path("confirm-code/", views.confirm_code_view, name='confirm_code'),
    path("group_add/", GroupADD)
]
