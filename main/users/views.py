from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages# messages  из  django.contrib  для вывода сообщений об ошибках.
from .forms import RegistrationForm
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Добавьте здесь логику для обработки успешной регистрации
            return redirect('/chat')
        else:
            # Добавьте здесь логику для обработки неверных данных формы
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = redirect('/chat')

            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            print('USER', refresh)
            response.set_cookie('access_token', access)

            return response
        else:
            messages.error(request, "Invalid login credentials. Please try again.")

    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

