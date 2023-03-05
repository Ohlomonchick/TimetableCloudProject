from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Category, CommonGroup, Event, User


class CommonGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonGroup
        fields = (
            "id",
            "name"
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )


class EventSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    participant_groups = CommonGroupSerializer(many=True)

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
            "participant_groups",
        )


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    participant_groups = CommonGroupSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "participant_groups",
        )