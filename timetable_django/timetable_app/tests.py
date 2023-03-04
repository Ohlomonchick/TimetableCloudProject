from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rest_framework.response import Response
    pass

from django.test import TestCase

from .models import Category, CommonGroup, Event

# Create your tests here.

class TestTimetable(TestCase):
    def test_index(self) -> None:
        request: Response = self.client.get("/api/v1/day/12-12-2023")
        assert request.status_code == 200

