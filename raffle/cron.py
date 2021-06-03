import datetime
import random

from raffle.models import RaffleTickets, Winner


def calculate_winner():
    qs = RaffleTickets.objects.filter(event__date=datetime.datetime.today() - datetime.timedelta(days=1))
    count = qs.count()
    if not count:
        return
    ticket = qs[random.randint(0, count - 1)]
    winner = Winner.objects.create(ticket=ticket)
