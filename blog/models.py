from django.db import models
from django.forms import ModelForm
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    

class PostForm(ModelForm):
    class Meta:
          model = Post
