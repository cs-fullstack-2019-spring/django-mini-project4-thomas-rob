from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('newUser/', views.newUser, name='newUser'),
    path('accounts/', include('django.contrib.auth.urls')),
]