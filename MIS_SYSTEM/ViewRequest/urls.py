from django.urls import path
from .import views
from ViewRequest.views import ViewRequestPres, ViewRequestReads, ViewRequestFac

urlpatterns = [

    path('View-Request-President/<id>', ViewRequestPres, name="viewrequestpres"),
    path('View-Request-READS/<id>', ViewRequestReads, name="viewrequestreads"),
    path('View-Request-Faculty/<id>', ViewRequestFac, name="viewrequestfac"),

]