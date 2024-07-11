from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from Posts.forms import NewPostForm, NewProjectForm
from django.utils import timezone
from .models import Post, Project
# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

def about(request):
    return render(request, "about.html")

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})

def blogPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "blogPost.html", {"post": post})

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

@login_required
def newPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.timePosted = timezone.now()
            post.timeLastEdit = timezone.now()
            post.save()
            return redirect('blog') 
        else:
            print(form.errors)
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {'form':form})

@login_required
def newProject(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.save()
            return redirect('projects') 
        else:
            print(form.errors)
    else:
        form = NewProjectForm()
    return render(request, 'newproject.html', {'form':form})