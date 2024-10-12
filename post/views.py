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
            Post.objects.create(title=title, body=body , auther=request.user)
            messages.success(request, 'پست با موفقیت افزوده شد.')
            return redirect('post_list')
    return render(request, 'add.html')


@login_required
def post_list(request):
    user_posts = Post.objects.filter(auther=request.user)
    return render(request, 'list.html', {'posts': user_posts})



def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'پست با موفقیت حذف شد.')
        return redirect('post_list')
    return render(request)


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        if new_title and new_body:
            post.title = new_title
            post.body = new_body
            post.save()
            messages.success(request,'پست با موفقیت ویرایش شد.')
            return redirect('post_list')
    return render(request, 'edit.html', {'post': post})
