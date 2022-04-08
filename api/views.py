from django.shortcuts import render
from rest_framework import generics
from .serializers import EventSerializer
from .models import Event

# Create your views here.

class EventView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer