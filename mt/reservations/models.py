from django.db import models
from django.contrib.auth import get_user_model
from tables.models import Table

User = get_user_model()

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ('table', 'date')

    def __str__(self):
        return f'Reservation by {self.user.username} on {self.date} - {self.status}'
    
# Create your models here.
