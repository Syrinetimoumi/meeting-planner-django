from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} on floor {self.floor_number}, room {self.room_number}"
