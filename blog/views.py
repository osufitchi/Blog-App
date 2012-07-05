# Create your views here.
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponseRedirect
from blog.models import Post, PostForm
def create_post(request):
    if request.method == 'POST':
       post = PostForm(request.POST)
       if post.is_valid():
           post.save()
           return HttpResponseRedirect('/blog')
    else:
        post = PostForm()
    return render_to_response('blog/create_post.html',{'post':post})
