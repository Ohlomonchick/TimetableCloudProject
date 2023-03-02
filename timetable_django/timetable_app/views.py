from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

from datetime import datetime, date


class EventDayView(APIView):

    def get(self, request, mydate):
        start_of_day = datetime.combine(mydate, datetime.min.time())
        end_of_day = datetime.combine(mydate, datetime.max.time())
        events = Event.objects.filter(start__range=(start_of_day, end_of_day))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventWeekView(APIView):

    def get(self, request, mydate):
        start_of_day = datetime.combine(mydate, datetime.min.time())
        end_of_day = datetime.combine(mydate, datetime.max.time())
        events = Event.objects.filter(start__range=(start_of_day, end_of_day))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

