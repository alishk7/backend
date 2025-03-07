from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)

    def _str_(self):
        return self.title

# Create your models here.
