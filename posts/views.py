from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post, Comment
from django.shortcuts import redirect

from posts.form import PostForm2, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def test_view(request):
    return HttpResponse (f"Hello,world{random.randint(0,1000)}")



def main_page_view(request):
    if request.method == "GET":
        return render(request,"base.html")

def shablon_view(request):
    return render(request,"view1.html")

def answer_view(request):
    return render(request,"view2.html")

@login_required(login_url="login")
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request,"posts/post_list.html", {"posts":posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "GET":
        form = CommentForm()
        comments = post.comments.all()
        return render(request, "posts/post_detail.html",{"post":post ,
                      "form": form, "comments": comments})
    if request.method == "POST":
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(request, "posts/post_detail.html",{"post":post ,
                      "form": form})
    text = form.cleaned_data.get("text")
    Comment.objects.create(text=text, post=post)
    return redirect(f"/posts/{post.id}/")


def privet_view(request):
    return render(request, "posts/privet.html")

def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_create_html.html", context ={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create_html.html", context={"form": form})

        form.save()
        return redirect("/posts/")


