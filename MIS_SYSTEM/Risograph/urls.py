from django.urls import path
from .import views
from Risograph.views import Risograph


urlpatterns = [
  
   path('risograph',Risograph, name = "risograph"),
   path('risograph/<id>', Risograph , name = "risograph"),

]