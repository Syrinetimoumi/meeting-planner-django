from django.db import models
from datetime import time

# Define the Room model
class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} on floor {self.floor_number}, room {self.room_number}"

# Define the Meeting model
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    