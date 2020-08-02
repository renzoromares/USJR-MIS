from django.urls import path
from .import views
from MakeupClass.views import MakeupClass



urlpatterns = [
  path('makeupclass',MakeupClass, name = "makeupclass"),
  path('makeupclass/<id>', MakeupClass , name = "makeupclass"),
]