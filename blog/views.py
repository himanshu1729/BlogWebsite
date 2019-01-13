from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Likes
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.




""" def home(request):
    context = {
        'title' : 'Posts',
        'posts' : Post.objects.all(),
    }
    return render(request, 'blog/home.html',context) """


## Rewriting 'Home view' as class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostUserListView(LoginRequiredMixin, ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(author = self.request.user)

class LikedPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        likes= Likes.objects.filter(user = self.request.user)
        post = [0]*len(likes)
        i = 0
        for like in likes:
            post[i] = like.post
            i += 1
        return post

def about(request):
    context = {}
    return render(request,'blog/about.html', context)

def testpage(request):
    return HttpResponse('<h1>Test Page for Blog app</h1>')


    ## Here we are not passing template 
    ## as we have named our template according 
    ## to Django default class view template name
    #  Pattern <app>/<model>_<viewtype>.html
    #  Our Template Name =  user/post_detail.html

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
