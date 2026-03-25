from django.shortcuts import render, get_object_or_404
from .models import Banner, GymActivity, PhotoAlbum, SubscriptionPlan
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

def photoalbum_detail(request, pk):
    album = get_object_or_404(PhotoAlbum.objects.prefetch_related('photos'), pk=pk)
    images=album.photos.filter(is_active=True).order_by('order', 'created_at')
    return render(request, 'managementsystem/photoalbum_detail.html',{'album':album,'images':images})

def subscriptionplan(request):
    subscriptionplan = SubscriptionPlan.objects.filter(is_active=True)
    return render(request, 'managementsystem/subscription_plans.html',{'tarifs':subscriptionplan})
