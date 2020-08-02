from django.urls import path
from .import views
from CashAdvance.views import CashAdvance

urlpatterns = [
  path('cashadvance',CashAdvance, name = "cashadvance"),
  path('cashadvance/<id>', CashAdvance , name = "cashadvance"),
]