

from .models import Post, Category
from django.shortcuts import render, get_object_or_404
import markdown


# 首页
def index(request):

    post_list = Post.objects.all().order_by('-create_time')

    return render(request, 'blog/index.html', context= {'post_list' : post_list})


# 详情
def detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,'blog/detail.html', context={'post' : post})


# 归档
def archives(request, year, month):

    post_list = Post.objects.filter(
                create_time__year=year,
                create_time__month=month
    ).order_by('-create_time')

    return render(request, 'blog/index.html', context={'post_list' : post_list})


# 分页
def category(request, pk):

    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return  render(request, 'blog/index.html',context={'post_list' : post_list})
