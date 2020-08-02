from django.urls import path
from .import views
from FileLeave.views import FileLeave




urlpatterns = [
  path('fileleave', FileLeave, name = "fileleave"),
  path('fileleave/<id>', FileLeave , name = "fileleave"),
]