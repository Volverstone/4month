from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post
# Create your views here.
def test_view(request):
    return HttpResponse (f"Hello,world{random.randint(0,1000)}")


def main_page_view(request):
    return render(request,"base.html")

def shablon_view(request):
    return render(request,"view1.html")

def answer_view(request):
    return render(request,"view2.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request,"posts/post_list.html", {"posts":posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html",{"post":post})

def privet_view(request):
    return render(request, "posts/privet.html")

