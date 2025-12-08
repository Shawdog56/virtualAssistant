from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def dashboard(request):
    return render(request, 'user/dashboard.html')

def pusuas(request):
    return render(request,'pusuas.html')

def register(request):
    return render(request, 'register.html')

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