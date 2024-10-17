from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.user_sign_in, name='user_sign_in'),
    path('signout/', views.user_sign_out, name='user_sign_out'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('changepassword/', views.change_password, name='change_password'),
]
