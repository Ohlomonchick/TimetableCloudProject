from django.urls import path, include, register_converter

from timetable_app import views
from timetable_app.converters import DateConverter
register_converter(DateConverter, 'date')

urlpatterns = [
    path('day/<date:mydate>', views.EventDayView.as_view()),
    path('week/<date:mydate>', views.EventWeekView.as_view()),
]