from django.shortcuts import render, get_object_or_404
from .models import Banner, GymActivity, PhotoAlbum
import random
# Create your views here.
def home(request):
    banners = Banner.objects.filter(is_active=True)
    gymactivities = GymActivity.objects.filter(is_active=True)
    gymactivities_random = list(gymactivities)
    random.shuffle(gymactivities_random)
    return render(request,
                  'managementsystem/main.html',
                  {'banners': banners, 'gymactivities':gymactivities, 'gymactivities_random': gymactivities_random}
                  )

def photoalbums(request):
    photoalbums = PhotoAlbum.objects.filter(is_active=True)
    return render(request, 'managementsystem/photoalbums.html',{'photoalbums':photoalbums})

def photoalbum_details(request, pk):
    photoalbum = get_object_or_404(PhotoAlbum, pk=pk)
    return render(request, 'managementsystem/photoalbums.html',{'photoalbum':photoalbum})

