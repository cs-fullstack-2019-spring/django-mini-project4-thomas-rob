from django.contrib import admin
from django.urls import path, include
from . import views
from .models import deleteForm

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('newUser/', views.newUser, name='newUser'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('newGame/', views.newGame, name='newGame'),
    path('edit/', views.edit, name='edit'),
    path('edit/', views.delete, name= 'deleteForm'),
    path('delete/<int:gameID>/', views.delete, name='delete'),
    path('savedGame/',views.saveNewGame, name='saveGame')
]