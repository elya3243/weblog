from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


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
    return redirect('login')
