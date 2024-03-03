# Ваш файл models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.OneToOneField('Director', on_delete=models.CASCADE, related_name='movie', null=True, blank=True)

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()
    duration = models.IntegerField()

class Hall(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    sessions = models.ManyToManyField(Session, related_name='halls')

class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
