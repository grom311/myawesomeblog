from django.shortcuts import render, get_object_or_404
from .models import Event
# Create your views here.


def showblog(request):
    posts = Event.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):
    post = get_object_or_404(Event, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': post})