import datetime
from datetime import time

from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.response import Response

from raffle import serializers
from raffle.models import Events, Winner


class EventView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Events.objects.filter(date__gte=datetime.datetime.today())


class WinnerView(generics.ListAPIView):
    serializer_class = serializers.WinnerSerializer
    queryset = Winner.objects.filter(ticket__event__date__gte=datetime.datetime.today() - datetime.timedelta(weeks=1))


class EventCreateView(generics.CreateAPIView):
    permission_classes = permissions.IsAdminUser,
    serializer_class = serializers.EventSerializer

    def post(self, request, *args, **kwargs):
        print(request.user)
        print(type(request.user))
        return self.create(request, *args, **kwargs)


class Participate(generics.GenericAPIView):
    permission_classes = permissions.IsAuthenticated,
    serializer_class = serializers.RaffleTicketSerializer

    def get(self, request, event_id):
        serializer = self.get_serializer(data={"event": event_id, **request.data})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(event_id=event_id)
            return Response(serializer.data)
        except IntegrityError as e:
            return Response({"error": "can participate only once per event"}, status=400)
        except Exception as e:
            return Response({"errors": serializer.errors}, status=400)
