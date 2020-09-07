from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)
    # return HttpResponse('<h1>Blog Home</h1>')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post




def about(request):
    return render(request,'blog/about.html',{'title': 'D_about'})
    # return HttpResponse('<h1>Blog Abouts</h1>')