from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views import View

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MyTemplateView(View)
    def home(request):
        context = {
        'posts': Post.objects.all()
        }
        return render(request,'blog/home.html', context)

    def about(request):
        return render(request,'blog/about.html',{'title': 'About'})













