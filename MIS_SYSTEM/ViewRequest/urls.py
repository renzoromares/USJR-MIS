from django.urls import path
from .import views
from ViewRequest.views import ViewRequestPres, ViewRequestReads, ViewRequestFac, ViewRequestPao, ViewRequestIMS, ViewRequestDetails
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('View-Request-President/<id>', ViewRequestPres, name="viewrequestpres"),
    path('View-Request-READS/<id>', ViewRequestReads, name="viewrequestreads"),
    path('View-Request-Faculty/<id>', ViewRequestFac, name="viewrequestfac"),
    path('View-Request-PAO/<id>/<idr>', ViewRequestPao, name="viewrequestpao"),
    path('View-Request/View-Request-Details/<id>/<idf>/<idm>', ViewRequestDetails, name="viewrequestdetails"),
    path('View-Request-IMS/<id>', ViewRequestIMS, name="viewrequestims")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)