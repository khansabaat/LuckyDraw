import random

from django.contrib.auth.models import User
from rest_framework import serializers

from raffle import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Events
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class RaffleTicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = models.RaffleTickets
        fields = ("event", "number", "user")
        read_only_fields = ("number",)

    def create(self, validated_data):
        validated_data["number"] = random.randint(10000, 1000000)
        validated_data["user"] = self.context['request'].user
        return super().create(validated_data)


class WinnerSerializer(serializers.ModelSerializer):
    ticket = RaffleTicketSerializer()

    class Meta:
        model = models.Winner
        fields = "__all__"
