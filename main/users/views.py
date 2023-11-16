from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ConfirmCodeForm, GroupADD
import random
from django.shortcuts import render, redirect
from django.urls import reverse


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Создание кода подтверждения
            confirmation_code = ''.join(random.choices('0123456789', k=4))

            # Сохранение кода в сессии
            request.session['confirmation_code'] = confirmation_code
            request.session['username'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']
            request.session['password'] = form.cleaned_data['password']

            # Отправка кода на почту
            send_confirmation_email(request.POST['email'], confirmation_code)

            # Перенаправление на страницу ввода кода
            return redirect('confirm_code')
        else:
            # Обработка неверных данных формы
            return render(request, 'auth/register.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'auth/register.html', {'form': form})


def send_confirmation_email(email, code):
    subject = 'Код подтверждения для регистрации'
    message = f'Ваш код для регистрации: {code}'
    from_email = 'test_userss@mail.ru'  # Замените на ваш email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


def confirm_code_view(request):
    if request.method == 'POST':
        form = ConfirmCodeForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['code']

            correct_code = request.session.get('confirmation_code')

            if entered_code == correct_code:
                # Предполагая, что у вас есть room_name, сохраненный в сессии или где-то еще
                room_name = 'room'  # Замените на фактический room_name

                # Перенаправление на представление room с указанием room_name
                return redirect(reverse('room', kwargs={'room_name': room_name}))
            else:
                form.add_error('code', 'Неверный код подтверждения')
    else:
        form = ConfirmCodeForm()

    return render(request, 'auth/confirm_code.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = redirect('/chat')
# todo нужно сделать передачу через locallho
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


def form_group(request):
    if request.method == 'POST':
        form = GroupADD(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/main')
    else:
        form = GroupADD(request.GET)
    return render(request, "group_add.html", {'form': form})