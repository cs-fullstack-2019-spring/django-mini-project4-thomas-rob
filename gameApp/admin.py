from django.contrib import admin
from .forms import GameCollectorForm , GameCollectorModel , GameForm , GameModel
# Register your models here.


admin.site.register(GameCollectorModel)
admin.site.register(GameModel)