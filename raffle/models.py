from django.contrib.auth.models import User
from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=100)
    reward = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(null=False, blank=False)


class RaffleTickets(models.Model):
    number = models.IntegerField(unique=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "event"]


class Winner(models.Model):
    ticket = models.ForeignKey(RaffleTickets, on_delete=models.CASCADE)
