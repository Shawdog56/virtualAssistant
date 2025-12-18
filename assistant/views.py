from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from datetime import datetime
from assistant.forms import RegisterForm


# Create your views here.

def dashboard(request):
    user = request.user
    return render(
        request, 
        'user/dashboard.html',
        {
            'username': user.username,
            'fname': f"{user.first_name} {user.last_name}",
            'joined': user.date_joined.date()
        }
    )

def pusuas(request):
    return render(request,'pusuas.html')

def register(request):
    if request.method == "POST":
        try:
            form = RegisterForm(request.POST)
            print(form)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password1"])
                user.save()
                messages.success(request, "Usuario registrado correctamente")
                return redirect("/login/")
        except Exception as e:
            print(e)
            form = RegisterForm()
    else:
        form = RegisterForm()

    return render(
        request, 
        'register.html',
        {
            "form": form
        }
        )

def recoverpasswd(request):
    return render(request,'recoverpasswd.html')

def sidebar(request):
    return render(request, 'layout/sidebar.html')

def musicExplore(request):
    return render(request, 'music/explore.html')

def musicPrincipal(request):
    return render(request, 'music/principal.html')

def devicesAdd(request):
    return render(request, 'devices/add.html')

def devicesManage(request):
    return render(request, 'devices/manage.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)