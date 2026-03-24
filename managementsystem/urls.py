from django.urls import path
from managementsystem.views import home, photoalbums

from managementsystem.apps import ManagementsystemConfig

app_name = ManagementsystemConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("photoalbums/", photoalbums, name='photoalbums'),

]
