from django.shortcuts import render, get_object_or_404
from .models import Blog


def posts(request):
    blog_counts = Blog.objects.count()
    blogs = Blog.objects.order_by('-date')
    print(blogs)
    return render(request, 'blog/posts.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
