from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    # Create your models here.
