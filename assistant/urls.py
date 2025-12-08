from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='index.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('recoverpasswd/', views.recoverpasswd, name='recoverpasswd'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('devices/manage/', login_required(views.devicesManage), name='devicesManage'),
    path('devices/add/', login_required(views.devicesAdd), name='devicesAdd'),
    path('music/explore', login_required(views.musicExplore), name='musicExplore'),
    path('music/principal', login_required(views.musicPrincipal), name='musicPrincipal'),
    path('pusuas/', views.pusuas, name='pusuas'),
    path('sidebar/', views.sidebar, name='sidebar'),
]