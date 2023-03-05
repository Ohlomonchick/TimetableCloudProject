from django.db import models
from django.conf import settings
from datetime import timedelta
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class CommonGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class User(AbstractUser):
    participant_groups = models.ManyToManyField(
        CommonGroup,
        related_name='users',
        blank=True,
    )


class Event(models.Model):
    DEFAULT_DELTA = timedelta(days=0, seconds=0)
    DELTA_CHOICES = [
        (DEFAULT_DELTA, "never"),
        (timedelta(days=1), "day"),
        (timedelta(weeks=1), "week"),
        (timedelta(weeks=2), "two weeks"),
    ]

    name = models.CharField(max_length=255)
    place = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    repeat = models.DurationField(default=DEFAULT_DELTA, choices=DELTA_CHOICES)
    category = models.ForeignKey(
        Category,
        related_name='events',
        on_delete=models.PROTECT,
    )
    participant_groups = models.ManyToManyField(
        CommonGroup,
        related_name='events',
        blank=True,
    )
    master = models.ForeignKey(
        User,
        related_name='events',
        on_delete=models.CASCADE,
        blank=True,
    )

    class Meta:
        ordering = ('start', )

    def __str__(self):
        return self.name

