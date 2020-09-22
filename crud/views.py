from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post


# Create your views here.

class BlogListView(ListView):
    template_name='list.html'
    model=Post

class BlogDetailView(DetailView):
    template_name='detail.html'
    model = Post

class BlogCreateView(CreateView):
    template_name='create.html'
    model=Post
    fields = ['title' ,'author','body']

class BlogUpdateView(UpdateView):
    template_name='edit.html'
    model=Post

class BlogDeleteView(DeleteView):
    template_name='del.html'
    model=Post