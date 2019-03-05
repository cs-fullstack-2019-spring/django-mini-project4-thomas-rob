from django.shortcuts import render , redirect    # pulling redirect
from django.http import HttpResponse
# Create your views here.
from .forms import GameModel,GameCollectorModel,GameForm,GameCollectorForm  #called all forms in models in single line

def index(request):  #for the rendering of the index page
    gameList = GameModel.objects.all()  # this collects all games made
    gameCollector = GameCollectorModel.objects.filter(userIDkey =request.user)  # this gets current logged in user

    context= \
        {
            'user':gameCollector,  #this converts the gamecollector to user
            'gameList':gameList   # this addes completed game list that will later filter out based on logged in user
        }
    return render(request,'gameApp/index.html',context)  # this renders the page and start at index


def newUser(request):   #for adding a new user
    userForm = GameCollectorForm()   #collects the form necessary to make a new user

    context = \
        {
            'form':userForm  # gets the form to add new user and uses an easy to read name
        }
    return render(request,'gameApp/newUser.html',context)