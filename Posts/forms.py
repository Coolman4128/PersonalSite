from django import forms
from .models import Post
from .models import Project


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'snippet', 'content', 'picture']

class NewProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'link', "picture"]