from django.urls import path
from .import views
from RoomTransfer.views import RoomTransfer, RoomTransferPermanent, RoomTransferTemporary

urlpatterns = [
   path('roomtransfer',RoomTransfer, name = "roomtransfer"),
   path('roomtransfer/<id>', RoomTransfer , name = "roomtransfer"),
   path('roomtransferpermanent/<id>', RoomTransferPermanent, name = "roomtransferpermanent"),
   path('roomtransfertemporary/<id>', RoomTransferTemporary, name ="roomtransfertemporary")
]