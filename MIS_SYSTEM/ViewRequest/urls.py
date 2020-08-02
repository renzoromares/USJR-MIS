from django.urls import path
from .import views
from ViewRequest.views import ViewRequestPres, ViewRequestReads, ViewRequestFac

urlpatterns = [

    path('View-Request-President/', ViewRequestPres, name="viewrequestpres"),
    path('View-Request-READS/', ViewRequestReads, name="viewrequestreads"),
    path('View-Request-Faculty/', ViewRequestFac, name="viewrequestfac"),

]