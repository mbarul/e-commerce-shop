from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_one(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',)
                             #publish_year=year, publish_month=month, publish_day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
