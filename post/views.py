from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

# Create your views here.

def post_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            Post.objects.create(title=title, body=body)
            messages.success(request,'Post add successfully.')
            return redirect('post_list')
    return render(request, 'add.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})