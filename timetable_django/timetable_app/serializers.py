from rest_framework import serializers

from .models import Category, CommonGroup, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "place",
            "start",
            "end",
            "repeat",
            "category",
            "master",
        )