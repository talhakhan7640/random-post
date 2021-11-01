from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

import post
from . models import Post, Images
from . forms import searchForm
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     post = {
#         'author': 'Niklaus',
#         'title': 'TVD',
#         'content': 'The Vampire Diaries',
#         ''
#     }
#     return render(request, 'post/home.html', {'post': post})

class postListView(ListView):
    model = Post
    template_name= 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-posted_date']
    paginate_by = 7

    # def word_count(self, request):
    #     for post in Post:
    #         content = post.content
    #         if len(content.split()) > 50:
    #             read
    #     return render(request, 'post/home', {'word_count':read_more})

class postDetailView(DetailView):
    context_object_name = 'post'
    model = Post

class postCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # post_author = User.objects.filter(username='talha').first()
    fields = ['title', 'description', 'content', 'content_video_title', 'content_video_url', 'content_after' ]

    def form_valid(self, form):
        author = User.objects.filter(username='talha').first()
        form.instance.author = author
        return super().form_valid(form)

class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content', 'content_video_title', 'content_video_url', 'content_after' ]

    def form_valid(self, form):
        author = User.objects.filter(username='talha').first()
        form.instance.author = author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if User.objects.filter(username='talha').first() == post.author:
            return True
        return False

class postDeleteView(DeleteView):
    model = Post
    success_url= reverse_lazy("blog-home")

    def test_func(self):
        post = self.get_object()
        if User.objects.filter(username='talha').first() == post.author:
            return True
        return False

def about(request):
    return render(request, 'post/about.html')

def announcments(request):
    return render(request, 'post/announcements.html')

def search(request):
    if request.method == 'POST':
        search = request.POST.get("search")
        return render(request, 'post/search.html', {'search': search })
    # search_input = request.POST.get("search-input", 'No results found :(')
    else:
        return render(request, 'post/home.html', {'search': 'No results found'})
    # return HttpResponse(search_input)
    