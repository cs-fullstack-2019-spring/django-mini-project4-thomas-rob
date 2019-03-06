from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404  # pulling redirect
from django.http import HttpResponse
# Create your views here.
from .forms import GameModel, GameCollectorModel, GameForm, \
    GameCollectorForm  # called all forms in models in single line
from django.contrib.auth.models import User
from .models import GameModel
def index(request):  #for the rendering of the index page
    gameList = GameModel.objects.all()  # this collects all games made


# @login_required
def index(request):  # for the rendering of the index page
    if request.user == 'AnonymousUser':
        gameCollector=''
        gameList=''
    else:
        gameCollector = GameCollectorModel.objects.get(userIDkey=request.user)  # this gets the game collector
        gameList = GameModel.objects.filter(gameMakeIdKey=gameCollector)  #this gets the list of games that person did
    context = \
        {
            'gameList': gameList  # this adds completed game list that will later filter out based on logged in user
        }
    return render(request, 'gameApp/index.html', context)  # this renders the page and start at index


def newUser(request):  # for adding a new user
    userForm = GameCollectorForm(request.POST or None)  # collects the form necessary to make a new user

    if userForm.is_valid():  # confirms that the parameters are met
        if request.POST['password1'] == request.POST['password2']:  # adds aditional parameter
            User.objects.create_user(request.POST['username'], '',request.POST['password1'])  # saves the user for use later
            userForm.save()  # saves the form for editing later
             # this adds the user as the link for the foreignKey
             #saves the foreignKey
            return redirect('index')  # returns person to index

    context = \
        {
            'form': userForm  # gets the form to add new user and uses an easy to read name
        }
    return render(request, 'gameApp/newUser.html', context)


def newGame(request):  # this will render the newgame page to save a new game
    gameForm = GameForm()  # this collects the form to use
    context = \
        {
            'form': gameForm  # this changed the name to fit the context for easy to input
        }
    return render(request, 'gameApp/newGame.html', context)

def edit(request, gameID):
    item = get_object_or_404(GameModel, pk=gameID)
    editForm = GameForm( instance=item)

    context = \
        {
            'form':editForm
        }
    if request.method == 'POST':
        editForm.save()
        return (request, 'gameApp/editForm.html', context)
    return render(request, 'gameApp/editForm.html', context)

def delete(request, gameID):
    deleteForm = get_object_or_404(GameModel, pk=gameID)
    deleteForm.delete()
    return redirect('index')

@login_required
def saveNewGame(request):  # this will upon submitting a newgame save it and redirect to the index
    gameCollector = GameCollectorModel.objects.get(userIDkey=request.user)  # this gets the game collector
    gameForm = GameForm(request.POST)
    # print(gameForm)
    # collects the data inputed by user to be saved
    newGame = gameForm.save(commit=None)  # saves the data for future use
    newGame.gameMakeIdKey=gameCollector
    newGame.save()
    return redirect('index')  # goes back to the index page
