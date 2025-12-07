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
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('register/', views.register, name='register'),
    path('pusuas/', views.pusuas, name='pusuas')
]