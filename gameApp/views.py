from django.shortcuts import render , redirect    # pulling redirect
from django.http import HttpResponse
# Create your views here.
from .forms import GameModel,GameCollectorModel,GameForm,GameCollectorForm  #called all forms in models in single line
from django.contrib.auth.models import User
def index(request):  #for the rendering of the index page
    gameList = GameModel.objects.all()  # this collects all games made

    context= \
        {
            'gameList':gameList   # this addes completed game list that will later filter out based on logged in user
        }
    return render(request,'gameApp/index.html',context)  # this renders the page and start at index


def newUser(request):   #for adding a new user
    userForm = GameCollectorForm(request.POST or None)   #collects the form necessary to make a new user

    if userForm.is_valid():  # confirms that the parameters are met
        if request.POST['password1'] == request.POST['password2']:  #adds aditional parameter
            User.objects.create_user(request.POST['username'],'',request.POST['password1']) # saves the user for use later
            userForm.save()   # saves the form for editing later
            return redirect('index')  #returns person to index


    context = \
        {
            'form':userForm  # gets the form to add new user and uses an easy to read name
        }
    return render(request,'gameApp/newUser.html',context)
