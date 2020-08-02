from django.urls import path
from .import views
from MemoRouting.views import MemoRouting


urlpatterns = [
   path('memorouting', MemoRouting , name = "memorouting"),
   path('memorouting/<id>', MemoRouting , name = "memorouting"),
]