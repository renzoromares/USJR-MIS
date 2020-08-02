from django.urls import path
from .import views
from RoomTransfer.views import RoomTransfer

urlpatterns = [
   path('roomtransfer',RoomTransfer, name = "roomtransfer"),
   path('roomtransfer/<id>', RoomTransfer , name = "roomtransfer"),

]