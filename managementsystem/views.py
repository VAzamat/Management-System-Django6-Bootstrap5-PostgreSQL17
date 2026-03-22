from django.shortcuts import render
from .models import Banner, GymActivity

# Create your views here.
def home(request):
    banners = Banner.objects.filter(is_active=True)
    gymactivities = GymActivity.objects.filter(is_active=True)
    return render(request,
                  'managementsystem/main.html',
                  {'banners': banners, 'gymactivities':gymactivities}
                  )
