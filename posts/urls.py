from django.urls import path

from .views import post_new

urlpatterns = [
    path('new/', post_new, name='post_new'),
]