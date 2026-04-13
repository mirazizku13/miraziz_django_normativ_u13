from django.db import models

from common.models import BaseModel, DeleteModel


class Genre(models.TextChoices):
    PVP = 'pvp', 'PvP'
    PVE = 'pve', 'PvE'
    RPG = 'rpg', 'RPG'
    FPS = 'fps', 'FPS'
    MMO = 'mmo', 'MMO'
    ADVENTURE = 'adventure', 'Adventure'
    STRATEGY = 'strategy', 'Strategy'
    SIMULATION = 'simulation', 'Simulation'
    SPORTS = 'sports', 'Sports'
    RACING = 'racing', 'Racing'
    MULTIPLAYER = 'multiplayer', 'Multiplayer'


class Game(BaseModel, DeleteModel):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=Genre.choices, default=Genre.PVP)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.title}'