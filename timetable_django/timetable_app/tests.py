from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

from django.test import TestCase

# Create your tests here.

class TestTimetable(TestCase):
    def test_index(self) -> None:
        request = self.client.get("/timetable_app/")
