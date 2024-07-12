from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from Posts.forms import NewPostForm, NewProjectForm
from django.utils import timezone
from .models import Post, Project
import math
# Create your views here.


def home(request):
    projectsfull = Project.objects.all()
    projectsfull = list(projectsfull)
    if len(projectsfull) < 3:
        projects = projectsfull
    else:
        projects = projectsfull[:3]
    return render(request, "home.html", {"projects": projects})

def about(request):
    return render(request, "about.html")

def blog(request, pk=1):
    pk = int(pk)
    posts = Post.objects.all()
    numOfPosts = len(list(posts))
    postsPerPage= 15
    numOfPages = math.ceil(numOfPosts/postsPerPage)
    firstPage = False
    lastPage = False
    startIndex = 0
    endIndex = 0

    print(pk)
    print(numOfPages)
    if numOfPages < 2:
        return render(request, "blog.html", {"posts": posts, "firstPage": True, "lastPage": True, "pk":pk})
    
    if pk > numOfPages:
        pk = numOfPages
    elif pk < 1:
        pk = 1

    if pk == numOfPages:
        startIndex = postsPerPage * (numOfPages - 1 )
        endIndex = len(list(posts))
    elif pk == 1:
        startIndex = 0
        endIndex = postsPerPage
    else:
        startIndex = postsPerPage * (pk - 1 )
        endIndex = postsPerPage * (pk)
    
    if pk == 1:
        firstPage = True
    if pk == numOfPages:
        lastPage = True

    realPosts = list(posts)[startIndex:endIndex]

    return render(request, "blog.html", {"posts": realPosts, "firstPage": firstPage, "lastPage": lastPage, "pk":pk})

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