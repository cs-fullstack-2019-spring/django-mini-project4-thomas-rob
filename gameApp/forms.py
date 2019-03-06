from django import forms
from .models import GameCollectorModel, GameModel


class GameCollectorForm(forms.ModelForm):
    class Meta:
        model = GameCollectorModel
        exclude = ['accountCreationDate','userIDkey']


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ['gameMakeIdKey']
