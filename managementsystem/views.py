from django.shortcuts import render
from .models import Banner, GymActivity
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
