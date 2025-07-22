from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('login/',views.login_View, name='login'),
    path('signup/', views.register_View, name='register'),
]