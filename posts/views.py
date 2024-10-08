from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post, Comment, Tag
from django.shortcuts import redirect

from django.db.models import Q

from posts.form import PostForm2, CommentForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView, DetailView


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

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm2
    success_url = "posts2/"

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    success_url = "posts2/"



@login_required(login_url="login")
def post_list_view(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        posts = Post.objects.all()
        search = request.GET.get("search")
        tag = request.GET.getlist("tag")
        ordering = request.GET.get("ordering")
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tag:
            posts = posts.filter(tags__id__in=tag)
        if ordering:
            posts = posts.order_by(ordering)

        page = request.GET.get("page", 1)
        page = int(page)
        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) +1
        else:
            max_pages = round(max_pages)

        start = (page-1) * limit
        end = page * limit

        posts = posts[start:end]
        context = {"posts": posts, "form": form, "max_pages": range(1, max_pages+1)}
        return render(request,"posts/post_list.html", context=context)

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

@login_required(login_url="login")
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

def update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        form = PostForm2(instance=post)
        return render(request, "posts/post_update.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "posts/post_update.html", context={"form": form})
        form.save()
        return redirect("/posts/")





