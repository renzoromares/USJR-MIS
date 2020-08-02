from django.urls import path
from .import views
from ScheduleTransfer.views import ScheduleTransfer



urlpatterns = [
   path('scheduletransfer',ScheduleTransfer, name = "scheduletransfer"),
   path('scheduletransfer/<id>', ScheduleTransfer , name = "scheduletransfer"),
]