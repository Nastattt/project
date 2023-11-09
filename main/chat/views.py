from django.shortcuts import render, redirect#render  используется для отображения HTML-шаблонов,
import datetime
# а  redirect  - для перенаправления на другую страницу.



def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "chat/index.html")


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('login')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "chat/room.html", {"room_name": room_name, "current_time": current_time})

