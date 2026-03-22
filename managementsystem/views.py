from django.shortcuts import render
from .models import Banner

# Create your views here.
def home(request):
    banners = Banner.objects.filter(is_active=True)
    return render(request, 'managementsystem/main.html', {'banners': banners})
