from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from main.models import Post
from datetime import datetime
# Create your views here.


class Posts(View):
    def get(self, request):
    	november_start = datetime(2014, 11, 1)
        posts = Post.objects.all().order_by('-when').filter(when__gt=november_start)
        """ SELECT * from POST WHERE when>='1.11.2014 ORDER by when; """
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))

