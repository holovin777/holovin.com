from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import HomeImage

def home(request):
    images = HomeImage.objects.all()
    return render(request, 'home/home.html', {'images': images})
