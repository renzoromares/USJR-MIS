from django.urls import path
from .import views
from ViewRequest.views import ViewRequestPres, ViewRequestReads, ViewRequestFac, ViewRequestIncoming, ViewRequestOutgoing

urlpatterns = [

    path('View-Request-President/<id>', ViewRequestPres, name="viewrequestpres"),
    path('View-Request-READS/<id>', ViewRequestReads, name="viewrequestreads"),
    path('View-Request-Faculty/<id>', ViewRequestFac, name="viewrequestfac"),
    path('View-Request-Incoming/<id>', ViewRequestIncoming, name="viewrequestincoming"),
    path('View-Request-Outgoing/<id>', ViewRequestOutgoing, name="viewrequestoutgoing")

]