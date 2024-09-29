"""
URL configuration for tilek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import (test_view, main_page_view,answer_view,shablon_view,
                         post_list_view, post_detail_view, privet_view, post_create_view,
                         update_view, PostListView, PostCreateView, PostDetailView)
from django.conf import settings
from django.conf.urls.static import static
from user.views import register_view, login_view, logout_view, profile_view
from parser.views import ParserView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name = 'register'),
    path('login',login_view, name = 'login'),
    path('logout/', logout_view, name = "logout"),
    path('test/',test_view),
    path('',main_page_view, name = 'main_page'),
    path('shablon/',shablon_view),
    path("posts2/", PostListView.as_view(), name="post_list"),
    path("posts2/create", PostCreateView.as_view(), name="post_create"),
    path("posts2/<int:post_id>/",PostDetailView.as_view(), name="post_detail"),
    path('answer/',answer_view),
    path("posts/", post_list_view, name="post_list"),
    path("posts/<int:post_id>/",post_detail_view, name = "post_detail"),
    path("privet/",  privet_view),
    path("posts/create/", post_create_view, name='post_create'),
    path("profile/", profile_view, name="profile"),
    path("posts/<int:post_id>/update", update_view, name='post_update'),
    path("parsing/", ParserView.as_view(), name='parser' )
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

