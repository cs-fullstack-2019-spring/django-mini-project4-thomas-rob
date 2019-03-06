from django.contrib.auth.decorators import \
    login_required  # unused for now but for making sure the person on the page is logged in
from django.shortcuts import render, redirect, get_object_or_404  # pulling redirect
from django.http import HttpResponse  # used for testing purposes
# Create your views here.
from .forms import GameModel, GameCollectorModel, GameForm, \
    GameCollectorForm  # called all forms in models in single line
from django.contrib.auth.models import User  # Collects the user form from django to add users


def index(request):  # for the rendering of the index page
    gameList = GameModel.objects.all()  # this collects all games made


# @login_required
def index(request):  # for the rendering of the index page
    if request.user.is_authenticated:  # makes sure the user is logged in to authorize this existing
        gameCollector = GameCollectorModel.objects.get(userIDkey=request.user)  # this gets the game collector
        gameList = GameModel.objects.filter(gameMakeIdKey=gameCollector)  # this gets the list of games that person did

    else:
        gameList = ''  # sets gamelist to empty so no games will be displayed

    context = \
        {
            'gameList': gameList  # this adds completed game list that will later filter out based on logged in user
        }
    return render(request, 'gameApp/index.html', context)  # this renders the page and start at index


def newUser(request):  # for adding a new user
    userForm = GameCollectorForm(request.POST or None)  # collects the form necessary to make a new user
    if userForm.is_valid():  # confirms that the parameters are met
        if request.POST['password1'] == request.POST['password2']:  # adds additional parameter
            newUser = User.objects.create_user(request.POST['username'], '',
                                               request.POST['password1'])  # saves the user for use later
            collector = userForm.save(commit=None)  # saves the model
            collector.userIDkey = newUser  # saves the user created as the foreignkey for the game-collector model
            collector.save()  # saves the form for editing later
            return redirect('index')  # returns person to index
    context = \
        {
            'form': userForm  # gets the form to add new user and uses an easy to read name
        }
    return render(request, 'gameApp/newUser.html',
                  context)  # renders the newUser page if they don't have the information entered


def newGame(request):  # this will render the newgame page to save a new game
    gameForm = GameForm()  # this collects the form to use
    context = \
        {
            'form': gameForm  # this changed the name to fit the context for easy to input
        }
    return render(request, 'gameApp/newGame.html', context)  # renders the page to make the game


def edit(request, gameID):
    item = get_object_or_404(GameModel, pk=gameID)  # gets the game model to be edited
    editForm = GameForm(request.POST or None,
                        instance=item)  # grabs the form and fills it out with the info from the model
    if request.method == 'POST':  # makes sure the it has retrieved the information before continuing this route
        if editForm.is_valid():  # makes sure that the information entered is valid to requirements
            item.save()  # saves the new information entered to be used later
            return redirect('index')  # returns to index because you are done, info will display on screen
    context = \
        {
            'form': editForm  # this gets the form to be shown and changed
        }
    return render(request, 'gameApp/editForm.html',
                  context)  # renders the page for viewing the form information to edit


def delete(request, gameID):  # starts down the path to delete the game, this build does not have a conformation page
    deleteForm = get_object_or_404(GameModel, pk=gameID)  # collects the form to delete
    deleteForm.delete()  # deletes the form IMMEDIATELY UPON CLICKING THE LINK
    return redirect('index')  # returns to the index without turning back


def saveNewGame(request):  # this will upon submitting a new game save it and redirect to the index
    gameCollector = GameCollectorModel.objects.get(userIDkey=request.user)  # this gets the game collector
    gameForm = GameForm(request.POST)  # this will retrieve the
    # collects the data inputed by user to be saved
    newGame = gameForm.save(commit=None)  # saves the data for future use
    newGame.gameMakeIdKey = gameCollector  # makes the gameCollector or person signed in to use
    newGame.save() # I ain't loosing no points for not commenting every line of code, this one saves the game made with the foreignkey linked
    return redirect('index')  # goes back to the index page
