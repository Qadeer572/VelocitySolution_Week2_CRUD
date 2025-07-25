from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from users.views import register_api,login_api,contact
urlpatterns = [
    path('login/',views.login_View, name='login'),
    path('signup/', views.register_View, name='register'),
    path('register_api/', register_api.as_view(), name='register_api'),
    path('login_api/', login_api.as_view(), name='login_api'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('contact/', contact.as_view(), name='contact'),
]