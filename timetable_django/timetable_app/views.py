from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import Q
from pytz import timezone

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import authentication, permissions

from .models import Event, User, CommonGroup
from .serializers import *

from datetime import datetime, timedelta


TZ = timezone('Europe/Moscow')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return []

        return User.objects.filter(pk=pk)


class CommonGroupViewSet(viewsets.ModelViewSet):
    serializer_class = CommonGroupSerializer
    queryset = CommonGroup.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return []

        return Event.objects.filter(pk=pk)


class EventDayView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, mydate):
        start_of_day = datetime.combine(mydate, datetime.min.time(), tzinfo=TZ)
        end_of_day = datetime.combine(mydate, datetime.max.time(), tzinfo=TZ)
        q = Q()
        user_groups = request.user.participant_groups.all()
        events = []
        if user_groups:
            for group in user_groups:
                q |= Q(participant_groups=group)
                print(group.name)
            events_raw = Event.objects.filter(
                q & (
                Q(start__range=(start_of_day, end_of_day)) |
                Q(repeat=timedelta(days=1)) |
                Q(repeat=timedelta(weeks=1), start__week_day=mydate.weekday()) |
                Q(repeat=timedelta(weeks=2), start__week_day=mydate.weekday())
                ))
            events = proceed_day_events(events_raw, start_of_day)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventWeekView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, mydate):

        q = Q()
        for group in request.user.participant_groups.all():
            q |= Q(participant_groups=group)

        events = Event.objects.filter(
            q & (
            Q(start__week=mydate.isocalendar()[1], start__year=mydate.today().year) |
            Q(repeat=timedelta(weeks=1)) |
            Q(repeat=timedelta(weeks=2))
            ))

        everyday_events = Event.objects.filter(
            q & (
            Q(repeat=timedelta(days=1)) &
            ~Q(start__week=mydate.isocalendar()[1], start__year=mydate.today().year)
            ))

        response_data = {}
        for i in range(7):
            response_data[i] = list(everyday_events)

        for event in events:
            response_data[event.start.weekday()].append(event)

        start_of_day = datetime.combine(mydate, datetime.min.time(), tzinfo=TZ)
        for i in range(7):
            response_data[i] = proceed_day_events(response_data[i], start_of_day)
            serializer = EventSerializer(response_data[i], many=True)
            response_data[i] = serializer.data

        return Response(response_data)


def proceed_day_events(events_raw, start_of_day):
    events = []
    for event in events_raw:
        if event.repeat != timedelta(days=0, seconds=0):
            event.start = event.start.replace(year=start_of_day.year,
                                              month=start_of_day.month,
                                              day=start_of_day.day)

        if event.repeat == timedelta(weeks=2):
            if event.start.weekday() % 2 == start_of_day.weekday() % 2:
                events.append(event)
        else:
            events.append(event)

    return sorted(events, key=lambda x: x.start)

