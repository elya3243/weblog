from django.urls import path
from . import views

urlpatterns=[
    path('add/', views.post_add, name='post_add'),
    path('list/', views.post_list, name='post_list'),
]