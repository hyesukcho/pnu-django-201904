from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# FIXME: accounts는 app_name을 쓰지 않습니다.
# app_name = ''

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
]
