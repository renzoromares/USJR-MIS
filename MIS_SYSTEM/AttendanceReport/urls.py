from django.urls import path
from .import views
from AttendanceReport.views import AttendanceReport



urlpatterns = [

  path('attendancereport',AttendanceReport, name = "attendancereport"),
  path('attendancereport/<id>', AttendanceReport , name = "attendancereport"),

]