from django.urls import path, include

from timetable_app import views

urlpatterns = [
    path('day/', views.EventListView.as_view()),
]