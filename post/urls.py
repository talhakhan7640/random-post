from django.contrib import admin
from django.urls import path
from . views import postListView, postDetailView, postCreateView, postUpdateView, postDeleteView
from . import views

urlpatterns = [
    path('random-post/', postListView.as_view(), name='blog-home'),
    path('random-post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('random-post/new/', postCreateView.as_view(), name='post-create'),
    path('random-post/<int:pk>/update/', postUpdateView.as_view(), name='post-update'),
    path('random-post/<int:pk>/delete/', postDeleteView.as_view(), name='post-delete'),
    path('random-post/about/', views.about, name='blog-about'),
    path('random-post/announcements/', views.announcments, name='blog-announcements'),
    path('random-post/search-result/', views.search, name='search-result'),
]