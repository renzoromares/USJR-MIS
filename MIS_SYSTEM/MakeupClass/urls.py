from django.urls import path
from MakeupClass.views import MakeupClass



urlpatterns = [
  path('makeupclass',MakeupClass, name = "makeupclass"),
  path('makeupclass/<id>', MakeupClass , name = "makeupclass"),
]