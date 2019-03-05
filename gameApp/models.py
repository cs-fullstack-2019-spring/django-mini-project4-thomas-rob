
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# The game collector should have the following:
#
# username
# Password1
# Password2
# dateAccountCreated (not user created)
# rank (not user created. default is "grunt")
# foreignKey to DjangoUser table


class GameCollectorModel(models.Model):
    username= models.CharField(max_length=100)
    password1= models.CharField(max_length=200)
    password2= models.CharField(max_length=200)
    accountCreationDate= models.DateField(default=timezone.now())
    rank= models.CharField(max_length=10,default='grunt')
    userIDkey= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.username


# The games they add should have the following:
#
# name
# developer
# dateMade (with validation)
# ageLimit (with validation)
# foreignKey to game collector

class GameModel(models.Model):
    name= models.CharField(max_length=200)
    developer= models.CharField(max_length=300)
    releaseDate= models.DateField(default=timezone.now())
    esbrRating= models.CharField(max_length=20)
    gameMakeIdKey= models.ForeignKey(GameCollectorModel,on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.name
