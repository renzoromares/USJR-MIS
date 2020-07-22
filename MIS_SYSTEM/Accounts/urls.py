from django.urls import path
from .import views
from Accounts.views import Home, Register, Dashboard


urlpatterns = [
    path('',Home, name = 'home'),
    path('register/', Register, name="register"),
    path('dashboard/', Dashboard, name="dashboard")
]
