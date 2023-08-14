from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('khoj/', views.KhojView.as_view(), name='khoj'),

    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('api/', views.KhojViewAPI.as_view(), name='api'),



]
