from django.db import models

class Boardgame(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    min_player_count = models.IntegerField(default=1)
    max_player_count = models.IntegerField(default=99)
    play_time = models.IntegerField(null=True)
    publisher = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Designer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designs = models.ManyToManyField(Boardgame, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


