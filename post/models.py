from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="", blank=True)
    content = RichTextUploadingField(blank=False, null=True, default="")
    content_after = RichTextUploadingField(blank=True, null=True, default="")
    content_video_title = models.CharField(max_length=100, default="", blank=True)
    content_video_url = EmbedVideoField(null=True, blank=True)
    posted_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_related_images', blank=True)