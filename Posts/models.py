from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique = True)
    snippet = models.TextField()
    content = models.TextField()
    picture = models.ImageField(upload_to='images/')
    timePosted = models.DateTimeField(null=True, blank=True)
    timeLastEdit = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=255, unique = True)
    description = models.TextField()
    link = models.TextField()
    picture = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title