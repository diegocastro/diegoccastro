from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now).order_by('published_date')
    context_object_name = 'post_list'
    template_name = "blog/post_list.html"
