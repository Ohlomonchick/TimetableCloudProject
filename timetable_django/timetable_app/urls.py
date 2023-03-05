from django.urls import path, include, register_converter

from timetable_app import views
from timetable_app.converters import DateConverter
from rest_framework import routers

register_converter(DateConverter, 'date')
router = routers.SimpleRouter()
router.register(r'event', views.EventViewSet, basename='event')
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'group', views.CommonGroupViewSet, basename='commongroup')
router.register(r'category', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('day/<date:mydate>', views.EventDayView.as_view()),
    path('week/<date:mydate>', views.EventWeekView.as_view()),
]