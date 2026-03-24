from django.urls import path
from managementsystem.views import home, photoalbums, photoalbum_details

from managementsystem.apps import ManagementsystemConfig

app_name = ManagementsystemConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("photoalbums/", photoalbums, name='photoalbums'),
    path("photoalbums/<int:pk>/", photoalbum_details, name='photoalbum_details'),

]
