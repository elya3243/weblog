from django.urls import path
from . import views

urlpatterns = [
    path('sinin/',views.user_sin_in, mame = 'user_sin_in'),
    path('sinout/',views.user_sin_out, name = 'user_sin_out'),
]