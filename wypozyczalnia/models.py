from msilib.schema import Directory
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.forms import ValidationError

class Rental(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Books(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=64)
    isbn = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999999)], unique=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    class Meta:
        unique_together="author","title","genre"
    def __str__(self):
        return "Book "+self.title

class Movies(models.Model):
    director = models.CharField(max_length=64)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=64)
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    def clean(self):
        if Movies.objects.filter(director=self.director, title=self.title).exists():
            for movie in Movies.objects.filter(director=self.director, title=self.title):
                if movie.duration == self.duration:
                    print('jest')
                    raise ValidationError(u"Cannot add this movie")
    def __str__(self):
        return "Movie "+self.title

class CD(models.Model):
    band = models.CharField(max_length=64)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=64)
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    def clean(self):
        genre_list = []
        for cd in CD.objects.all():
            if cd.genre in genre_list:
                continue
            else:
                genre_list.append(cd.genre)
        if (len(genre_list) > 1) and (not self.genre in genre_list):
            raise ValidationError(u"Cannot add this CD for that band")

    def __str__(self):
        return "CD "+self.title

class Songs(models.Model):
    title = models.CharField(max_length=200)
    Cd = models.ForeignKey(CD, on_delete=models.CASCADE)
    def clean(self):
        song_list = []
        for cd in CD.objects.filter(genre=self.Cd.genre):
            cds_songs = []
            for song in Songs.objects.filter(Cd=cd):
                cds_songs.append(song.title)
            song_list.append(cds_songs)
        print(song_list)
        for cd in range(len(song_list)):
            for cd2 in range(len(song_list)):
                if cd == cd2:
                    continue
                if song_list[cd] == song_list[cd2]:
                    raise ValidationError(u"You cannot add this song to CD with this genre")
    def __str__(self):
        return "Song "+self.title