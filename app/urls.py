from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('khoj/', views.KhojView.as_view(), name='khoj'),

    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('api/get-all-input-values/', views.KhojViewAPI.as_view(), name='api'),

    path('gettoken/', views.get_token, name='gettoken'),
    path('api-docs/', views.api_docs, name='apidocs'),


]
