from django.db import models

# Create your models here.
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)  #
    released_date = models.DateField()  #
    popularity = models.FloatField()  #
    vote_count = models.IntegerField()  #
    vote_avg = models.FloatField()  #
    overview = models.TextField()  #
    poster_path = models.CharField(max_length=200)  #
    genres = models.ManyToManyField(Genre)  #

