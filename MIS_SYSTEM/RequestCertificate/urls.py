from django.urls import path
from .import views
from RequestCertificate.views import RequestCertificate



urlpatterns = [
  path('requestcertificate',RequestCertificate, name = "requestcertificate"),
  path('requestcertificate/<id>', RequestCertificate , name = "requestcertificate"),
]