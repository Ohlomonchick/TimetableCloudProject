from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Dict, List

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

from datetime import datetime, date


class EventDayView(APIView):
    def get(self, request, mydate) -> Response:
        start_of_day: datetime = datetime.combine(mydate, datetime.min.time())
        end_of_day: datetime = datetime.combine(mydate, datetime.max.time())
        events = Event.objects.filter(start__range=(start_of_day, end_of_day))
        serializer: EventSerializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventWeekView(APIView):
    def get(self, request, mydate) -> Response:
        events = Event.objects.filter(start__week=mydate.isocalendar()[1], start__year=mydate.today().year)
        response_data: Dict[int, List] = {i: [] for i in range(7)}
        
        for event in events:
            serializer: EventSerializer = EventSerializer(event)
            response_data[event.start.weekday()].append(serializer.data)

        return Response(response_data)

