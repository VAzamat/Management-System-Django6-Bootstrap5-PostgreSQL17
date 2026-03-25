from django.urls import path
from managementsystem.views import home, photoalbums, photoalbum_detail, subscriptionplan

from managementsystem.apps import ManagementsystemConfig

app_name = ManagementsystemConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("photoalbums/", photoalbums, name='photoalbums'),
    path("photoalbum_detail/<uuid:pk>/", photoalbum_detail, name='photoalbum_detail'),
    path("subscribtionplan/", subscriptionplan, name='subscribtionplan'),

]
