from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def test_view(request):
    return HttpResponse (f"Hello,world{random.randint(0,1000)}")


def main_page_view(request):
    return render(request,"base.html")

def shablon_view(request):
    return render(request,"view1.html")

def answer_view(request):
    return render(request,"view2.html")
