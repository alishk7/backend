from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name = 'custom_user_grops',
        blank = True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )



# Create your models here.
