from django.urls import path
from .import views
from MemoRouting.views import MemoRouting, MemoRoutingIngoing, MemoRoutingOutgoing


urlpatterns = [
   path('memorouting', MemoRouting , name = "memorouting"),
   path('memorouting/<id>', MemoRouting , name = "memorouting"),
   path('MemoOutgoing/<id>', MemoRoutingOutgoing , name = "memoroutingoutgoing"),
   path('MemoRouting<id>', MemoRoutingIngoing , name = "memoroutingincoming"),
]