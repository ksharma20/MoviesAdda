from django.db import models
from django.contrib.auth.models import User
from Home.models import Movies

# Create your models here.
class FavMovies(models.Model):

    name = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name+' by '+self.user.username


