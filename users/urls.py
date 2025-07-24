from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from users.views import register_api
urlpatterns = [
    path('login/',views.login_View, name='login'),
    path('signup/', views.register_View, name='register'),
   path('register_api/', register_api.as_view(), name='register_api'),
]