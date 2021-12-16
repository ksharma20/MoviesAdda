from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movies(models.Model):

    name = models.CharField(default='Unknown', max_length=50)
    rate = models.IntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


