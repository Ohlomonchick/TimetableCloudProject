from django.urls import path, include, register_converter

from timetable_app import views
from timetable_app.converters import DateConverter
from rest_framework import routers

register_converter(DateConverter, 'date')
router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('day/<date:mydate>', views.EventDayView.as_view()),
    path('week/<date:mydate>', views.EventWeekView.as_view()),
]