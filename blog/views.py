from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

def myview(sla):

    return HttpResponse('Hello')

# Create your views here.
def allblogs(request):
    blogs= Blog.objects
    return render(request, 'allblogs.html', context={'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': detailblog})