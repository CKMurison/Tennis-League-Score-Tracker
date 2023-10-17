from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    games_for = models.IntegerField()
    games_against = models.IntegerField()
    game_difference = models.IntegerField()
    total_points = models.FloatField()
    form = models.CharField(max_length=10)
    bbb = models.IntegerField()
    wsb = models.IntegerField()
    tsb = models.IntegerField()
    bp = models.IntegerField()
    jvm = models.FloatField()