from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'contents.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post.html", {'post': post})