from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
                 

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})
