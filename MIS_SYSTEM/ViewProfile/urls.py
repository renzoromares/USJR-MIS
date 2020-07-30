from django.urls import path
from .import views
from ViewProfile.views import Profile


urlpatterns = [
    path('Profile/', Profile, name="profile"),
    path('Profile/<id>', Profile, name="profile")

]