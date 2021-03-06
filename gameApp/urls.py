from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/', views.newUser, name='newUser'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('newGame/', views.newGame, name='newGame'),
    path('edit/', views.edit, name='edit'),
    path('edit/<int:gameID>/', views.edit, name= 'edit'),
    path('delete/<int:gameID>/', views.delete, name='delete'),
    path('savedGame/',views.saveNewGame, name='saveGame')
]