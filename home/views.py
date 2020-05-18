from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HomeImage, Post
from django.utils import timezone

def home(request):
    images = HomeImage.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/home.html', {'images': images, 'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})
