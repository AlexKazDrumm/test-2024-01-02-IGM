from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name="games")
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    poster_path = models.URLField(null=True, blank=True)
    backdrop_path = models.URLField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    license_type = models.CharField(max_length=50, null=True, blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title