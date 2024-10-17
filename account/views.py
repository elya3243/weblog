from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from post.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


# Create your views here.

def user_profile(request):
    return render(request, 'profile.html', )


def user_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
            return redirect('user_sign_in')
    return render(request, 'sign-in.html')


def user_sign_out(request):
    logout(request)
    messages.success(request, 'خروج کاربر انجام شد.')
    return redirect('user_sign_in')


def user_profile(request):
    user = request.user
    posts = Post.objects.filter(author=request.user)
    post_count = posts.count()
    return render(request, 'profile.html', {'user': user, 'post_count': post_count})


@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phon_number = request.POST.get('phonnumber')
        user.firstname = first_name
        user.lastname = last_name
        user.email = email
        user.phonnumber = phon_number
        request.user.save()
        messages.success(request, 'تعییرات با موفقیت ثبت شد.')
        return redirect('user_profile')
    return render(request, 'profile.html', {'username': user.username, 'password': user.password})


@login_required
def change_password(request):
    if request.method == 'Post':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if not check_password(current_password, request.user.password):
            messages.error(request, 'رمز عبور فعلی اشتباه است.')
            return render(request, 'profile.html')
        if new_password != confirm_password:
            messages.error(request, 'رمز عبور جدید و تاییدیه آن تطابق ندارد.')
            return render(request, 'profile.html')
        if len(new_password) < 8:
            messages.error(request, 'رمز عبور باید حداقل 8 کاراکتر باشد.')
            return render(request, 'profile.html')
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.success(request, 'رمز عبور با موفقیت تغییر کرد.')
        return redirect('user_profile')
    return render(request, 'profile.html')
