from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from .models import Post



class HomeIndexPage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


