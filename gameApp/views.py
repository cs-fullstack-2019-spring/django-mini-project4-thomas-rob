from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import GameModel,GameCollectorModel,GameForm,GameCollectorForm

def index(request):
    gameList = GameModel.objects.all()

    context= \
        {
            'gameList':gameList
        }
    return render(request,'gameApp/index.html',context)