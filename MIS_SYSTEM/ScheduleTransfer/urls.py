from django.urls import path
from .import views
from ScheduleTransfer.views import ScheduleTransfer, ScheduleTransferPermanent, ScheduleTransferTemporary



urlpatterns = [
   path('scheduletransfer',ScheduleTransfer, name = "scheduletransfer"),
   path('scheduletransfer/<id>', ScheduleTransfer , name = "scheduletransfer"),
   path('ScheduleTransferPermanent/<id>', ScheduleTransferPermanent, name = "schedtransferpermanent"),
   path('ScheduleTransferTemporary/<id>', ScheduleTransferTemporary, name ="schedtransfertemporary")
]