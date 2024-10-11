from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            Post.objects.create(title=title, body=body)
            messages.success(request, 'پست با موفقیت افزوده شد.')
            return redirect('post_list')
    return render(request, 'add.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'پست با موفقیت حذف شد.')
        return redirect('post_list')
    return render(request)
