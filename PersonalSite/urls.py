"""
URL configuration for PersonalSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import re_path
from django.conf.urls import include
from Posts import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    re_path(r"^blog/$", views.blog, name="blog"),
    re_path(r"^blog/(page=(?P<pk>\d+))?/$", views.blog, name="blogPage"),
    re_path(r"^blog/(?P<pk>\w+)/$", views.blogPost, name="blogPost"),
    path("projects/", views.projects, name="projects"),
    path('admin/', admin.site.urls),
    path('newpost/', views.newPost, name="newpost"),
    path('newproject/', views.newProject, name="newproject"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
