from django.shortcuts import render
from .models import Event
# Create your views here.


def showblog(request):
    posts = Event.objects
    return render(request, 'blog/blog.html', {'posts': posts})