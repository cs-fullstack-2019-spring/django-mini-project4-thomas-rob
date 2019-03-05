from django.shortcuts import render , redirect    # pulling redirect
from django.http import HttpResponse
# Create your views here.
from .forms import GameModel,GameCollectorModel,GameForm,GameCollectorForm  #called all forms in models in single line
from django.contrib.auth.models import User
def index(request):  #for the rendering of the index page
    gameList = GameModel.objects.all()  # this collects all games made
    # gameCollector = GameCollectorModel.objects.filter(userIDkey =request.user)  # this gets current logged in user

    context= \
        {
#            'user':gameCollector,  #this converts the gamecollector to user
            'gameList':gameList   # this addes completed game list that will later filter out based on logged in user
        }
    return render(request,'gameApp/index.html',context)  # this renders the page and start at index


def newUser(request):   #for adding a new user
    userForm = GameCollectorForm(request.POST or None)   #collects the form necessary to make a new user

    if userForm.is_valid():
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'],'',request.POST['password1'])
            userForm.save()
            return HttpResponse('New User Created')


    context = \
        {
            'form':userForm  # gets the form to add new user and uses an easy to read name
        }
    return render(request,'gameApp/newUser.html',context)