from django.urls import path
from . import views

urlpatterns = [
    path('signin/',views.user_sign_in, name = 'user_sign_in'),
    path('signout/',views.user_sign_out, name = 'user_sign_out'),
]