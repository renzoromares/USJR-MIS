from django.urls import path
from .import views
from Accounts.views import Home, Register, Dashboard


urlpatterns = [
    path('',Home, name = 'home'),
    path('Register/', Register, name="register"),
    path('Dashboard/', Dashboard, name="dashboard"),
    path('Dashboard/<id>', Dashboard, name="dashboard")
    
]